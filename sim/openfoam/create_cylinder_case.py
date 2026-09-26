#!/usr/bin/env python3
"""Create OpenFOAM cylinder_test case for the condenser CFD.
Single 15 mm cylinder in crossflow, buoyantSimpleFoam."""

import os
import math

BASE = os.path.expanduser("~/projects/solar-absorption-fridge/sim/openfoam/cylinder_test")

for d in ["system", "constant", "constant/triSurface", "0"]:
    os.makedirs(os.path.join(BASE, d), exist_ok=True)


def write(path, content):
    full = os.path.join(BASE, path)
    with open(full, 'w') as f:
        f.write(content)
    print(f"  wrote {path}")


# ---------- system/blockMeshDict ----------
write("system/blockMeshDict", """FoamFile { version 2.0; format ascii; class dictionary; object blockMeshDict; }

scale   0.001;

vertices
(
    (-100 -100 -25)
    ( 100 -100 -25)
    ( 100  100 -25)
    (-100  100 -25)
    (-100 -100  25)
    ( 100 -100  25)
    ( 100  100  25)
    (-100  100  25)
);

blocks
(
    hex (0 1 2 3 4 5 6 7) (100 100 1) simpleGrading (1 1 1)
);

edges ();

boundary
(
    inlet  { type patch; faces ((0 4 7 3)); }
    outlet { type patch; faces ((1 2 6 5)); }
    top    { type patch; faces ((3 7 6 2)); }
    bottom { type patch; faces ((0 1 5 4)); }
    front  { type empty; faces ((0 3 2 1)); }
    back   { type empty; faces ((4 5 6 7)); }
);

mergePatchPairs ();
""")


# ---------- system/controlDict ----------
write("system/controlDict", """FoamFile { version 2.0; format ascii; class dictionary; object controlDict; }

application     buoyantSimpleFoam;
startFrom       startTime;
startTime       0;
stopAt          endTime;
endTime         3000;
deltaT          1;
writeControl    timeStep;
writeInterval   500;
purgeWrite      0;
writeFormat     ascii;
writePrecision  6;
writeCompression off;
timeFormat      general;
timePrecision   6;
runTimeModifiable true;
""")


# ---------- system/fvSchemes ----------
write("system/fvSchemes", """FoamFile { version 2.0; format ascii; class dictionary; object fvSchemes; }

ddtSchemes { default steadyState; }

gradSchemes
{
    default         Gauss linear;
    grad(U)         cellLimited Gauss linear 1;
}

divSchemes
{
    default         none;
    div(phi,U)      Gauss linearUpwind grad(U);
    div(phi,h)      Gauss upwind;
    div(phi,K)      Gauss linear;
    div(phi,k)      Gauss upwind;
    div(phi,omega)  Gauss upwind;
    div((muEff*dev2(T(grad(U))))) Gauss linear;
}

laplacianSchemes { default Gauss linear corrected; }
interpolationSchemes { default linear; }
snGradSchemes { default corrected; }
wallDist { method meshWave; }
""")


# ---------- system/fvSolution ----------
write("system/fvSolution", """FoamFile { version 2.0; format ascii; class dictionary; object fvSolution; }

solvers
{
    p_rgh
    {
        solver          GAMG;
        tolerance       1e-7;
        relTol          0.01;
        smoother        DIC;
    }
    "(U|h|k|omega)"
    {
        solver          PBiCGStab;
        preconditioner  DILU;
        tolerance       1e-8;
        relTol          0.1;
    }
}

SIMPLE
{
    nNonOrthogonalCorrectors 0;
    pRefCell        0;
    pRefValue       0;
    residualControl
    {
        p_rgh           1e-4;
        U               1e-4;
        "(h|k|omega)"   1e-4;
    }
}

relaxationFactors
{
    fields { p_rgh 0.3; }
    equations { U 0.7; h 0.7; k 0.7; omega 0.7; }
}
""")


# ---------- system/surfaceFeatureExtractDict ----------
write("system/surfaceFeatureExtractDict", """FoamFile { version 2.0; format ascii; class dictionary; object surfaceFeatureExtractDict; }

cylinder.stl
{
    extractionMethod    extractFromSurface;
    includedAngle       150;
    writeObj            yes;
}
""")


# ---------- system/snappyHexMeshDict ----------
write("system/snappyHexMeshDict", """FoamFile { version 2.0; format ascii; class dictionary; object snappyHexMeshDict; }

castellatedMesh true;
snap            true;
addLayers       true;

geometry
{
    cylinder.stl
    {
        type triSurfaceMesh;
        name cylinder;
    }
}

castellatedMeshControls
{
    maxLocalCells      200000;
    maxGlobalCells     500000;
    minRefinementCells 10;
    maxLoadUnbalance   0.10;
    nCellsBetweenLevels 3;

    features
    (
        { file "cylinder.eMesh"; level 3; }
    );

    refinementSurfaces
    {
        cylinder
        {
            level (2 3);
            patchInfo { type wall; }
        }
    }

    resolveFeatureAngle 30;
    refinementRegions {}
    locationInMesh (0.05 0.05 0);
    allowFreeStandingZoneFaces true;
}

snapControls
{
    nSmoothPatch    3;
    tolerance       2.0;
    nSolveIter      30;
    nRelaxIter      5;
}

addLayersControls
{
    relativeSizes   true;
    layers
    {
        cylinder { nSurfaceLayers 5; }
    }
    expansionRatio        1.2;
    finalLayerThickness   0.3;
    minThickness          0.1;
    nGrow                 0;
    featureAngle          60;
    slipFeatureAngle      30;
    nRelaxIter            3;
    nSmoothSurfaceNormals 1;
    nSmoothNormals        3;
    nSmoothThickness      10;
    maxFaceThicknessRatio 0.5;
    maxThicknessToMedialRatio 0.3;
    minMedianAxisAngle    90;
    nBufferCellsNoExtrude 0;
    nLayerIter            50;
}

meshQualityControls
{
    maxNonOrtho     65;
    maxBoundarySkewness 20;
    maxInternalSkewness 4;
    maxConcave      80;
    minVol          1e-13;
    minTetQuality   1e-15;
    minArea         -1;
    minTwist        0.02;
    minDeterminant  0.001;
    minFaceWeight   0.02;
    minVolRatio     0.01;
    minTriangleTwist -1;
    nSmoothScale    4;
    errorReduction  0.75;
}

debug           0;
mergeTolerance  1e-6;
""")


# ---------- constant/thermophysicalProperties ----------
write("constant/thermophysicalProperties", """FoamFile { version 2.0; format ascii; class dictionary; object thermophysicalProperties; }

thermoType
{
    type            hePsiThermo;
    mixture         pureMixture;
    transport       const;
    thermo          hConst;
    equationOfState perfectGas;
    specie          specie;
    energy          sensibleEnthalpy;
}

mixture
{
    specie          { molWeight 28.96; }
    thermodynamics  { Cp 1005; Hf 0; }
    transport       { mu 1.85e-05; Pr 0.71; }
}
""")


# ---------- constant/turbulenceProperties ----------
write("constant/turbulenceProperties", """FoamFile { version 2.0; format ascii; class dictionary; object turbulenceProperties; }

simulationType  RAS;

RAS
{
    RASModel        kOmegaSST;
    turbulence      on;
    printCoeffs     on;
}
""")


# ---------- 0/T ----------
write("0/T", """FoamFile { version 2.0; format ascii; class volScalarField; object T; }
dimensions      [0 0 0 1 0 0 0];
internalField   uniform 313.15;
boundaryField
{
    inlet  { type fixedValue; value uniform 313.15; }
    outlet { type inletOutlet; inletValue uniform 313.15; value uniform 313.15; }
    top    { type zeroGradient; }
    bottom { type zeroGradient; }
    "cylinder.*" { type fixedValue; value uniform 313.15; }
    front  { type empty; }
    back   { type empty; }
}
""")


# ---------- 0/U ----------
write("0/U", """FoamFile { version 2.0; format ascii; class volVectorField; object U; }
dimensions      [0 1 -1 0 0 0 0];
internalField   uniform (0.5 0 0);
boundaryField
{
    inlet  { type fixedValue; value uniform (0.5 0 0); }
    outlet { type inletOutlet; inletValue uniform (0 0 0); value uniform (0.5 0 0); }
    top    { type slip; }
    bottom { type slip; }
    "cylinder.*" { type noSlip; }
    front  { type empty; }
    back   { type empty; }
}
""")


# ---------- 0/p_rgh ----------
write("0/p_rgh", """FoamFile { version 2.0; format ascii; class volScalarField; object p_rgh; }
dimensions      [1 -1 -2 0 0 0 0];
internalField   uniform 0;
boundaryField
{
    inlet  { type fixedFluxPressure; value uniform 0; }
    outlet { type fixedValue; value uniform 0; }
    top    { type fixedFluxPressure; value uniform 0; }
    bottom { type fixedFluxPressure; value uniform 0; }
    "cylinder.*" { type fixedFluxPressure; value uniform 0; }
    front  { type empty; }
    back   { type empty; }
}
""")


# ---------- 0/k ----------
write("0/k", """FoamFile { version 2.0; format ascii; class volScalarField; object k; }
dimensions      [0 2 -2 0 0 0 0];
internalField   uniform 0.001;
boundaryField
{
    inlet  { type fixedValue; value uniform 0.001; }
    outlet { type inletOutlet; inletValue uniform 0.001; value uniform 0.001; }
    top    { type slip; }
    bottom { type slip; }
    "cylinder.*" { type kqRWallFunction; value uniform 0.001; }
    front  { type empty; }
    back   { type empty; }
}
""")


# ---------- 0/omega ----------
write("0/omega", """FoamFile { version 2.0; format ascii; class volScalarField; object omega; }
dimensions      [0 0 -1 0 0 0 0];
internalField   uniform 1;
boundaryField
{
    inlet  { type fixedValue; value uniform 1; }
    outlet { type inletOutlet; inletValue uniform 1; value uniform 1; }
    top    { type slip; }
    bottom { type slip; }
    "cylinder.*" { type omegaWallFunction; value uniform 1; }
    front  { type empty; }
    back   { type empty; }
}
""")


# ---------- 0/alphat ----------
write("0/alphat", """FoamFile { version 2.0; format ascii; class volScalarField; object alphat; }
dimensions      [1 -1 -1 0 0 0 0];
internalField   uniform 0;
boundaryField
{
    inlet  { type calculated; value uniform 0; }
    outlet { type calculated; value uniform 0; }
    top    { type calculated; value uniform 0; }
    bottom { type calculated; value uniform 0; }
    "cylinder.*" { type compressible::alphatWallFunction; Prt 0.85; value uniform 0; }
    front  { type empty; }
    back   { type empty; }
}
""")


# ---------- constant/triSurface/cylinder.stl ----------
def generate_cylinder_stl(path, radius=7.5, z_min=-25, z_max=25, n=48):
    lines = ["solid cylinder"]
    for i in range(n):
        t1 = 2 * math.pi * i / n
        t2 = 2 * math.pi * (i + 1) / n
        x1, y1 = radius * math.cos(t1), radius * math.sin(t1)
        x2, y2 = radius * math.cos(t2), radius * math.sin(t2)
        nx = (x1 + x2) / 2.0 / radius
        ny = (y1 + y2) / 2.0 / radius
        # Triangle 1
        lines.append(f"facet normal {nx:.6e} {ny:.6e} 0")
        lines.append("  outer loop")
        lines.append(f"    vertex {x1:.6e} {y1:.6e} {z_min:.6e}")
        lines.append(f"    vertex {x2:.6e} {y2:.6e} {z_min:.6e}")
        lines.append(f"    vertex {x2:.6e} {y2:.6e} {z_max:.6e}")
        lines.append("  endloop")
        lines.append("endfacet")
        # Triangle 2
        lines.append(f"facet normal {nx:.6e} {ny:.6e} 0")
        lines.append("  outer loop")
        lines.append(f"    vertex {x1:.6e} {y1:.6e} {z_min:.6e}")
        lines.append(f"    vertex {x2:.6e} {y2:.6e} {z_max:.6e}")
        lines.append(f"    vertex {x1:.6e} {y1:.6e} {z_max:.6e}")
        lines.append("  endloop")
        lines.append("endfacet")
    lines.append("endsolid cylinder")
    with open(path, 'w') as f:
        f.write('\n'.join(lines))
    print(f"  wrote constant/triSurface/cylinder.stl ({n} facets)")


generate_cylinder_stl(os.path.join(BASE, "constant/triSurface/cylinder.stl"))


# ---------- Allrun ----------
write("Allrun", """#!/bin/bash
cd "${0%/*}" || exit 1
source ~/.openfoam_env

echo "=== blockMesh ==="
blockMesh 2>&1 | tee log.blockMesh

echo "=== surfaceFeatureExtract ==="
surfaceFeatureExtract 2>&1 | tee log.surfaceFeatureExtract

echo "=== snappyHexMesh ==="
snappyHexMesh -overwrite 2>&1 | tee log.snappyHexMesh

echo "=== checkMesh ==="
checkMesh 2>&1 | tee log.checkMesh

echo "=== buoyantSimpleFoam ==="
buoyantSimpleFoam 2>&1 | tee log.solver

echo "=== Done ==="
""")

os.chmod(os.path.join(BASE, "Allrun"), 0o755)

print()
print("=" * 60)
print("cylinder_test case created")
print(f"Location: {BASE}")
print("=" * 60)

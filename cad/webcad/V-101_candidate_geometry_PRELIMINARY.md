# Preliminary WebCAD model — V-101 candidate geometry

**Status: PRELIMINARY GEOMETRY ONLY. NOT AN APPROVED DESIGN. NOT FOR FABRICATION, PRESSURE TESTING, AMMONIA CHARGING, OR OPERATION.**

This ArchScript records the candidate dimensions currently found in project records solely to make the geometry easy to retrieve and review. The values are not approved design dimensions.

- Candidate vessel length: 4000 mm
- Candidate outside diameter: 200 mm
- Candidate wall thickness: 2.5 mm
- Existing candidate flat-cap thickness: 5 mm
- Unresolved design-pressure conflict: 16 bar versus 25 bar
- Current thermodynamic model high-side pressure: approximately 15.55 bar (model output, not a verified operating limit)

The WebCAD geometry build passed. That result verifies only that WebCAD built the declared geometry. **No pressure-stress FEA was run.** The model does not demonstrate pressure-boundary adequacy, cap adequacy, code compliance, material suitability, or relief protection. The documented WebCAD FEA syntax found so far shows face forces; internal-pressure loading capability remains unverified.

ArchScript source:

    // PRELIMINARY GEOMETRY ONLY — NOT A PRESSURE-VESSEL DESIGN
    // Candidate V-101 dimensions from current project records; all dimensions unapproved.
    param vesselLength = 4000
    param outerRadius = 100
    param wallThickness = 2.5
    param capThickness = 5
    param innerRadius = outerRadius - wallThickness

    body shellBlank = cylinder radius outerRadius height vesselLength at [0, 0, 0] axis x
    body boreCutter = cylinder radius innerRadius height vesselLength + 2 at [0, 0, 0] axis x
    body shell = subtract shellBlank boreCutter

    body leftCap = cylinder radius outerRadius height capThickness at [-vesselLength / 2 - capThickness / 2, 0, 0] axis x
    body rightCap = cylinder radius outerRadius height capThickness at [vesselLength / 2 + capThickness / 2, 0, 0] axis x

    body v101_candidate_geometry = compound shell leftCap rightCap
    color v101_candidate_geometry 94A3B8

## Next actions

1. Resolve governing code/jurisdiction and approved design pressure and temperature with qualified pressure-equipment review.
2. Verify geometry, end closures, openings, joints and materials against controlled source documents.
3. Establish whether WebCAD can apply true distributed internal pressure to the vessel surfaces.
4. Only then determine a suitable, validated analysis route and compare it against independent calculations.
5. Analyze overpressure scenarios and relief-device sizing separately.

Do not close any HOLD gate on the basis of this geometry build.

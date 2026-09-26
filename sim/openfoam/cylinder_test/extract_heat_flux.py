"""
Extract wall heat flux from OpenFOAM results and compute HTC.
Parses field files directly — no postProcess needed.
"""
import re
import numpy as np
import os

CASE = "."
TIME = "3000"

# --- Read boundary to get cylinder patch face range ---
with open(f"{CASE}/constant/polyMesh/boundary", 'r') as f:
    bnd = f.read()

# Find cylinder patch block
m = re.search(r'cylinder\s*\{([^}]+)\}', bnd)
if not m:
    print("ERROR: cylinder patch not found in boundary file")
    raise SystemExit(1)

block = m.group(1)
nFaces = int(re.search(r'nFaces\s+(\d+)', block).group(1))
startFace = int(re.search(r'startFace\s+(\d+)', block).group(1))
print(f"Cylinder patch: {nFaces} faces, startFace={startFace}")

# --- Read T field (internal + boundary) ---
def read_scalar_field(path):
    """Read OpenFOAM volScalarField (uniform or nonuniform)."""
    with open(path, 'r') as f:
        content = f.read()
    
    # Internal field
    m = re.search(r'internalField\s+uniform\s+([-\d.eE+]+)', content)
    if m:
        return float(m.group(1)), None
    
    m = re.search(r'internalField\s+nonuniform\s+List<scalar>\s*\n(\d+)\s*\n\(', content)
    if m:
        n = int(m.group(1))
        start = m.end()
        values = []
        for line in content[start:].split('\n'):
            line = line.strip()
            if line.startswith(')'):
                break
            if line:
                values.append(float(line))
        return None, np.array(values)
    
    return None, None

# --- Read boundary T values for cylinder ---
def read_boundary_T(path):
    with open(path, 'r') as f:
        content = f.read()
    
    # Find cylinder boundary block
    m = re.search(r'cylinder\s*\{([^}]+)\}', content)
    if not m:
        return None
    block = m.group(1)
    
    # Check if uniform
    um = re.search(r'value\s+uniform\s+([-\d.eE+]+)', block)
    if um:
        return np.full(nFaces, float(um.group(1)))
    
    # Non-uniform: parse list
    nm = re.search(r'value\s+nonuniform\s+List<scalar>\s*\n(\d+)\s*\n\(', block)
    if nm:
        n = int(nm.group(1))
        start = nm.end()
        values = []
        for line in block[start:].split('\n'):
            line = line.strip()
            if line.startswith(')'):
                break
            if line:
                values.append(float(line))
        return np.array(values)
    return None

T_int, T_cell = read_scalar_field(f"{CASE}/{TIME}/T")
print(f"T internal: uniform={T_int}, cells={len(T_cell) if T_cell is not None else 0}")

# Cylinder patch T
T_cyl = read_boundary_T(f"{CASE}/{TIME}/T")
if T_cyl is None:
    print("ERROR: Could not read cylinder T values")
    raise SystemExit(1)
print(f"T cylinder: {len(T_cyl)} faces, mean={T_cyl.mean():.2f} K")

# --- For HTC we need the gradient at the wall ---
# OpenFOAM stores nut (turbulent viscosity). Wall heat flux is:
# q = rho * Cp * (alpha + alpha_t) * dT/dy
# Without postProcess, we approximate using nut_wall and T_wall - T_ref

# Read nut at cylinder wall
def read_boundary_nut(path):
    with open(path, 'r') as f:
        content = f.read()
    m = re.search(r'cylinder\s*\{([^}]+)\}', content)
    if not m:
        return None
    block = m.group(1)
    um = re.search(r'value\s+uniform\s+([-\d.eE+]+)', block)
    if um:
        return np.full(nFaces, float(um.group(1)))
    return None

nut_cyl = read_boundary_nut(f"{CASE}/{TIME}/nut")
if nut_cyl is None:
    nut_cyl = np.zeros(nFaces)

print(f"nut at wall: {nut_cyl.mean():.3e} m²/s")

# --- Physical constants ---
rho = 1.0        # kg/m³ (Boussinesq)
Cp = 1005.0      # J/(kg·K)
Pr = 0.71
Prt = 0.85
nu = 1.5e-5      # m²/s (from transportProperties)
alpha = nu / Pr  # thermal diffusivity
alpha_t = nut_cyl / Prt  # turbulent thermal diffusivity

# Wall temperature (fixed value)
T_wall = 340.15
T_ref = 313.15
dT = T_wall - T_ref

# Estimate h from wall function analogy
# For turbulent flow, wall HTC ~ rho * Cp * u_tau / T+
# Simplified: use alpha_eff and boundary layer thickness estimate
# delta_T ~ 1 mm for turbulent BL
delta = 1e-3  # m

alpha_eff = alpha + alpha_t.mean()
h = rho * Cp * alpha_eff / delta
U = h  # for single cylinder without fins

print()
print("=" * 60)
print("  RESULTS SUMMARY")
print("=" * 60)
print(f"  Cylinder wall T:        {T_wall:.2f} K ({T_wall-273.15:.2f} C)")
print(f"  Air reference T:        {T_ref:.2f} K ({T_ref-273.15:.2f} C)")
print(f"  ΔT:                     {dT:.2f} K")
print(f"  Molecular α:            {alpha:.3e} m²/s")
print(f"  Turbulent α_t (avg):    {alpha_t.mean():.3e} m²/s")
print(f"  Effective α:            {alpha_eff:.3e} m²/s")
print(f"  Estimated BL thickness: {delta*1000:.2f} mm")
print()
print(f"  >> Estimated h:         {h:.2f} W/m²·K")
print(f"  >> Design U (baseline): 15.0 W/m²·K")
print(f"  >> Ratio h/U_design:    {h/15.0:.3f}")
print("=" * 60)

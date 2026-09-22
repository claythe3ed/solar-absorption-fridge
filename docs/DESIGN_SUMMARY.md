# Solar Absorption Fridge - Design Summary

## 1. Cycle Specification
- Type: NH3-H2O continuous absorption
- Cooling capacity: 200 W
- Evaporator temperature: -15°C
- Condenser temperature: 40°C
- Generator temperature: 135°C
- Absorber temperature: 30°C
- COP: 0.424
- Solution circulation ratio f: 4.37

## 2. Solar Collector
- Type: CPC (Compound Parabolic Concentrator)
- Receiver: 200 mm OD steel pipe, 4 m long
- Wall thickness: 2.5 mm (SF=4, carbon steel)
- Aperture width: 400 mm
- Aperture area: 1.59 m²
- Acceptance half-angle: 30°
- Concentration ratio: 2.0
- Orientation: East-West horizontal
- Tilt: local latitude (15° for Sudan)

## 3. Heat Exchangers
### Condenser
- Heat load: 274.8 W
- Fin factor: 6x
- Tube: 15 mm OD, 7.5 m total (5 passes × 1.5 m)
- Air-cooled, natural convection
- U = 15 W/m²·K

### Evaporator
- Heat load: 200 W
- Fin factor: 8x
- Tube: 10 mm OD, 6.37 m coil (7 turns at Ø300 mm)
- Inside insulated 150 L cold box
- U = 25 W/m²·K

### Absorber
- Heat load: 396.7 W
- Same vessel as generator (integrated unit)
- Available area: 3.97 m²

## 4. Mass Flows
- Refrigerant: 0.68 kg/h (pure NH3)
- Rich solution: 2.99 kg/h (x_NH3 = 0.40)
- Poor solution: 2.30 kg/h (x_NH3 = 0.25)
- Vapor from generator: y_NH3 = 0.906

## 5. Storage
- Rich solution buffer: 3.0 L
- Poor solution buffer: 2.3 L

## 6. Operating Pressures
- Low side (evap + absorber): 2.36 bar
- High side (gen + condenser): 15.55 bar
- Pressure ratio: 6.58

## 7. Thermodynamic Property Model
- Pure NH3 and H2O: CoolProp 8.0 (NIST-ref)
- Mixture: Ziegler-Trepp 1984 (coefficients cross-validated)
- Bubble/dew point: Patek-Klomfar 1995

## 8. References
- Ziegler & Trepp (1984), Int. J. Refrig. 7(2):101-106
- Patek & Klomfar (1995), Int. J. Refrig. 18(4):228-234
- Herold, Radermacher, Klein, "Absorption Chillers and Heat Pumps"
- Kherris et al. (2013), Thermal Science 17(3):891-902
- Sadhukhan et al., Int. Centre Applied Thermodynamics 15(3)
- Tillner-Roth & Friend (1998), J. Phys. Chem. Ref. Data 27(1):63-96

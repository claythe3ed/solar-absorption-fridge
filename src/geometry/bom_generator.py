"""
Bill of Materials (BOM) for the Solar NH3-H2O Absorption Fridge.
Target: 200 W cooling, 150 L cold box, household-scale.

Currency: USD primary, SDG secondary (rate configurable).
Prices: Indicative, Sep 2026 — expect ±30% local variation.
"""

import csv
import os
import textwrap


# ============================================================
# Exchange rate
# ============================================================
USD_TO_SDG = 600.0  # Update periodically


# ============================================================
# BOM entries
# Format: (category, item, spec, qty, unit, unit_price_usd, notes)
# ============================================================
BOM = [
    # ---------- STEEL PIPES & VESSELS ----------
    ("Steel pipes", "Generator/receiver pipe",
     "Carbon steel ASTM A106 Gr.B, 200 mm OD x 2.5 mm wall x 4 m",
     1, "pc", 180.0, "High-pressure side, design P=16 bar"),

    ("Steel pipes", "Condenser tube",
     "Carbon steel, 15 mm OD x 2 mm wall x 1.5 m",
     5, "pc", 12.0, "5 passes, will need fins welded"),

    ("Steel pipes", "Evaporator tube",
     "Carbon steel, 10 mm OD x 1.5 mm wall x 1.5 m",
     5, "pc", 8.0, "Coiled into 300 mm helix"),

    ("Steel pipes", "Connecting pipes (assorted)",
     "Carbon steel seamless, 8-15 mm OD, various lengths",
     1, "set", 85.0, "Piping per P&ID"),

    ("Steel pipes", "Fittings (elbows, tees, reducers)",
     "Carbon steel, welded, 10-200 mm",
     1, "set", 120.0, "Per P&ID drawing"),

    ("Steel pipes", "End caps for generator",
     "Carbon steel plate, 200 mm dia x 5 mm thick",
     2, "pc", 20.0, "Welded to pipe ends"),

    # ---------- SOLAR COLLECTOR ----------
    ("Solar collector", "CPC mirror (acrylic or aluminum)",
     "Reflective sheet, 400 mm x 4000 mm x 2 mm",
     1, "pc", 95.0, "Acrylic fragile; anodized Al preferred"),

    ("Solar collector", "Solar cover glass",
     "Low-iron tempered, 4 mm x 500 x 4100 mm",
     1, "pc", 60.0, "High transmittance >90%"),

    ("Solar collector", "Selective coating service",
     "Black nickel or black chrome on receiver",
     1, "set", 40.0, "Workshop service"),

    ("Solar collector", "Rock wool insulation",
     "50 mm thick, foil-faced, 100 kg/m^3",
     3, "m^2", 8.0, "Back of mirror + receiver"),

    ("Solar collector", "Reflector frame",
     "Galvanized steel profiles 40x40 mm",
     12, "m", 5.0, "Support structure"),

    ("Solar collector", "Mounting bolts and brackets",
     "Stainless, assorted M8-M12",
     1, "set", 25.0, "—"),

    # ---------- INSULATION & COLD BOX ----------
    ("Insulation", "Cold box cabinet",
     "Stainless 304 or painted steel, 700x700x800 mm",
     1, "pc", 150.0, "Custom fabricated"),

    ("Insulation", "Polyurethane rigid foam",
     "100 mm thick boards",
     3, "m^2", 30.0, "Walls + lid"),

    ("Insulation", "Pipe insulation (Armaflex)",
     "19 mm wall, 15 mm ID",
     5, "m", 8.0, "Low-temp lines"),

    # ---------- VALVES ----------
    ("Valves", "Expansion capillary tube",
     "Stainless, 0.6 mm ID x 1.5 m, coiled",
     1, "pc", 25.0, "Sized for 15.5 -> 2.4 bar"),

    ("Valves", "Throttle needle valve",
     "Stainless, 1/4 NPT",
     1, "pc", 45.0, "Poor solution expansion"),

    ("Valves", "Safety relief valve",
     "Stainless, 25 bar set point, 1/4 NPT",
     2, "pc", 35.0, "On generator + condenser"),

    ("Valves", "Check valve (non-return)",
     "Stainless, 1/4 NPT, 0.2 bar cracking",
     2, "pc", 28.0, "Prevents backflow"),

    ("Valves", "Ball valves (shut-off)",
     "Stainless, 1/4 NPT",
     4, "pc", 18.0, "Isolation"),

    ("Valves", "Schrader charging valve",
     "Stainless, 1/4 SAE",
     1, "pc", 15.0, "Ammonia charging"),

    # ---------- INSTRUMENTS ----------
    ("Instruments", "Pressure gauge",
     "0-25 bar, glycerin-filled, 63 mm dial",
     2, "pc", 30.0, "High + low side"),

    ("Instruments", "Thermocouple Type-K",
     "With digital display meter",
     4, "pc", 12.0, "T_evap, T_cond, T_gen, T_abs"),

    ("Instruments", "Sight glass with moisture indicator",
     "1/4 NPT",
     2, "pc", 22.0, "Liquid line check"),

    # ---------- WORKING FLUIDS ----------
    ("Fluids", "Ammonia (NH3) anhydrous",
     "99.5% purity, agriculture grade",
     2, "kg", 25.0, "1 kg charge + purge cycles"),

    ("Fluids", "Distilled water",
     "Deionized, >1 MOhm*cm",
     5, "L", 3.0, "Solution preparation"),

    ("Fluids", "Nitrogen (N2) cylinder",
     "Dry, 99.99%, for pressure testing",
     1, "rental", 40.0, "Refundable deposit"),

    # ---------- FABRICATION SERVICES ----------
    ("Fabrication", "TIG welding service",
     "Stainless + carbon steel, certified welder",
     1, "lot", 200.0, "~10 hours at $20/h"),

    ("Fabrication", "Pipe bending service",
     "Hydraulic bender for coils",
     1, "lot", 50.0, "Condenser + evaporator"),

    ("Fabrication", "Drilling and threading",
     "Holes, NPT threads, end caps",
     1, "lot", 60.0, "Workshop"),

    ("Fabrication", "Pressure testing",
     "Hydro test at 25 bar + N2 leak test",
     1, "lot", 80.0, "Certified test report"),

    # ---------- CONSUMABLES ----------
    ("Consumables", "Silver brazing rods 5%",
     "1.6 mm x 500 mm, flux-coated",
     20, "pc", 5.0, "Copper-steel joints"),

    ("Consumables", "Thread sealant",
     "Ammonia-compatible, PTFE tape + paste",
     1, "set", 15.0, "For all NPT joints"),

    ("Consumables", "Anti-corrosion epoxy paint",
     "2-component, 1 L",
     1, "can", 20.0, "External surfaces"),

    ("Consumables", "Solvent + cleaning rags",
     "Acetone + lint-free cloths",
     1, "set", 10.0, "Pre-assembly cleaning"),
]


# ============================================================
# Print table
# ============================================================
def print_bom(bom):
    total_usd = 0.0
    print("=" * 110)
    print("  BILL OF MATERIALS - Solar NH3-H2O Absorption Fridge (200 W)")
    print("=" * 110)
    print(f"{'#':>3} {'Category':<16} {'Item':<34} {'Qty':>6} "
          f"{'Unit':<8} {'USD':>8} {'SDG':>10}")
    print("-" * 110)

    for i, (cat, item, spec, qty, unit, price, notes) in enumerate(bom, 1):
        subtotal = qty * price
        sdg = subtotal * USD_TO_SDG
        total_usd += subtotal
        print(f"{i:>3} {cat:<16} {item:<34} {qty:>6.2f} "
              f"{unit:<8} {subtotal:>8.2f} {sdg:>10.0f}")

    print("-" * 110)
    print(f"{'TOTAL':<65} {'USD':>8} {total_usd:>8.2f} "
          f"{total_usd * USD_TO_SDG:>10.0f}")
    print("=" * 110)
    print(f"\nNote: 1 USD ~= {USD_TO_SDG:.0f} SDG (Sep 2026)")
    print(f"Prices indicative; expect +/- 30% local variation.")
    return total_usd


# ============================================================
# Summary by category
# ============================================================
def summary_by_category(bom):
    print("\n" + "=" * 60)
    print("  SUMMARY BY CATEGORY")
    print("=" * 60)
    print(f"{'Category':<22} {'USD':>10} {'SDG':>12} {'%':>7}")
    print("-" * 60)

    cats = {}
    for cat, item, spec, qty, unit, price, notes in bom:
        cats[cat] = cats.get(cat, 0.0) + qty * price

    total = sum(cats.values())
    for cat, sub in sorted(cats.items(), key=lambda x: -x[1]):
        pct = sub / total * 100
        print(f"{cat:<22} {sub:>10.2f} {sub * USD_TO_SDG:>12.0f} "
              f"{pct:>6.1f}%")
    print("-" * 60)
    print(f"{'TOTAL':<22} {total:>10.2f} {total * USD_TO_SDG:>12.0f} "
          f"{100.0:>6.1f}%")
    print("=" * 60)


# ============================================================
# Sudan procurement notes
# ============================================================
def procurement_notes():
    print("\n" + "=" * 70)
    print("  PROCUREMENT NOTES FOR SUDAN")
    print("=" * 70)

    notes = [
        ("Steel pipes (200 mm OD)",
         "Khartoum Bahri Industrial Area or Port Sudan. Order seamless "
         "ASTM A106 Gr.B. Lead time ~1 week."),
        ("Steel tubes (10-15 mm)",
         "Common hydraulic tubing (EN 10305-4). Available in Omdurman "
         "Souq and Khartoum industrial markets."),
        ("CPC mirror",
         "Local suppliers: Khartoum Bahri. Alternative: polished stainless "
         "steel sheet 1 mm (lower reflectivity ~0.6 vs 0.85)."),
        ("Cover glass",
         "Import from Egypt or UAE. Alternative: standard window glass "
         "(slightly lower transmittance)."),
        ("Ammonia (NH3)",
         "Agricultural fertilizer suppliers or industrial gas companies "
         "in Khartoum. Request 99.5% purity certificate."),
        ("Nitrogen cylinder",
         "Industrial gas suppliers. Rental ~50 USD/month with deposit."),
        ("TIG welding",
         "Many workshops in Khartoum industrial area. Rate: 20-30 USD/hour. "
         "Project ~8-10 hours."),
        ("Expansion valve / capillary",
         "Import from UAE (Dubai). Or fabricate a precision capillary from "
         "0.6 mm ID stainless steel."),
        ("Safety valves",
         "CRITICAL - Do NOT compromise. Import genuine parts."),
        ("Pressure test",
         "Required. Any certified workshop can perform 25 bar hydro test."),
    ]

    for item, note in notes:
        print(f"\n  >> {item}")
        for line in textwrap.wrap(note, width=68):
            print(f"      {line}")

    print("=" * 70)


# ============================================================
# Export to CSV
# ============================================================
def export_csv(bom, path):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['#', 'Category', 'Item', 'Specification',
                    'Quantity', 'Unit', 'Unit Price (USD)',
                    'Subtotal (USD)', 'Subtotal (SDG)', 'Notes'])
        for i, (cat, item, spec, qty, unit, price, notes) in enumerate(bom, 1):
            sub_usd = qty * price
            sub_sdg = sub_usd * USD_TO_SDG
            w.writerow([i, cat, item, spec, qty, unit,
                        f"{price:.2f}", f"{sub_usd:.2f}",
                        f"{sub_sdg:.0f}", notes])
    print(f"\nCSV exported: {path}")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    out_dir = "/root/fridge/results"
    os.makedirs(out_dir, exist_ok=True)
    csv_path = os.path.join(out_dir, "bom.csv")

    total = print_bom(BOM)
    summary_by_category(BOM)
    procurement_notes()
    export_csv(BOM, csv_path)

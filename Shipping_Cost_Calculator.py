# Shipping Cost Calculator — Ton-Kilometer Model

import math

# Global Constants
DIM_DIVISOR = 6000          # cm³ per kg
STEP_KG = 0.5               # round billable weight up to nearest 0.5
BASE_FEE = 5.00             # flat base fee
RATE_PER_KG_PER_KM = 0.002  # main rate
MIN_CHARGE = 8.00           # minimum charge before fuel
FUEL_PERCENTAGE = 0.15      # 15% fuel surcharge

# Input and Validation
while True:
    try:
        weight = float(input("Enter weight (g): "))
        if weight <= 0:
            print("Weight must be positive.")
            continue

        length = float(input("Enter length (cm): "))
        if length <= 0:
            print("Length must be positive.")
            continue

        width = float(input("Enter width (cm): "))
        if width <= 0:
            print("Width must be positive.")
            continue

        height = float(input("Enter height (cm): "))
        if height <= 0:
            print("Height must be positive.")
            continue

        distance = float(input("Enter distance (km): "))
        if distance <= 0:
            print("Distance must be positive.")
            continue

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
    break

# Normalize weight
weight_kg = weight / 1000

# Dimensional Weight
dimensional_weight = (length * width * height) / DIM_DIVISOR

# Billable Weight
billable_weight = max(weight_kg, dimensional_weight)
billable_kg = math.ceil(billable_weight / STEP_KG) * STEP_KG

# Transportation Cost
transport_pre_min = BASE_FEE + (billable_kg * distance * RATE_PER_KG_PER_KM)
transport = max(transport_pre_min, MIN_CHARGE)

# Fuel Surcharge
fuel_surcharge = transport * FUEL_PERCENTAGE

# Total
total = round(transport + fuel_surcharge, 2)

# Output
print("\n--- Shipping Cost Breakdown ---")
print(f"Billable Weight (kg): {billable_kg:.2f}")
print(f"Transportation (after min ${MIN_CHARGE:.2f}): ${transport:.2f}")
print(f"Fuel Surcharge ({FUEL_PERCENTAGE*100:.0f}%): ${fuel_surcharge:.2f}")
print(f"Total Shipping Cost: ${total:.2f}")

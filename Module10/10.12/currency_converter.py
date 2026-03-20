# ============================================================
# 3. Create the main script currency_converter.py that imports the exchange_rates module.
# ============================================================

import exchange_rates


# ============================================================
# 4. Define functions to convert currency using exchange rates from the module.
# ============================================================

def convert_usd_to_eur(amount):
    # Demonstrates scope: accessing module-level variable
    rate = exchange_rates.USD_TO_EUR
    return amount * rate

def convert_usd_to_gbp(amount):
    rate = exchange_rates.USD_TO_GBP
    return amount * rate

def convert_usd_to_jpy(amount):
    rate = exchange_rates.USD_TO_JPY
    return amount * rate


# ============================================================
# 5. Demonstrate scope by accessing module variables inside functions.
#    Use main() as the entry point.
# ============================================================

def main():
    usd_amount = 100  # Local variable inside main()

    print("\n========== CURRENCY CONVERTER ==========\n")
    print(f"USD Amount: {usd_amount}")

    print(f"USD → EUR: {convert_usd_to_eur(usd_amount):.2f}")
    print(f"USD → GBP: {convert_usd_to_gbp(usd_amount):.2f}")
    print(f"USD → JPY: {convert_usd_to_jpy(usd_amount):.2f}")


# Only runs when executed directly
if __name__ == "__main__":
    main()

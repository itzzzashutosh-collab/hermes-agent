if __name__ == '__main__':
    # Test case for Swatch Paints
    # Based on typical financials for a medium-sized paint manufacturer in Rajasthan
    test_inputs = {
        'net_income': 12500000,  # ₹1.25 crore
        'depreciation_amortization': 2800000,  # ₹28 lakh
        'working_capital_change': 1500000,  # ₹15 lakh increase in working capital
        'maintenance_capex': 1800000,  # ₹18 lakh
        'current_liabilities': 8500000,  # ₹85 lakh
        'current_assets': 11200000  # ₹1.12 crore
    }

    try:
        result = calculate_working_capital_float(**test_inputs)
        print("\n=== Swatch Paints - Warren Buffett Cash Flow Analysis ===")
        print(f"Net Income: ₹{test_inputs['net_income']:,.2f}")
        print(f"Depreciation & Amortization: ₹{test_inputs['depreciation_amortization']:,.2f}")
        print(f"Working Capital Change: ₹{test_inputs['working_capital_change']:,.2f}")
        print(f"Maintenance Capex: ₹{test_inputs['maintenance_capex']:,.2f}")
        print(f"Current Assets: ₹{test_inputs['current_assets']:,.2f}")
        print(f"Current Liabilities: ₹{test_inputs['current_liabilities']:,.2f}")
        print(f"\nResults:")
        print(f"Owner Earnings: ₹{result['owner_earnings']:,.2f}")
        print(f"Working Capital: ₹{result['working_capital']:,.2f}")
        print(f"Float: ₹{result['float']:+,.2f}")
        print(f"\nAnalysis:")
        if result['owner_earnings'] > 0:
            print("✅ Strong cash-generating business")
        else:
            print("❌ Weak cash-generating business")
        print(f"\nFloat (Liabilities - Assets): ₹{result['float']:+,.2f}")
        print(f"Negative float indicates positive working capital; positive float indicates negative working capital.")
    except Exception as e:
        print(f"Error during calculation: {e}")

    # Additional test case: edge case with zero inputs
    print("\n\n=== Edge Case Test: Zero Inputs ===")
    try:
        zero_inputs = {k: 0 for k in ['net_income', 'depreciation_amortization', 'working_capital_change', 'maintenance_capex', 'current_liabilities', 'current_assets']}
        result_zero = calculate_working_capital_float(**zero_inputs)
        print(f"Zero inputs test passed. Results: {result_zero}")
    except Exception as e:
        print(f"Zero inputs test failed: {e}")
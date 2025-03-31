def sensitivity_analysis(free_cash_flows, discount_rates):
    results = {}
    for rate in discount_rates:
        npv = sum([fcf / (1 + rate) ** i for i, fcf in enumerate(free_cash_flows, 1)])
        results[rate] = npv
    return results


# Example free cash flows (in millions) and discount rates
free_cash_flows = [10, 15, 20, 25, 30]
discount_rates = [0.06, 0.08, 0.10]

results = sensitivity_analysis(free_cash_flows, discount_rates)
for rate, npv in results.items():
    print(f"NPV at {rate * 100:.2f}% discount rate: ${npv:.2f} million")



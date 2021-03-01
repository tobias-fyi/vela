"""Simple script to estimate self-employment taxes on a given amount of income."""

# %%
def tax_calc(gross_income, business_expenses):
    net_income = gross_income - business_expenses
    # Self-employment tax calculation
    # self_emp_tax = (net_income * .9235) * .153
    line_3 = net_income * 0.9235
    line_4 = line_3 * 0.029
    line_9 = line_3 * 0.124
    self_emp_tax = line_4 + line_9  # line_10

    # Income tax calculation
    # Deductible portion of self employment tax
    self_emp_tax_ded = self_emp_tax * 0.5
    # Adjusted gross income
    agi = net_income - self_emp_tax_ded
    std_deduction = 12400
    personal_exemption = 3900
    taxable_income = agi - std_deduction - personal_exemption


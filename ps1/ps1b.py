
portion_down_payment = .25
r = .04
current_savings = 0
annual_salary = float(input('what is your annual salary? '))
portion_saved = float(input('what portion of your salary will you save? '))
total_cost = float(input('how much does your dream house cost? '))
semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal '))

months = 0

while current_savings < total_cost * portion_down_payment:
    months = months + 1
    if months % 6 == 0:
        annual_salary = annual_salary * (1+semi_annual_raise)

    current_savings = current_savings + current_savings * \
        r / 12 + annual_salary / 12 * portion_saved

print('Number of Months:' + str(months))

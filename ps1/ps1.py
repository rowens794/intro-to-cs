
portion_down_payment = .25
r = .04
annual_salary = float(input('what is your annual salary? '))
portion_saved = float(input('what portion of your salary will you save? '))
total_cost = float(input('how much does your dream house cost? '))
current_savings = 0

months = 0

print('pre loop')
print(current_savings)
print(total_cost * portion_down_payment)

while current_savings < total_cost * portion_down_payment:
    months = months + 1
    current_savings = current_savings + current_savings * \
        r / 12 + annual_salary / 12 * portion_saved
    print('in loop')
    print(current_savings)

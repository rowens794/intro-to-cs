current_savings = 0
annual_salary = float(input('what is your annual salary? '))
months = 36
semi_annual_raise = .07
r = .04
portion_down_payment = .25
total_cost = 1000000
current_savings_rate = 0
max_error = 100
current_error = 10000
down_payment = portion_down_payment * total_cost
step = 0
rate_list = list(range(1, 10001))
salary_too_low = False


def calc_savings(salary, savings_rate, semi_annual_raise, r):
    savings_rate = float(savings_rate / 10000)
    savings = 0
    new_salary = salary

    for x in range(0, 36):
        if x % 6 == 0 and x > 0:
            new_salary = new_salary * (1 + semi_annual_raise)

        savings = savings * (1+r/12) + new_salary/12 * savings_rate

    return savings


while abs(current_error) > max_error and not(salary_too_low):
    # set initial loop variables
    step += 1
    middle_element = int(len(rate_list) / 2)
    current_savings_rate = rate_list[middle_element]
    current_savings = calc_savings(
        annual_salary, current_savings_rate, semi_annual_raise, r)
    current_error = current_savings - down_payment

    if(current_savings_rate == 10000):
        print('It is not possible to pay the down payment in three years.')
        salary_too_low = True

    if abs(current_error) < max_error:
        print('Best savings rate:' + str(current_savings_rate/10000))
        print('Steps in bisection search:' + str(step))

    elif current_error > 0:
        # then the savings rate is too high and we need to eliminate the top half of the list
        mid_point = int(len(rate_list) / 2)
        rate_list = rate_list[0:mid_point]

    elif current_error < 0:
        # then the savings rate is too low and we need to eliminate the bottom half of the list
        mid_point = int(len(rate_list) / 2)
        end_point = int(len(rate_list))
        rate_list = rate_list[mid_point:end_point]

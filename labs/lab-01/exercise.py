def determine_scholarship(cgpa, tuition_fee):
    if 3.8 <= cgpa <= 4.0:
        waiver_percentage = 1
        print("Eligible for 100% scholarship.")
    elif 3.5 <= cgpa < 3.8:
        waiver_percentage = 0.5
        print("Eligible for 50% scholarship.")
    elif 3.0 <= cgpa < 3.5:
        waiver_percentage = 0.25
        print("Eligible for 25% scholarship.")
    else:
        waiver_percentage = 0
        print("Not eligible for a scholarship.")

    waived_amount = tuition_fee * waiver_percentage 
    amount_paid = tuition_fee - waived_amount

    return amount_paid

result = determine_scholarship(3.6, 10000)
print(f"Amount to be paid after scholarship: ${result:.2f}")



#code C

def calculate_cost(item_price,quantity):
    total_cost = item_price * quantity
    if total_cost > 100:
        discount = total_cost * 0.1
    return total_cost

price1 = calculate_cost(50,3)
price2 = calculate_cost(120,1)

grand_total = price1 + price2

print("price 1:", price1)
print("price 2:", price2)
print("Grand total:", grand_total)



#code D

def calculate_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temp1 = calculate_celsius(100)
temp2 = calculate_celsius(212)
temp3 = calculate_celsius(32)

print("Temperature 1 in Celsius:", temp1)
print("Temperature 2 in Celsius:", temp2)
print("Temperature 3 in Celsius:", temp3)


#code E

def calculate_profit(money_invested, yearly_rate, years_waited):
    total_profit = money_invested * yearly_rate * years_waited
    return total_profit

profit1 = calculate_profit(1000, 0.05, 3)
profit2 = calculate_profit(5000, 0.04, 5)

print("Profit 1:", profit1)
print("Profit 2:", profit2)


#code F

def calculate_cost(height, width,):
    area = height * width
    paint_needed = area / 350
    cost = paint_needed * 45
    return cost

cost1 = calculate_cost(10,12)
cost2 = calculate_cost(15,20)

print("Cost 1:", cost1)
print("Cost 2:", cost2)

#code G

def calculate_payslip(base_pay,overtime_hours,ot_rate):
    overtime_pay = overtime_hours * ot_rate
    grooss_pay = base_pay + overtime_pay
    tax = grooss_pay * 0.11
    net_pay = grooss_pay - tax
    return net_pay

def print_payslip(emp_name, base_pay, ot_pay, tax, overtime_hours, ot_rate):
    print("--- PAYSLIP ---")
    print(f"Name: {emp_name}")
    print(f"Base: RM{base_pay}")
    print(f"Overtime: RM{ot_pay}")
    print(f"Tax: RM{tax}")
    print(f"Net Pay: RM{calculate_payslip(base_pay, overtime_hours, ot_rate)}")
    print("----------------")

print_payslip("Ali", 2000, 50, 0.1, 10, 15)

#scenario 12

def calculate_discounted_price(quantity, discount_rate):
    if quantity > 10:
        discount_rate = 0.15
    elif quantity > 50:
        discount_rate = 0.25
    else:
        discount_rate = 0
    return discount_rate

def is_stock_avalilable(stock, requested_quantity):
    if stock >= requested_quantity:
        return True
    else:
        return False
    
def calculate_total_price(price, quantity, available_stock):
    if is_stock_avalilable(available_stock, quantity):
        discount_rate = calculate_discounted_price(quantity, 0)
        total_price = price * quantity * (1 - discount_rate)
        return total_price
    else:
        return "Insufficient stock"
    
#scenario 11

def calculate_average_scores(scores):
    total_score = sum(scores)
    average_score = total_score / len(scores)
    return average_score

def determine_grade(average_score):
    if average_score >= 80:
        return 'A'
    elif average_score >= 60:
        return 'B'
    else:
        return 'C'
    
def print_student_report(name, scores):
    average_score = calculate_average_scores(scores)
    grade = determine_grade(average_score)
    print(f"Student Name: {name}")
    print(f"Scores: {scores}")
    print(f"Average Score: {average_score}")
    print(f"Grade: {grade}")

print_student_report("Ahmad", [75, 82, 68])
    
#scenario 2

scores = [78, 82, 79, 81, 90]
def has_distinction(scores):
    for score in scores:
        if score < 80:
            return False
    return True

print("Has Distinction:", has_distinction(scores))

# scenario 2

team_a = [3,2,1,4,2]
team_b = [2,2,3,1,2]
def compare_teams(team_a, team_b):
    win = 0
    loss = 0
    draw = 0
    while len(team_a) > 0 and len(team_b) > 0:
        score_a = team_a.pop(0)
        score_b = team_b.pop(0)
        if score_a > score_b:
            win += 1
        elif score_a < score_b:
            loss += 1
        else:
            draw += 1
    return [win, loss, draw]

result = compare_teams(team_a, team_b)
print(result)
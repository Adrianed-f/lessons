deposit = int(2130)

interest_rate = float(0.1)

bonus = int(120)

first_year = deposit + deposit * interest_rate + bonus

print("первый год:", first_year)

second_year = first_year + first_year * interest_rate + bonus

print("второй год:", second_year)

third_year = second_year + second_year * interest_rate + bonus

print("третий год:", third_year)

fourth_year = third_year + third_year * interest_rate + bonus

print("четвёртый год:", fourth_year)

fifth_year = fourth_year + fourth_year * interest_rate + bonus

print("пятый год:", fifth_year)

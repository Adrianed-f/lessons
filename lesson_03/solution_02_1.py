deposit = int(2130)

period = int(5)

interest_rate = float(0.1)

bonus = int(120)

i = int(0)

while i < period:
   deposit = deposit + deposit * interest_rate + bonus 
   print(i+1, "год:", deposit)
   i += 1

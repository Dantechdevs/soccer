#player payment based on manager creteria

def weeklyPaid(hours_worked, wage):
	if hours_worked < 30:
		return 30 * wage + (hours_worked - 30) * wage * 1.5
	else:
		return hours_worked * wage


hours_worked = 60
wage = 1000

pay = weeklyPaid(hours_worked, wage)
print("overall Rate = simmulation of skills rate*100/30")
print(f"Total gross pay: Rs.{pay:.2f} ")

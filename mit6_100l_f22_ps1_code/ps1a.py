## 6.100A PSet 1: Part A
## Name: dracotato
## Time Spent: ~1 hour (unsure)
## Collaborators: N/A

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
amount_saved = 0
portion_down_payment = 0.25
r = 0.05
down_payment = cost_of_dream_home * portion_down_payment
months = 0


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################
while amount_saved < down_payment:
    amount_saved += amount_saved * (r / 12)
    amount_saved += (yearly_salary / 12) * portion_saved

    months += 1

print(f"Months: {months}")

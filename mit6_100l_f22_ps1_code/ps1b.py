## 6.100A PSet 1: Part B
## Name: dracotato
## Time Spent: ~30 minutes (unsure)
## Collaborators: N/A

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual raise, as a decimal: "))


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

    if months % 6 == 0:
        yearly_salary += yearly_salary * semi_annual_raise

print(f"Months: {months}")

## 6.100A PSet 1: Part C
## Name: dracotato
## Time Spent: ~30 minutes (unsure)
## Collaborators: N/A

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_dream_home = 800_000
down_payment = cost_of_dream_home * 0.25


def calc_amount_saved(r: float):
    return initial_deposit * (1 + r / 12) ** 36


r = 0.5
amount_saved = calc_amount_saved(r)


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
steps = 1

if initial_deposit > (down_payment - 100):
    r = 0
elif calc_amount_saved(1) < down_payment - 100:
    r = None
else:
    lower_limit = 0
    upper_limit = 1

    while True:
        if amount_saved > (down_payment - 100) and amount_saved < (down_payment + 100):
            break

        steps += 1

        if amount_saved < down_payment - 100:
            lower_limit = r
        elif amount_saved > down_payment + 100:
            upper_limit = r

        r = (lower_limit + upper_limit) / 2

        amount_saved = calc_amount_saved(r)

print(f"Best savings rate: {r} [or very close]")
print(f"Steps in bisection search: {steps}")

# Write your solution here!
# 
import math

def optimal_change(item_cost, amount_paid):

    denomination = [100, 50, 20, 10, 5, 1, .25, .1, .05, .01]

    change = float(amount_paid - item_cost)

    output = f'The optimal change for this item is ${item_cost} with an amount paid of {amount_paid} is '

    if amount_paid == item_cost:
        return ("No Change.")

    if amount_paid < item_cost:
        return("You dont have enough money for this purchase.")

    if change > 0:
        for x in range(len(denomination)):
            amount = math.floor(change // denomination[x])

            if amount > 1:
                if x >= 6 and amount > 0:
                    output += f' , {amount} ${denomination[x]} cents'
                    change -= (amount * denomination[x])
                    continue
                elif amount > 0:
                    output += f', {amount} ${denomination[x]} bills'
                    change -=(amount * denomination[x])

            elif amount > 0:
                if x >= 6 and amount > 0:
                    output += f' {amount} ${denomination[x]} cent'
                    change -= (amount * denomination[x])
                    continue
                elif amount > 0:
                    output += f' {amount} ${denomination[x]} bill'
                    change -= (amount * denomination[x])

        return output + '.'

    print(optimal_change(66.66, 80))
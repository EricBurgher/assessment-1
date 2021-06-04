# Write your solution here!
# 
def optimal_change(item_cost, amount_paid):

    denomination = [100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
    denomination_names = ['$100 bill', '$50 bill', '$20 bill', '$10 bill', '$5 bill', '$1 bill', 'quarter', 'dime', 'nickel', 'penny']

    change = 0
    for x in denomination:
        while item_cost >= denomination:
            item_cost = item_cost - denomination
            change = change + 1

    optimal_change(66.66, 80)

    print("The optimal change for an item that costs " + (item_cost) + "with an amount paid of " + (amount_paid) + "is " + (change))
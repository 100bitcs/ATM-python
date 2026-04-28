from data import money

def withdraw(your_id):
    now_money = money[your_id]
    withdraw_amount = int (input('enter amount for withdraw:  '))
    if now_money > withdraw_amount:
        updated_money = now_money - withdraw_amount
        money[your_id] = updated_money
    else :
        print ('Insufficient Balance')
        withdraw(your_id)
    print ("-"*40)
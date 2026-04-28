from data import money

def add_money(your_id):
    amount =  int(input('enter amount for add :  '))
    org_amount= money[your_id]

    money[your_id] = amount + org_amount
    print ("-"*40)
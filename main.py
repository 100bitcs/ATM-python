from login import login
from create_id import create_id
from check_balence import check_balence
from add_money import add_money
from withdraw_money import withdraw

login_bool = False


while True:
    print ('1.  creating id')
    print ('2.  login')
    print ('3.  Cancel')
    a = int (input ('enter your choice : '))
    if a == 1 :
        create_id()
    if a == 2 :
        your_id = int(input('enter your id :  '))
        login(your_id)
        login_bool= True
    if a == 3:
        break


    # while True:
    while login_bool == True:
        print ('1.  check balence')
        print ('2.  add money')
        print ('3.  withdraw money')
        print ('4.  Cancel')
        choice = int (input ('enter your choice :  '))
            
        #~ function call by choice 
        if choice == 1 :  check_balence(your_id)
        if choice == 2 : add_money(your_id)
        if choice == 3 : withdraw(your_id) 
        if choice == 4 : break
            



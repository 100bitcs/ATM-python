from data import id 

def login(your_id):
    your_pass = input('enter your password : ')
    org_pass = id[your_id]
    if your_pass == org_pass:
        print ('you are sucessfully login  ')
    else: 
        print ('please enter valid id password\n')
        login(your_id)
    print ("-"*40)

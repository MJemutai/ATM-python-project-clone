from utilities import collect_user_input, login_user,withdraw
import pprint
from getpass import getpass
from sys import exit

#DATE AND TIME PROGRAM
from datetime import datetime
now = datetime.now()
today = (now.strftime("%Y-%m-%d %H:%M:%S"))


logged_in = False
logged_in_user_details = None
times_withdrawn = 0
withdraw_again = False


# welcome statement
print('Welcome to Lambda Investment Bank')

# user login functionality
user_input = collect_user_input()

if user_input is None:
    # we do not need to log them in when wrong username is entered
    print(
'''
        Sorry we did not find an account with the given credentials. 
        Please visit your nearest branch to open an account.
'''
)

else:
    # we have a username and a pin
    user = login_user(user_input['username'], user_input['pin'])

    # check if the pin is correct
    if (user['error'] == 'Wrong password!'):
        print('You entered the wrong pin...')
        # tell the user to enter the correct pin
        retries_limit = 2
        tries = 0

        while tries < retries_limit:
            # ask them to enter their credentials again, two more tries to get the pin right
            pin = getpass('Enter your pin: ')
            res = login_user(user_input['username'], pin)

            if (res['error'] == 'Wrong password!'):
                print('You entered the wrong pin...')
                
                tries += 1

                if (retries_limit - tries) == 1 :
                    print('You only have one more chance...')

                if tries == retries_limit:
                    print('Please visit your nearest branch to reset your pin... Or try again in 24 Hours')
                    exit()
                    
                  
                
            else:
                # if they entered correct credentials
                print('Succesful login')
                logged_in = True
                logged_in_user_details = user['details']
                
                break
                
    else: #correct pin at first try
        print("Succesful login")
        logged_in = True
        logged_in_user_details = user['details']
    
    
    

# withdraw money or check balance
    print('Enter W to Withdraw or C to Check Balance')
    withdraw_or_check_balance = input('Do you want to withdraw some money or check your balance? (W/C) >>> ')
    
    transaction_attempt = withdraw(withdraw_or_check_balance, logged_in_user_details,today,times_withdrawn)
    logged_in_user_details = transaction_attempt['user_details']

    # transact = withdraw(logged_in_user_details,today,times_withdrawn)  ##
    

    if transaction_attempt['wc_invalid_input'] ==True:
        w_and_c_tries_limit = 2
        w_and_c_tries = 0
        
        while w_and_c_tries < w_and_c_tries_limit:
            print('Invalid input please enter W to Withdraw and C to Check Balance') 
            withdraw_or_check_balance = input('Do you want to withdraw some money or check your balance? (W/C) >>> ')

            withdraw(withdraw_or_check_balance, logged_in_user_details,today,times_withdrawn)

            w_and_c_tries += 1
            
            if w_and_c_tries == w_and_c_tries_limit:
                print("You have exhausted your attempts. Try again in 24 hours.")
                break

    if transaction_attempt['yn_invalid_input'] ==True: ###
        y_and_n_tries_limit = 2
        y_and_n_tries = 0
        
        while y_and_n_tries < y_and_n_tries_limit:
             
            feedback = input('Try again. Enter Y for Yes or N for No (Y/N) >>> ')

            withdraw(feedback, logged_in_user_details,today,times_withdrawn)

            y_and_n_tries += 1
            
            if y_and_n_tries == y_and_n_tries_limit:
                print("You have exhausted your attempts. Try again in 24 hours.")
                break


        
    
 
from utilities import collect_user_input, login_user
import pprint
from getpass import getpass
from sys import exit

#DATE AND TIME
from datetime import datetime
now = datetime.now()
today = (now.strftime("%Y-%m-%d %H:%M:%S"))
# print(today)

logged_in = False
logged_in_user_details = None
times_withdrawn = 0
withdraw_again = False


# welcome statement
print('Welcome to Lambda Investment Bank')

# user login functionality
user_input = collect_user_input()

if user_input is None:
    # we do not need to log them in
    print(
'''
        Sorry we did not find an account with the given credentials. 
        Please visit a nearby branch to open an account.
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
            # ask them to enter their credentials again
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
                pprint.pprint(logged_in_user_details)
                break
                
    else:
        print("Succesful login")
        logged_in = True
        logged_in_user_details = user['details']
    #receipt
    def receipt_w():
        slip = input("Enter Y for a receipt and N for no receipt: ")
        if (slip.upper() == 'Y'):
            print(f"""
            LAMBDA INVESTMENT BANK             {today}
              TRANSACTION TYPE: CHECK BALANCE
                BALANCE: Ksh.{logged_in_user_details['balance']}
            
                    THANK YOU""") #to edit
            print("Thank you for banking with us. Have a good Day 😊")
        elif (slip.upper() == 'N'):
            print('Thank you for banking with us. Have a good Day 😊')
        else:
            print("Invalid input0.") 

    def receipt_c():
        slip = input("Enter Y for a receipt and N for no receipt: ")
        if (slip.upper() == 'Y'):
            print(f"""
        LAMBDA INVESTMENT BANK             {today}
          TRANSACTION TYPE: CHECK BALANCE
            BALANCE: Ksh.{logged_in_user_details['balance']}
            
                THANK YOU""") #to edit
            print("Thank you for banking with us. Have a good Day 😊")
        elif (slip.upper() == 'N'):
            print('Thank you for banking with us. Have a good Day 😊')
        else:
            print("Invalid input1.") 

    def receipt_cw():
        slip = input("Enter Y for a receipt and N for no receipt: ")
        if (slip.upper() == 'Y'):
            print(f"""
            LAMBDA INVESTMENT BANK           {today}
                TRANSACTION TYPE: BALANCE CHECK AND WITHDRAWAL 
                    BALANCE: Ksh.{logged_in_user_details['balance']}
                      
                        THANK YOU""") #to edit
            print("Thank you for banking with us. Have a good Day 😊")
        elif (slip.upper() == 'N'):
            print('Thank you for banking with us. Have a good Day 😊')
        else:
            print("Invalid input2.") 

        # check balance
    def check_balance():
        try:
            print(f"Your current balance is Ksh {logged_in_user_details['balance']}")

        except:
            print('Something went wrong...')

        # withdraw money
    def withdraw_money(amount_to_withdraw, current_balance):
        remainder = current_balance - amount_to_withdraw

        if remainder < 0:
            print (
                f'''
                     You do not have sufficient balance to continue with this transaction...
                     Your current balance is Ksh {current_balance}
                    '''
                )
        else:
            logged_in_user_details['balance'] = remainder
            print(f'Successfully withdrawn Ksh {amount_to_withdraw}. Your balance is now Ksh {remainder}')




    print('Enter W to Withdraw and C to Check Balance')
    withdraw_or_check_balance = input('Do you want to withdraw some money or check your balance? (W/C) >>> ')

    if withdraw_or_check_balance.upper() == 'W':
            # withdraw some money
        how_much = int(input('How much? >>> '))
        withdraw_money(how_much, logged_in_user_details['balance'])
        times_withdrawn += 1

        x = input('Withdraw again? (Y/N) >>> ')

        if (x.upper() == 'Y'):
            withdraw_again = True
        elif (x.upper() == 'N'):
            withdraw_again = False
            receipt_w() #added
            # print('Thank you for banking with us. Have a good Day 😊') #added
        else:
            withdraw_again = False
                # TODO: Handle It in another Way


        if times_withdrawn < 2 and withdraw_again == True:
                how_much = int(input('How much more? >>> '))
                withdraw_money(how_much, logged_in_user_details['balance'])
                receipt_w()


    elif withdraw_or_check_balance.upper() == 'C':
            # show them the balance
        check_balance()

        response = input('Do you want to withdraw some money? (Y/N) >>> ')
        if response.upper() == 'Y':
                # withdraw some money
            how_much = int(input('How much? >>> '))
            withdraw_money(how_much, logged_in_user_details['balance'])
            times_withdrawn += 1

            x = input('Withdraw again? (Y/N) >>> ')

            if (x.upper() == 'Y'):
                withdraw_again = True
            elif (x.upper() == 'N'):
                withdraw_again = False
                receipt_cw()
                # print('Thank you for banking with us. Have a good Day 😊') #added
            else:
                withdraw_again = False
                # TODO: Handle It in another Way

            if times_withdrawn < 2 and withdraw_again == True:
                how_much = int(input('How much more? >>> '))
                withdraw_money(how_much, logged_in_user_details['balance'])
                receipt_cw()

        elif response.upper() == 'N':
            receipt_c()
            # print('Thank you for banking with us. Have a good Day 😊') ###edited

        else:
            print('Invalid input3')
            print("Try again")###
    else:
        # while withdraw_or_check_balance != 'W' and withdraw_or_check_balance != 'C' :
            # Invalid input
            # TODO: Handle It in another Way

        print(f'Invalid input4..Please try again using W for Withdraw or C for Check balance {withdraw_or_check_balance}')
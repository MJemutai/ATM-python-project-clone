from getpass import getpass
from pprint import pprint
from users import users_data
from pprint import pprint


# collect input on whether a user 
# def x():



# collect the username, pin
def collect_user_input():
    user_input = {
        'username': None,
        'pin': None
    }

    username = input('What is your username? >>> ')

    for user in users_data:
        cleaned_username = username.capitalize()

        if cleaned_username == user['username']:
            print(f'Welcome back {cleaned_username}!')
            pin = getpass('Enter your pin: ')
            
            user_input['username'] = cleaned_username
            user_input['pin'] = pin
            return user_input

    print('User not found...')
    return None


# check if the username and pin are correct according to our database
def login_user(username, pin):
    """
    This func takes in a username and a pin and returns userdata if credentials
    are correct. If the credentials are wrong, the return obj will have user set to None
    and wrong_pin set to True
    """

    temp = {
        'details': None,
        'error': None
    }

    for user in users_data:
        if user['username'] == username:
            # login check password
            if pin == user['pin']:
                temp['details'] = {
                    'username': user['username'],
                    'balance': user['balance']
                }
                return temp
            else:
                temp['error'] = 'Wrong password!'
                return temp

    return None


def withdraw_money(amount_to_withdraw,user_details):
        remainder = user_details['balance'] - amount_to_withdraw
        
        if remainder < 0:
            print (
                f'''
                     You do not have sufficient balance to continue with this transaction...
                     Your current balance is Ksh {user_details['balance']}
                    '''
                )
            return user_details['balance']
        else:
            # logged_in_user_details['balance'] = remainder 
            print(f'Successfully withdrawn Ksh {amount_to_withdraw}. Your balance is now Ksh {remainder}')
            return remainder

#RECEIPTS FUNCTIONS
def receipt_w(date, user_details):
    res = {'receipt_error': False}
    slip = input("Enter Y for a receipt and N for no receipt: ")
    if (slip.upper() == 'Y'):
        print(f"""
        LAMBDA INVESTMENT BANK             {date}
            TRANSACTION TYPE: WITHDRAWAL
            BALANCE: Ksh.{user_details['balance']}
        
                THANK YOU""") 
        print("Thank you for banking with us. Have a good Day 😊")
    elif (slip.upper() == 'N'):
        print('Thank you for banking with us. Have a good Day 😊')
    else:
        print("Invalid input.") 
        res['receipt_error'] = True 
    return res

def receipt_c(date, user_details):
    res = {'receipt_error': False}
    slip = input("Enter Y for a receipt and N for no receipt: ")
    if (slip.upper() == 'Y'):
        print(f"""
    LAMBDA INVESTMENT BANK             {date}
        TRANSACTION TYPE: BALANCE CHECK
        BALANCE: Ksh.{user_details['balance']}
        
            THANK YOU""") 
        print("Thank you for banking with us. Have a good Day 😊")
    elif (slip.upper() == 'N'):
        print('Thank you for banking with us. Have a good Day 😊')
    else:
        print("Invalid input.") 
        res['receipt_error'] = True 
    return res

def receipt_cw(date, user_details):
    res = {'receipt_error': False}
    slip = input("Enter Y for a receipt and N for no receipt: ")
    if (slip.upper() == 'Y'):
        print(f"""
        LAMBDA INVESTMENT BANK           {date}
            TRANSACTION TYPE: BALANCE CHECK AND WITHDRAWAL 
                BALANCE: Ksh.{user_details['balance']}
                    
                    THANK YOU""") 
        print("Thank you for banking with us. Have a good Day 😊")
    elif (slip.upper() == 'N'):
        print('Thank you for banking with us. Have a good Day 😊')
    else:
        print("Invalid input.") 
        res['receipt_error'] = True 
    return res



def check_balance(user_details):
        try:
            print(f"Your current balance is Ksh {user_details['balance']}")

        except:
            print('Something went wrong...')

#WITHDRAWAL OR CHECK BALANCE FUNCTION
def withdraw(user_feedback, user_details,date,times_withdrawn):
    result = {'user_details':user_details,
               'wc_invalid_input': False,
                'yn_invalid_input': False}
    if user_feedback.upper() == 'W':
            # withdraw some money
        how_much = int(input('How much? >>> '))
        
        balance = withdraw_money(how_much, user_details)
        result['user_details']['balance'] = balance
        times_withdrawn += 1

        x = input('Withdraw again? (Y/N) >>> ')

        if (x.upper() == 'Y'):
            withdraw_again = True
        elif (x.upper() == 'N'):
            withdraw_again = False
            first_chance = receipt_w(date, user_details) 
        
            if first_chance['receipt_error'] == True:
                last_chance = receipt_w(date, user_details)
                if last_chance['receipt_error'] == True:
                    print("Sorry we cannot complete your request. Good bye.")
        else:
            withdraw_again = False
            result['yn_invalid_input'] = True
              


        if times_withdrawn < 2 and withdraw_again == True:
                how_much = int(input('How much more? >>> '))
                balance = withdraw_money(how_much, user_details)
                result['user_details']['balance'] = balance
                first_chance = receipt_w(date, user_details) 
        
                if first_chance['receipt_error'] == True:
                    last_chance = receipt_w(date, user_details)
                    if last_chance['receipt_error'] == True:
                       print("Sorry we cannot complete your request. Good bye.")


    elif user_feedback.upper() == 'C':
            # show them the balance
        check_balance(user_details)

        response = input('Do you want to withdraw some money? (Y/N) >>> ')
        if response.upper() == 'Y':
                # withdraw some money
            how_much = int(input('How much? >>> '))
            balance = withdraw_money(how_much, user_details)
            result['user_details']['balance'] = balance
            times_withdrawn += 1

            x = input('Withdraw again? (Y/N) >>> ')

            if (x.upper() == 'Y'):
                withdraw_again = True
            elif (x.upper() == 'N'):
                withdraw_again = False
                first_chance = receipt_cw(date, user_details)
                if first_chance['receipt_error'] == True: ####
                    last_chance = receipt_w(date, user_details)
                    if last_chance['receipt_error'] == True:
                        print("Sorry we cannot complete your request. Good bye.")
                
            else:
                withdraw_again = False
                result['yn_invalid_input'] = True
                
            if times_withdrawn < 2 and withdraw_again == True:
                how_much = int(input('How much more? >>> '))
                balance = withdraw_money(how_much, user_details)
                result['user_details']['balance'] = balance
                first_chance = receipt_cw(date, user_details)
                if first_chance['receipt_error'] == True:  ###
                    last_chance = receipt_cw(date, user_details)
                    if last_chance['receipt_error'] == True:
                        print("Sorry we cannot complete your request. Good bye.")

        elif response.upper() == 'N':   ####
            first_chance = receipt_c(date, user_details)
            
            if first_chance['receipt_error'] == True:
                last_chance = receipt_c(date, user_details)
                if last_chance['receipt_error'] == True:
                    print("Sorry we cannot complete your request. Good bye.")
            

        else:
            print('Invalid input')
            print("Try again")
            result['yn_invalid_input'] = True
    else:
        print(f'Invalid input..Please try again using W for Withdraw or C for Check balance ')
        result['wc_invalid_input'] = True
    
    return result   



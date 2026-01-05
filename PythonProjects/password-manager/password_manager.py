import json #Read and write JSON files (like saving data)
import os #Check if files exist
from datetime import datetime #Get current date and time

#Save all passwords in a file called passwords.json
PASSWORD_FILE = 'password.json'

#Load passwords
def load_passwords():

  if(os.path.exists(PASSWORD_FILE)):
    with open(PASSWORD_FILE,'r') as f:
      return json.load(f)
  return {}

#save passwords
def save_passwords(passwords):

    with open(PASSWORD_FILE,'w') as f:
      json.dump(passwords,f,indent=2)

    

#add passwords
def add_passwords(passwords):
  account = input('Add account for which passwords needs to be saved')

  while account == '':
    print('Account cant be empty')
    account = input('Add account for which passwords needs to be saved')

  userName = input('Enter UserName')
  pasword = input('Enter Password')

  while pasword == '':
    print('Passowrd cant be empty')
    pasword = input('Please Enter Password')

  current_time = datetime.now().strftime('%Y%M%d,%H:%M:%S')
  

  passwords[account]={
    'username':userName,
    'password':pasword,
    'time':current_time
  }
  save_passwords(passwords)
  print('Data saved to file')

#get password
def get_password(passwords):

  account=input('Enter the account to be searched')

  if account in passwords:
    data = passwords[account]
    print(f'Account:{account}')
    print(f'UserName:{data['username']}')
    print(f'Password:{data['password']}')
    print('='*40)

  else:
    print('Account doesnt exist')

#delete password
def delete_password(passwords):
  account = input('Enter account to be deleted')

  while account == '':
    print('Account cannot be empty')
    account = input('Enter account to delete: ').strip()


  if account in passwords:
    confirmation =input('Do you want to delete the account press y or n')
    if(confirmation.lower() == 'y'):
      del passwords[account]
      save_passwords(passwords)
      print(f'✅ {account} is deleted successfully')
    else:
      print('Account not deleted')
  else:
    print('Account doesnt exist')
    
def list_accounts(passwords):

  print('Here is the list of passwords')

  if len(passwords) == 0:
    print('No passwords available')

  for data in passwords:
    print(f'{data}')
    print(f'The userName in account is {passwords[data]['username']}')
    print(f'The Password in account is {passwords[data]['password']}')

def show_menu():
  print('Main Menu for Password Manager')
  print("="*40)
  print('\n 1.Save Password')
  print('\n 2.Get Password')
  print('\n 3.List Password')
  print('\n 4.Delete Account')
  print('\n 5.Exit')
  print("="*40)

def main():
  passwords =load_passwords()

  while True:
    #show_menu
    show_menu()
    user_choice = input('Enter the choice')
    if(user_choice == '1'):
      add_passwords(passwords)
    elif(user_choice == '2'):
      get_password(passwords)
    elif(user_choice == '3'):
      list_accounts(passwords)
    elif(user_choice == '4'):
      delete_password(passwords)
    elif(user_choice == '5'):
      print('GoodBye')
      break
    else:
      print('Invalid choice')


if __name__ == "__main__":
    main()







import datetime
accounts_pass =  dict()
accounts_money = dict()
Transactions_account = dict()
def menu():
    choice =1
    exitprogram = False
    while not exitprogram:
        print("Welcome to our Banking System \n1-Login \n2-Create Account\n0-Quit")
        choice = int(input("Enter the number of operation you want: "))
        if choice == 1:
            login()
        elif choice ==2:
            createAccount()
        elif choice ==0:
            exitprogram = True
        else:
            print("Sorry, the number you entered is invalid")

def CheckAccount(usname):
    print("*"*15)
    print("Username : " + usname + "\nCurrent Money found in account: " + str(accounts_money[usname]) + "$" )
    print("*"*15)

def deposit(usname):
    amntt = input("Enter the amount of money you want to deposit: ")
    amnt = int(amntt)
    accounts_money[usname]+=amnt
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    transaction = "Action : Deposit  Amount : "+ str(amnt) +" At: "+  str(formatted_datetime) 
    Transactions_account[transaction] = usname
    print("Money deposited in your account successfully! \nNow you have " + str(accounts_money[usname]) + "$ available in your account")
    print("*"*15)

def withDraw(usname):
    amntt = input("Enter the amount of money you want to withdraw: " )
    amnt = int(amntt)
    existingamnt = accounts_money[usname]
    if existingamnt<amnt:
        print("Sorry, the amount you entered is not available in your account")
        print("*"*15)
    elif existingamnt - amnt <1000:
        print("Sorry, you cannot withdraw more than " + str(existingamnt-1000))
        print("*"*15)
    else:
        accounts_money[usname]-=amnt
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        transaction = "Action : WithDraw  Amount : "+ str(amnt) +" At: "+  str(formatted_datetime) 
        Transactions_account[transaction] = usname
        print("Money deposited in your account successfully! \nNow you have " + str(accounts_money[usname]) + "$ available in your account")
        print("*"*15)


def Transfer(usname):
    anotherAcc=  (input("Enter the Username of the other account you want to transfer money to: "))
    if anotherAcc not in accounts_pass.keys():
        print("Sorry, this account doesn't exist in our bank, try another account that exists")
        print("*"*15)
    
    else:
        transferAmnt = int(input("Enter the amount of money you want to transfer: "))
        useramnt = accounts_money[usname]
        if transferAmnt>useramnt:
            print("Sorry, the amount you entered is not available in your account")
            print("*"*15)
        elif useramnt-transferAmnt <1000:
            print("Sorry, you cannot withdraw more than " + (useramnt-1000))
            print("*"*15)
        else:
            accounts_money[anotherAcc]+=transferAmnt
            accounts_money[usname]-=transferAmnt
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            transaction = "Action : Transfer From your account to " + anotherAcc +  "Amount : "+ str(transferAmnt) +" At: "+  str(formatted_datetime)
            transaction2 = "Action : Transfer to your account from " + usname +  "Amount : "+ str(transferAmnt) +" At: "+  str(formatted_datetime)
            Transactions_account[transaction] = usname
            Transactions_account[transaction2] = anotherAcc
            print("Money transfered to " +anotherAcc +" successfully! \nNow you have " + str(accounts_money[usname]) + "$ available in your account")
            print("*"*15)

def login():
    usname = input("Enter your username: ")
    password = input("Enter your desired password: ")
    if usname in accounts_pass.keys():
        temppass = accounts_pass[usname]
        if password == temppass:
            print("*"*10)
            print("Welcome " + usname + " !")
            print("*"*10)
            exitProgram = False
            while not exitProgram:
                print("1-Check Account Money \n2-See Transactions\n3-Deposit \n4-Withdraw \n5-Transfer\n0-Quit")
                print("*"*10)
                user_input = input("Enter the number of operation you want: ")
                userchoice = int(user_input)
                if userchoice ==1:
                    CheckAccount(usname)     
                
                elif userchoice ==2:
                    ViewTransactions(usname)
                
                elif userchoice == 3:
                    deposit(usname)
                
                elif userchoice ==4:
                    withDraw(usname)
                
                elif userchoice == 5:
                    Transfer(usname)
                elif userchoice == 0:
                    exitProgram = True
                    return
                else:
                    print("The number of operation you requested doesn't exist")
            else:
                print("Sorry, either username or password is wrong")
        else:
            print("Sorry, this user doesn't exit , try again later")

def createAccount():
    usname = input("Enter your username")
    if usname not in accounts_pass.keys():
        password = input("Enter your desired password,note that password should be at least 8 characters with special character: ")
        phone = int(input("Enter your phone number: "))
        initialamnt = int(input("Enter the initial amount of money you want to deposit: "))
        accounts_pass[usname] = password
        accounts_money[usname] = initialamnt
        print("Congratulations! Account created successfully!")
    else:
        print("Sorry, it seems this username exists, please try another one later")

def main():
    menu()

def ViewTransactions(usname):
    for key, value in Transactions_account.items():
        if value == usname:
            print(key)
            print("*"*15)
            print()
    
    

main()

# regex and input validation
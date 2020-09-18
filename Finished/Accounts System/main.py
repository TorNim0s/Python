import mysql.connector

Accounts = []

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python"
    )

class Account:
    def __init__(self, holder_name, username, password, cash):
        self._holder_name = holder_name
        self._username = username
        self._password = password
        self._cash = cash

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_cash(self):
        return self._cash

    def set_cash(self, amount):
        self._cash = amount
        self.update_cash()

    def deposit(self, amount):
        self._cash += amount
        self.update_cash()

    def withdraw(self, amount):
        self._cash -= amount
        self.update_cash()

    def update_cash(self):
        mycursor = mydb.cursor()

        sql = f"UPDATE customers SET `cash` = {self._cash} WHERE `username` = '{self._username}'"

        mycursor.execute(sql)

        mydb.commit()

    def get_holder_name(self):
        return self._holder_name

    def __str__(self):
        return ("{} Account data: \nusername: {} \npassword: {} \nCash: {}".format(self._holder_name ,self._username, self._password, self._cash))

def import_accounts():
    global mydb
    global Accounts

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS `customers` (name VARCHAR(255) NOT NULL, username VARCHAR(32) PRIMARY KEY NOT NULL,"
                     " password VARCHAR(64) NOT NULL, cash INT NOT NULL)")

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

    for customer in myresult:
        Accounts.append(Account(customer[0], customer[1], customer[2], customer[3]))

def main_screen():
    item_choosed = input("Enter the number of your choosing \n1. Enter account \n2. New account\n")
    if (item_choosed == "1"):
        login_screen()
        return

    elif (item_choosed == "2"):
        register_accounts()
        return

    print("Invalid number")
    main_screen()

def register_accounts():
    global Accounts

    holder_name = input("What's your name?:  ")

    username = input("Please enter a username: ")
    if (not check_valid_username(username)):
        register_accounts()

    password = input("Please enter a password (min 6 characters): ")
    while (len(password) < 6):
        password = input("Incorrect password \nPlease enter a password (min 6 characters): ")

    Accounts.append(Account(holder_name, username, password, 0))

    SQL_New_User(holder_name, username, password, 0)

    main_screen()

def SQL_New_User(holder_name, username, password, cash):
    global mydb
    mycursor = mydb.cursor()

    sql = f'''INSERT INTO customers VALUES ('{holder_name}', '{username}', '{password}', {cash}) '''
    mycursor.execute(sql)

    mydb.commit()

def check_valid_username(username):
    valid = True

    for acc in Accounts:
        if username in acc.get_username():
            valid = False
            break

    return valid

def login_screen():
    username = input("Please Enter your username: ")
    password = input("Please Enter your password: ")

    CheckAccount(username, password)

def CheckAccount(username, password):
    global Accounts
    account_index = -1

    for acc in range(len(Accounts)):
        if username == Accounts[acc].get_username():
            account_index = acc

    if (account_index == -1):
        return False

    if password == Accounts[account_index].get_password():
        print("Approved, Wellcome back {}".format(Accounts[account_index].get_holder_name()))
        Accounts[account_index].deposit(1500)
        return True

    print("Username or password invalid, please try again")
    login_screen()
    return False


def main():
    import_accounts()

    main_screen()
    global Accounts

if __name__ == "__main__":
    main()
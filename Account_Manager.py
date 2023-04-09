from useraccount import useraccount
import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="phyo",
  password="password@35571559",
  database="cinema"
)

cursor = db.cursor()

def login () -> bool:
    
    """ 
    Ask the user username and password and check if the account exist in the database.
    Return True if yes, otherwise False.
    """
    
    print('=' * 10 + "Login Account" + "=" * 10)
    print()
    
    username = input("Enter the username : ")
    password = input("Enter the password : ")
    
    find = findAccount(username, password)
    
    if find:
        return True
    else:
        return False
    
    
    
def registerAccount() -> bool:
    """
    Ask the user to input personal credentials for cinema booking account.
    Then add that account to the database.
    """
    print()
    
    print('=' * 10 + "Creating Account" + "=" * 10)
    print()
    
    username = input("Enter the username : ")
    
    usernameAlrExist = checkUsername(username)
    
    if usernameAlrExist:
        print("Username already Exist, write another")
        return False
    
    userpass = input("Enter the password : ")
    
    useremail = input("Enter your personal email : ")
    
    phone_no = input("Enter your contact number : ")
    
    account = useraccount(username, userpass, useremail, phone_no)
    
    addAccountToDB(account)
    
    return True
    
    
def addAccountToDB(account : useraccount):
    
    sql = "INSERT INTO useraccount(username, password, useremail, phone_num, payment_info, booking_info)" \
           "VALUES (%s, %s, %s, %s, %s, %s)"
           
    values = (account.username, account.password, account.useremail, account.phone_num,
              account.payment_info, account.booking_info)
    
    
    # this is just a sql query
    cursor.execute(sql, values)

    db.commit()
    
def findAccount(username, password) -> bool:
    
    """
    Check if the account with the provided username and password exists in the database.
    Return True if yes.
    """
    
    sql = "SELECT * FROM useraccount where username=%s and password=%s" 
    values = (username, password)
    cursor.execute(sql, values)
    
    row = cursor.fetchone()
    
    if row is not None:
        return True
    else:
        return False    

def checkUsername(username) -> bool:
    
    """Check if the username for account creation already exist""" 
    sql = "SELECT * FROM useraccount where username=%s"
    values = (username,)
    
    cursor.execute(sql, values)
    
    row = cursor.fetchone()
    
    if row is not None:
        return True
    return False
          
def getTotalUserAcccounts ():
    
    """Return total no of accounts created"""
    
    sql = "SELECT COUNT(*) from useraccount"
    
    cursor.execute(sql)
    return cursor.fetchall()[0]

def closeConnection():
    db.close()
    
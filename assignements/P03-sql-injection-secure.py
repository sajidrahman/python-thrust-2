'''
Created on May 28, 2018

@author: sajid
'''
import configparser
import mysql.connector
from pip._vendor.distlib.compat import raw_input
import re


config = configparser.ConfigParser()
config.read('db.ini')
username =  config['DB']['USER']
secret_key = config['DB']['SECRET']
host = config['DB']['HOST']
dbname = config['DB']['DATABASE']

cnx = mysql.connector.connect(user=username, password= secret_key, host=host, database=dbname)


def main():
    while True:
        account = raw_input("Enter account no. or type 'quit' to end: ")
        pattern = r"AB[1-9]\d{5}"
        if re.match(pattern, account): #input validation for a/c number
            option = raw_input("Enter 'd' for deposit, 'w' for withdraw: ")
            if str(option) == 'd':
                amount = raw_input("Enter amount: ")
                deposit(account, amount)
            elif str(option) =='w':
                amount = raw_input("Enter amount: ")
                withdraw(account, amount)
            elif str(account) == "quit":
                sys.exit("The session has ended")
            else:
                print("Not a valid option, please try again!")
        else:
            print("Not a valid account number, please try again!")
    
    

    
  
    
def deposit(account, amount):
    balance, status = check_bal(account)
    if status == "ACTIVE":
        sql = "UPDATE Account SET balance = %s WHERE account_no = %s"
        updated_bal = float(balance) + float(amount)
        try:
            cursor = cnx.cursor(buffered=True)
            cursor.execute(sql, (updated_bal, account))
        except:
            print("An error occurred")
            cursor.close()
            return False
        cnx.commit()
        cursor.close()
        return True
    else:
        print("Transaction not allowed on closed account!!! ")
        return False

def withdraw(account, amount):
    balance, status = check_bal(account)
    updated_bal = float(balance) - float(amount)
    if status == "ACTIVE" and updated_bal > 0:
        sql = "UPDATE Account SET balance = %s WHERE account_no = %s"
        try:
            cursor = cnx.cursor(buffered=True)
            affected_rows = cursor.execute(sql, (updated_bal, account))
            print(affected_rows)
        except:
            print("An error occurred")
            cursor.close()
            return False
        cnx.commit()
        cursor.close()
        return True
    else:
        print("Transaction not allowed on closed account!!! ")
        return False

def check_bal(account):
    sql = "SELECT  balance, status FROM Account WHERE account_no = %s"  
    try:
        cursor = cnx.cursor(buffered=True)
        cursor.execute(sql, (account,))
        row = cursor.fetchone()
        print(row)
        cnx.commit()
        cursor.close()
        return row
    except:
       cursor.close()
       print("An error occurred") 

if __name__=="__main__":
    main()
import os
from pip._vendor.distlib.compat import raw_input


FILE_PATH = 'master.txt'
new_master_file = open("new_master.txt", "a+")
EOF_FLAG = "999999"
def main():
    if os.access(FILE_PATH, os.R_OK):
        with open(FILE_PATH) as fileobj:
            for line in fileobj:
                if line== EOF_FLAG:
                    break
                print("Current customer record: "+line)
                print("current balance: {}".format(get_ac_balance(line)))
                print("customer name: {}".format(get_customer_name(line)))
                deposit = 0
                withdraw = 0
                while(True):
                    user_input = raw_input("Enter any of the following command: deposit - d, withdraw - w,closing a/c - c, next record - a: ")
                    if user_input == 'd':
                        deposit += float(raw_input("Enter deposit amount: "))
                        print(deposit)
                    elif user_input == 'w':
                        withdraw -= float(raw_input("Enter withdraw amount: "))
                    elif user_input == 'c':
                        account_closed = True if get_ac_balance(line)+deposit+withdraw == 0 else False
                        if account_closed:
                            print("Account closed successfully!")
                            break
                        else:
                            print("Account balance not zero")
                        
                    elif user_input =='a':
                        current_balance = get_ac_balance(line) + deposit + withdraw
                        print("{} {} {}".format(get_ac_number(line), current_balance, get_customer_name(line)))
                        new_master_file.write("{} {} {}".format(get_ac_number(line), str(current_balance).rjust(10), get_customer_name(line)))      
                        break
                        
                        
        new_master_file.write(EOF_FLAG)     
        new_master_file.close()   
#     inFile = open('master.txt', 'r')
#     contents = inFile.read()
#     print(contents)

def get_ac_number(single_line):
    return int(single_line[:6])

def get_ac_balance(single_line):
    return float(single_line[7:17])

def get_customer_name(single_line):
    return single_line[18:]    

if __name__=="__main__":
    main()
    
print("All records are saved in a new file. Program is exiting now...")
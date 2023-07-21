#import modules
import string
import random

print("Welcome to our Random Password Generator Environment......")
 
# input password length
length = int(input("Enter the Password length: "))

##getting password type
print('''Select desired character set for password from these :
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
 
password_list = ""
 

while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
         
        # Adding letters to random password
        password_list += string.ascii_letters
        
    elif(choice == 2):
         
        # Adding digits to random password
        password_list += string.digits
        
    elif(choice == 3):
         
        # Adding special characters to random password
        
        password_list += string.punctuation
        
    elif(choice == 4):
        
        # exit
        break
    
    else:
        # if choice is other than list of 4
        print("Sorry,Please Pick a valid option.......!")
 
password = []
 
for i in range(length):
   
    
    randomkey = random.choice(password_list)
    
    #append the password list 
    
    password.append(randomkey)
    
    #print the final output -->generated random password
 


print("Your random password is ", "".join(password))
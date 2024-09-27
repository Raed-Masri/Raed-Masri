# Exercise 1

# def calcFactorial(num):
#     factorial=1
#     for i in range(1,num+1):
#         factorial*=i
#     print("Output",factorial)

# number = int(input("Input: "))
# calcFactorial(number)

#---------------------------------------------------------------------------------------------------------

# Exercise 2

# def findDivisor(num):
#     newList=[]
#     for i in range(1, num+1):
#         if num % i == 0:
#             newList.append(i)
#     print("Output:",newList)

# number = int(input("Input: "))
# findDivisor(number)

#-----------------------------------------------------------------------------------------------------------------

# Exercise 3

# def reverseString(sentence):
#     finalAns= sentence[::-1]
#     print("Output:", finalAns)

# sentence = input("Input: ")
# reverseString(sentence)

#--------------------------------------------------------------------------------------------------------------------

# Exercise 4

# def evenNumbers():
#     evenList=[]
#     input_str = input("Input: ")
#     number_list = input_str.split()
#     print(number_list)
#     for i in number_list:
#         if (int(i)%2 ==0):
#             evenList.append(i)

#     print(evenList)

# evenNumbers()

#----------------------------------------------------------------------------------------------------------------------

# Exercise 5

# def check_password(password):
    
#     special_characters = {'#', '?', '!', '$', '@','%','&'}
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special = False
    
#     if len(password) < 8:
#         print("Weak password")
    
#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in special_characters:
#             has_special = True
    

#     if has_upper and has_lower and has_digit and has_special:
#         print ("Strong password")
#     else:
#         print ("Weak password")

# password= input("Input: ")
# check_password(password)

#---------------------------------------------------------------------------------------------------------------

# Exercise 6

# def valid_ipv4(ip):
    
#     octets = ip.split('.')
#     if len(octets) != 4:
#         print('ip address should contains 4 octets')
    
#     for octet in octets:
#         if not octet.isdigit():
#             print ('octet is not a digit')
        
#         num = int(octet)
        
#         if num < 0 or num > 255 or (octet != 0 and octet[0] == 0):
#             return 'error'
    


# ipv4= input("Input: ")
# valid_ipv4(ipv4)


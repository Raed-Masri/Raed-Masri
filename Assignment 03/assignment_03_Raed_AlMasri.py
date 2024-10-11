def countDigits():
    def count_digits(num):
        if num<10:
            return 1
        else:
            return 1 + count_digits(num // 10)
    digit = int(input("Input: "))
    print("Output: ",count_digits(digit))

def findMax():
    def find_max_recursive(lst):

        if not lst:  # if the list is empty
            return 0
   
        if len(lst) == 1:    # if the list has one element return it
            return lst[0]
    
        maximum = find_max_recursive(lst[1:])
    
        if lst[0] > maximum:
            return lst[0]
        else:
            return maximum

    input_string = input("Input: ")
    int_list = list(map(int, input_string.split(',')))
    result = find_max_recursive(int_list)
    print("Output:",result)


def countTags():
    return 1

def exit_program():
    return 0


print("1. Count Digits")
print("2. Find Max")
print("3. Count Tags")
print("4. Exit")
print("---------------")

option=int(input("Enter a choice: "))

if option == 1:
    countDigits()
elif option == 2:
    findMax()
elif option == 3:
    countTags()
else:
    exit_program()

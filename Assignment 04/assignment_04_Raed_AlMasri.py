
def sum_tuples(tup1, tup2):
    return tuple(a + b for a, b in zip(tup1, tup2))

def export_json(data, filename):
    with open(filename, 'w') as file:
        json_str = "{\n"
        json_str += ",\n".join(f'  "{key}": {repr(value)}' for key, value in data.items())
        json_str += "\n}"
        file.write(json_str)
        print(f"Data successfully written to {filename}.")

def import_json(filename):
    data_list = []
    
    with open(filename, 'r') as file:
        content = file.read().strip('{} \n')
        objects = content.split('},')
        for obj in objects:
            obj = obj.strip(' {}') + '}'
            dictionary = eval(obj.replace("'", "\""))
            data_list.append(dictionary)
        return data_list
    
    
def display_menu():
    print("1. Sum Tuples")
    print("2. Export JSON")
    print("3. Import JSON")
    print("4. Exit")
    print("-----------------")

def main():
    while True:
        display_menu()
        choice = input("Enter a choice: ")

        if choice == '1':
            tup1 = tuple(map(int, input("Enter elements of the first tuple: ").split(',')))
            tup2 = tuple(map(int, input("Enter elements of the second tuple: ").split(',')))
            if len(tup1) != len(tup2):
                print("Tuples must have the same length")
            else:
                result = sum_tuples(tup1, tup2)
                print(f"Result: {result}")

        elif choice == '2':
            dictionary = eval(input("Enter a dictionary: "))
            filename = input("Enter a filename to export to: ")
            export_json(dictionary, filename)

        elif choice == '3':
            filename = input("Enter the JSON filename to import from: ")
            data = import_json(filename)
            print(f"Imported Data: {data}")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice.")


main()

# -------------------------------------------------------
# Exercise 2

# a- Order of Growth: O(N3)
# The highest-order term dominates.

# b- Order of Growth: O(N3)
# Constants are ignored in Big-O notation. 

# c- Order of Growth: O(N!)
# Factorial growth is faster than any polynomial.

# d- Order of Growth: O(N log N)
# The logarithmic term dominates over constants.

# e- Order of Growth: O(N)
# Linear growth dominates logarithmic growth.

# f- Order of Growth: O(N2)
# Equal to 1/2(N2-N), the quadratic term dominates.

# g- Order of Growth: O(N2)
# Polynomial N2 grows faster than the N log N2 term for large N

# h- Order of Growth: O(N!)
# Factorial growth dominates exponential, polynomial, and constant terms.
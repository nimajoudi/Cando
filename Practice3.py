from colorama import Fore, Style, init

init()

def create_multiplication_table(num1, num2):
    table = []
    results = []
    for i in range(1, num1 + 1):
        row = []
        for j in range(1, num2 + 1):
            if i == 2 or j == 2:
                row.append(None)  # نادیده گرفتن عدد 2 در سطر و ستون
            else:
                product = i * j
                row.append(product)
                results.append(product)
        table.append(row)
    return table, results

def print_colored_table(table):
    for i, row in enumerate(table):
        for j, item in enumerate(row):
            if item is None:
                print("   ", end=" ")
            elif i == 3 or j == 3:  # سطر و ستون عدد 4
                print(f"{Fore.RED}{item:3}{Style.RESET_ALL}", end=" ")
            else:
                print(f"{Fore.YELLOW}{item:3}{Style.RESET_ALL}", end=" ")
        print()

def extract_even_numbers(results):
    even_numbers = [num for num in results if num % 2 == 0]
    return even_numbers

def main():
    num1 = int(input("عدد اول را وارد کنید (بین 6 تا 10): "))
    num2 = int(input("عدد دوم را وارد کنید (بین 6 تا 10): "))
    
    if not (6 <= num1 <= 10 and 6 <= num2 <= 10):
        print("اعداد باید بین 6 تا 10 باشند.")
        return
    
    table, results = create_multiplication_table(num1, num2)
    print_colored_table(table)
    
    even_numbers = extract_even_numbers(results)
    print("اعداد زوج استخراج شده:", even_numbers)


main()
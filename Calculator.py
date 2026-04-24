def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a / b

def power(a, b):
    return a ** b

def main():
    print("Оберіть операцію:")
    print("1 - Додавання")
    print("2 - Віднімання")
    print("3 - Множення")
    print("4 - Ділення")
    print("5 - Піднесення до степеня")

    choice = input("Ваш вибір (1/2/3/4/5): ")

    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if choice == '1':
            print("Результат:", add(num1, num2))
        elif choice == '2':
            print("Результат:", subtract(num1, num2))
        elif choice == '3':
            print("Результат:", multiply(num1, num2))
        elif choice == '4':
            print("Результат:", divide(num1, num2))
        elif choice == '5':
            print("Результат:", power(num1, num2))
        else:
            print("Невірний вибір операції")
    except ValueError:
        print("Помилка: введіть коректні числа!")

if __name__ == "__main__":
    main()
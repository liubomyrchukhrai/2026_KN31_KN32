import unittest

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

# Новий метод: Піднесення до степеня
def power(a, b):
    return a ** b

# --- Клас з юніт-тестами ---
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        
    def test_multiply(self):
        self.assertEqual(multiply(3, 3), 9)
        
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), "Помилка: ділення на нуль!")
        
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

# --- Логіка інтерфейсу ---
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
    # Якщо ви хочете запустити ТЕСТИ, розкоментуйте рядок нижче і закоментуйте main()
    # unittest.main() 
    
    # Зараз запускається звичайна програма
    main()

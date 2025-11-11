class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero!")
        return a / b

    print("Conflict from Myros")

if __name__ == "__main__":
    calc = Calculator()
    print("Conflict test by Burla")

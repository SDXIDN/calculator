class Calculator:
    def add(self, a, b):
        # TODO: implement addition
        raise NotImplementedError

    def subtract(self, a, b):
        # TODO: implement subtraction
        raise NotImplementedError

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero!")
        return a / b


if __name__ == "__main__":
    calc = Calculator()
    print("Team calculator ready!")

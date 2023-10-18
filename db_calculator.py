class Calculator:
    def __init__(self, save_to_file=False):
        self.save_to_file = save_to_file


    def add(self, a, b):
        self.result = a + b
        if self.save_to_file:
            self.save_result_to_file(self.result)
        return self.result


    def subtract(self, a, b):
        self.result = a - b
        if self.save_to_file:
            self.save_result_to_file(self.result)
        return self.result


    def multiply(self, a, b):
        self.result = a * b
        if self.save_to_file:
            self.save_result_to_file(self.result)
        return self.result


    def divide(self, a, b):
        if b == 0:
            if self.save_to_file:
                lf.save_result_to_file(self.result)
            self.result = "Cannot divide by zero"
        else:
            if self.save_to_file:
                self.save_result_to_file(self.result)
            self.result = a / b

        return self.result
        

    def save_result_to_file(self, result, filename="results.txt"):
        with open(filename, "a") as file:
            file.write(str(result) + "\n")

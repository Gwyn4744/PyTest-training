from pathlib import Path


class Calculator:
    def __init__(self, save_to_file=False):
        self.save_to_file = save_to_file
        self.result = None
        self.init_last_values_dict()


    def init_last_values_dict(self):
        self.last_values_dict = {}
        self.last_values_dict['add'] = None
        self.last_values_dict['subtract'] = None
        self.last_values_dict['multiply'] = None
        self.last_values_dict['divide'] = None


    def add(self, a, b):
        self.result = a + b
        self.last_values_dict['add'] = self.result
        if self.save_to_file:
            self.save_result_to_file(self.result)
        return self.result


    def subtract(self, a, b):
        self.result = a - b
        self.last_values_dict['subtract'] = self.result
        if self.save_to_file:
            self.save_result_to_file(self.result)
        return self.result


    def multiply(self, a, b):
        self.result = a * b
        self.last_values_dict['multiply'] = self.result
        if self.save_to_file:
            self.save_result_to_file(self.result)
        return self.result


    def divide(self, a, b):
        if b == 0:
            if self.save_to_file:
                self.save_result_to_file(self.result)
            self.result = "Cannot divide by zero"
        else:
            if self.save_to_file:
                self.save_result_to_file(self.result)
            self.result = a / b
            self.last_values_dict['divide'] = self.result

        return self.result
    

    def last_result(self):
        return f'{self.result}'
    

    def last_result_verbose(self):
        if self.result == None:
            return f'no activity has been carried out'
        
        return (f'The last result was {self.last_result()}.')
        

    def save_result_to_file(self, result, filename="results.txt"):
        with open(filename, "a") as file:
            file.write(str(result) + "\n")

    
    def remove_results_file(self, filename="results.txt"):
        file = Path(filename)
        try:
            file.unlink()
            return f'The file {filename} has been deleted.'
        except FileNotFoundError:
            return f'The file {filename} does not exist.'
        except PermissionError:
            return f'You do not have permission to delete the {filename} file.'
        except Exception as e:
            return f'An error occurred while deleting file {filename}: {str(e)}'
        
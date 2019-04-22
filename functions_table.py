from variable import Variable
from function import Function
from pprint import *

class FunctionsTable:
    # Global and Local variables and functions
    def __init__(self):
        self._functions = {}

    # Check if function name is valid
    def add_function(self, item):
        if item.function_id in self._functions:
            print("Error, function {} already exists".format(item.function_id))             
            exit(1)
        else:
            self._functions[item.function_id] = item   
            # print("Function added")
            # print(self._functions.items())

    def find_function(self, function_id):
        if function_id not in self._functions:
            print("Undefined function")
            exit(1)
        else:
            return self._functions[function_id]
    
    def find_variable(self, var_id):
        for f in self._functions:
            if var_id in self._functions[f].variables_directory:
                return self._functions[f].variables_directory[var_id].var_type
       # Variable is not found 
        print("Undefined variable")
        exit(1)

    def find_var_address(self, var_id):
        for f in self._functions:
            if var_id in self._functions[f].variables_directory:
                return self._functions[f].variables_directory[var_id].var_address
       # Variable is not found 
        print("Undefined variable")
        exit(1)

    # Add variable
    def add_variable(self, item, current_function):
        variables_directory = self._functions[current_function.function_id].variables_directory.items()

        if item.var_id in variables_directory:
            print("Error, variable {} already exists".format(item.var_id))
            exit(1)
        else:
            f = self._functions[current_function.function_id]
            f.declare_variable(item.var_id, item.var_type, item.var_address)
            # self._functions[current_function.function_id].variables_directory[item.var_id] = item.var_type
            # print("Variable added")
            # print(self._functions[current_function.function_id].variables_directory.items())
    
    # Add parameter
    def add_param(self, item, current_function):
        self._functions[current_function.function_id].params_list.append(item.var_type)
        # print("Parameter type added")
        # print(self._functions[current_function.function_id].params_list)

    def print_table(self):
        for f in self._functions.items():
            print(f[1])
            for var in f[1].variables_directory.items():
                print("Variables directory: ", var[1])
            

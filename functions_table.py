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

    def function_exists(self, function_id):
        if function_id not in self._functions:
            print("Undefined function")
            exit(1)
        else:
            return True

    
    def find_variable(self, var_id, function_id):
        # print("function id at find_variable: ", function_id)
        # print("var_id: ", var_id, "function_id: ", function_id)

        if (function_id != "Mathrix"):
            # Check if it is a  local variable
            variables_directory = self._functions[function_id].variables_directory

            if var_id in variables_directory:
                return variables_directory[var_id]
            else:
                # Check if it is a global variable
                variables_directory = self._functions["Mathrix"].variables_directory
                
                if var_id in variables_directory:
                    return variables_directory[var_id]
                else:
                    # Variable is not found 
                    print("Undefined variable 1: ", var_id)
                    exit(1)
        else:
            variables_directory = self._functions["Mathrix"].variables_directory
            if var_id in variables_directory:
                return variables_directory[var_id]
            else:
                # Variable is not found 
                print("Undefined variable 2: ", var_id)
                exit(1)

    #     # Check if it is a local variable
    #     for f in self._functions:
    #         if var_id in self._functions[f].variables_directory:
    #             return self._functions[f].variables_directory[var_id].var_type
    #    # Variable is not found 
    #     print("Undefined variable")
    #     exit(1)

    def find_var_address(self, var_id, function_id):
        # Check if it is a  local variable
        if (function_id != "Mathrix"):
            variables_directory = self._functions[function_id].variables_directory
            # print("function_id", function_id)
            # print("var_id", var_id)

            if var_id in variables_directory:
                return variables_directory[var_id].var_address
            else:
                # Check if it is a global variable
                variables_directory = self._functions["Mathrix"].variables_directory
            
                if var_id in variables_directory:
                    return variables_directory[var_id].var_address
                else:
                    # Variable is not found 
                    print("Undefined variable 3: ", var_id)
                    exit(1)
        else:
            variables_directory = self._functions["Mathrix"].variables_directory
            if var_id in variables_directory:
                return variables_directory[var_id].var_address
            else:
                # Variable is not found 
                print("Variable not found 4: ", var_id)
                exit(1)


    # Add variable
    def add_variable(self, item, current_function, memory):
        # print("var to add var_id: ", item.var_id, "to function_id: ", current_function.function_id)

        if (current_function.function_id == "Mathrix"):
            # Add global variable
            variables_directory = self._functions["Mathrix"].variables_directory.items()
            
            if item.var_id in variables_directory:
                print("Error, variable {} already exists".format(item.var_id))
                exit(1)
            else:
                item.var_address = memory.set_address(item, current_function.function_id)
                f = self._functions[current_function.function_id]
                f.declare_variable(item.var_id, item.var_type, item.var_address)
                # print("Variable: ", item.var_id, " added to function: ", current_function.function_id)
                # print(self._functions[current_function.function_id].variables_directory.items())
        else:
            variables_directory = self._functions[current_function.function_id].variables_directory.items()

            if item.var_id in variables_directory:
                print("Error, variable {} already exists".format(item.var_id))
                exit(1)
            else:
                item.var_address = memory.set_address(item, current_function.function_id)
                f = self._functions[current_function.function_id]
                f.declare_variable(item.var_id, item.var_type, item.var_address)
                # print("Variable: ", item.var_id, " added to function: ", current_function.function_id)
                # print(self._functions[current_function.function_id].variables_directory.items())

        
        # variables_directory = self._functions[current_function.function_id].variables_directory.items()

        # if item.var_id in variables_directory:
        #     print("Error, variable {} already exists".format(item.var_id))
        #     exit(1)
        # else:
        #     f = self._functions[current_function.function_id]
        #     f.declare_variable(item.var_id, item.var_type, item.var_address)
            # self._functions[current_function.function_id].variables_directory[item.var_id] = item.var_type
            # print("Variable added")
            # print(self._functions[current_function.function_id].variables_directory.items())
    
    def find_constant(self, item):
        variables_directory = self._functions["Mathrix"].variables_directory

        if item.var_id in variables_directory:
            return True
        else:
            return False

    def add_constant(self, item):
        #print("Var_id: ", item.var_id)
        #print(self._functions["Mathrix"].variables_directory.items())

        f  = self._functions["Mathrix"]
        f.declare_variable(item.var_id, item.var_type, item.var_address)
        #print("Constant added: ", item.var_id)


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
            

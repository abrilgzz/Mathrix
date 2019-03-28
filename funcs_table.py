from variable import Variable
from function import Function

class FunctionsTable:
    # Global and Local variables and functions
    def __init__(self):
        self._functions = {}

    # Check if function name is valid
    def add_function(self, item):
        if item.function_ID in self._functions:
            print("Error, function {} already exists".format(item.function_ID))             
            exit(1)
        else:
            self._functions[item.function_ID] = item
            # print("Function added")
            # print(self._functions.items())

    def find_function(self, function_ID):
        print("I got here")
        if function_ID not in self._functions:
            print("Undefined function")
            exit(1)
        else:
            return self._functions[function_ID]
    
    def find_variable(self, var_ID):
        print("I got here")
        for f in self._functions:
            if var_ID in self._functions[f.varsTable]:
                return self._functions[f.varsTable].get(var_ID)
       # Variable is not found 
        print("Undefined variable")
        return None

    # Add variable
    def add_variable(self, item, currentFunction):
        varsdict = self._functions[currentFunction.function_ID].varsTable.items()

        if item.var_ID in varsdict:
            print("Error, variable {} already exists".format(item.var_ID))
            exit(1)
        else:
            self._functions[currentFunction.function_ID].varsTable[item.var_ID] = item.var_TYPE
            # print("Variable added")
            # print(self._functions[currentFunction.function_ID].varsTable.items())
        
        
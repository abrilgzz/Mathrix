class Functions:
    def _init_(self, function_ID = None, function_TYPE= None, parameters = None):
        self.function_ID = function_ID
        self.function_TYPE = function_TYPE
        self.parameters = parameters

class Variables:
    def _init_(self, var_ID, var_TYPE):
        self.var_ID = var_ID
        self.var_TYPE = var_TYPE


class VariablesTable:
    # Global and Local variables and functions
    def _init_(self):
        self._global = {}
        self._local = {}
        self._functions = {}

    # Variables
    def add_global(self, item):
        if item.var_ID in self._global:
            print("Error, variable already exists")
        else:
            self._global[item.var_ID] = item

    def add_local(self, item):
        if item.var_ID in self._local:
            print("Error, variable already exists")
        else:
            self._local[item.var_ID] = item

    def find_variable(self, varID):
        # First search on global then local scope
        if varID in self._global:
            return self._global.get(varID)
        elif varID in self._local:
            return self._local.get(varID)
        else:
            print("Undefined variable")

    # Functions
    def add_function(self, item):
        if item.var_ID in self._functions:
            print("Error, function already exists")
        else:
            self._functions[item.function_ID] = item

    def find_function(self, function_ID):
        if function_ID not in self._functions:
            print("Undefined function")
        else:
            return self._functions[function_ID]
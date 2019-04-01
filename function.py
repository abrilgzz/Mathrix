

class Function:
    def __init__(self, function_id, function_type, variables_directory):
        self.function_id = function_id
        self.function_type = function_type
        self.variables_directory = variables_directory
    
    def declareVar(self, variable):
        self.variables_directory[variable.var_id] = variable.var_type
        
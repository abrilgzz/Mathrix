from variable import Variable

class Function(dict):
    def __init__(self, function_id, function_type, variables_directory, params_list, start_address, ints, doubles, bools):
        self.function_id = function_id
        self.function_type = function_type
        self.variables_directory = variables_directory
        self.params_list = params_list
        self.start_address = start_address
        self.ints = ints
        self.doubles = doubles
        self.bools = bools
    
    def declare_variable(self, var_id, var_type, var_address, var_dim1_dict, var_dim2_dict):
        # Create variable
        v = Variable(var_id, var_type, var_address, var_dim1_dict, var_dim2_dict)
        # Append to variables_directory
        self.variables_directory[var_id] = v
       
    def __str__(self):
        return str(self.__dict__)

from fastnumbers import fast_real
from functions_table import Variable
from constants import Types


class ExecutionMemory(object):
    def __init__(self):
        # Global variable addresses
        self.global_int = 5000
        self.global_double = 6000
        self.global_bool = 7000

        # Local variable addresses
        self.local_int = 9000
        self.local_double = 10000
        self.local_bool = 11000

        # Temporal variable addresses
        self.temp_int = 43000
        self.temp_double = 44000
        self.temp_bool = 45000

        # Constant variable addresses
        self.cte_int = 20000
        self.cte_double = 21000
        self.cte_bool = 22000

        # Storing vars
        self.memory = {}
        self.memory['global'] = {}

        self.memory['global']['var'] = {}
        self.memory['global']['temp'] = {}
        self.memory['global']['cte'] = {}  

        self.memory['global']['var']['int'] = {}
        self.memory['global']['var']['double'] = {}
        self.memory['global']['var']['bool'] = {}

        self.memory['global']['temp']['int'] = {}
        self.memory['global']['temp']['double'] = {}
        self.memory['global']['temp']['bool'] = {}

        self.memory['global']['cte']['int'] = {}
        self.memory['global']['cte']['double'] = {}
        self.memory['global']['cte']['bool'] = {}

        self.memory['local'] = {}


    def get_variable_value(self, address, current_function):
        # print("address: ", address)
        # print("current_function: ", current_function)
        if self.is_address_reference(address):
            address = self.dereference(address)

        # Check if it is a global variable
        if (5000 <= address <= 8999):
            if(5000 <= address <= 5999):
                return int(self.memory['global']['var']['int'][address])
            elif(6000 <= address <= 6999):
                return self.memory['global']['var']['double'][address]
            elif(7000 <= address <= 7999):
                return self.memory['global']['var']['bool'][address]
         # Check if it is a constant
        if (20000 <= address <= 22999):
            if(20000 <= address <= 20999):
                return int(self.convert_constant(self.memory['global']['cte']['int'][address]))
            elif(21000 <= address <= 21999):
                return self.convert_constant(self.memory['global']['cte']['double'][address])
            elif(22000 <= address <= 22999):
                return self.convert_constant(self.memory['global']['cte']['bool'][address])   
        elif(current_function == 'Mathrix'):
            # Check if it is temp
            if (43000 <= address <= 45999):
                if(43000 <= address <= 43999):
                    return int(self.memory['global']['temp']['int'][address])
                elif(44000 <= address <= 44999):
                    return self.memory['global']['temp']['double'][address]
                elif(45000 <= address <= 45999):
                    return self.memory['global']['temp']['bool'][address]
        else:
            # Local variables
            # print("current_function to get val from: ", current_function)
            # print("type: ", type(current_function))
            # print(self.memory['local'][current_function]['var']['int'])
            
            if (9000 <= address <= 11999):
                if(9000 <= address <= 9999):
                    return int(self.memory['local'][current_function]['var']['int'][address])
                elif(10000 <= address <= 10999):
                    return self.memory['local'][current_function]['var']['double'][address]
                elif(11000 <= address <= 11999):
                    return self.memory['local'][current_function]['var']['bool'][address]
            # Check if it is temp
            if (43000 <= address <= 45999):
                if(43000 <= address <= 43999):
                    return int(self.memory['local'][current_function]['temp']['int'][address])
                elif(44000 <= address <= 44999):
                    return self.memory['local'][current_function]['temp']['double'][address]
                elif(45000 <= address <= 45999):
                    return self.memory['local'][current_function]['temp']['bool'][address]


    def write_to_memory(self, address, result, current_function):
        # print("address: ", address)
        # print("current_function: ", current_function)
        # print("memory: ", self.memory)

        if self.is_address_reference(address):
            address = self.dereference(address)
        
        # if self.is_address_reference(result):
        #     result = self.dereference(result)

        # Check if it is a global variable
        if (5000 <= address <= 8999):
                if(5000 <= address <= 5999):
                    self.memory['global']['var']['int'][address] = result
                elif(6000 <= address <= 6999):
                    self.memory['global']['var']['double'][address] = result
                elif(7000 <= address <= 7999):
                    self.memory['global']['var']['bool'][address] = result
        # Check if it is a constant
        elif (20000 <= address <= 22999):
                if(20000 <= address <= 20999):
                    self.memory['global']['cte']['int'][address] = result
                elif(21000 <= address <= 21999):
                    self.memory['global']['cte']['double'][address] = result
                elif(22000 <= address <= 22999):
                    self.memory['global']['cte']['bool'][address] = result
        elif(current_function == 'Mathrix'):
            # Check if it is temp
            if (43000 <= address <= 45999):
                if(43000 <= address <= 43999):
                    self.memory['global']['temp']['int'][address] = result
                elif(44000 <= address <= 44999):
                    self.memory['global']['temp']['double'][address] = result
                elif(45000 <= address <= 45999):
                    self.memory['global']['temp']['bool'][address] = result
        else:
            # Local variables
            if (9000 <= address <= 11999):
                if(9000 <= address <= 9999):
                    self.memory['local'][str(current_function)]['var']['int'][address] = result 
                elif(10000 <= address <= 10999):
                    self.memory['local'][str(current_function)]['var']['double'][address] = result
                elif(11000 <= address <= 11999):
                    self.memory['local'][str(current_function)]['var']['bool'][address] = result
            # Check if it is temp
            elif (43000 <= address <= 45999):
                if(43000 <= address <= 43999):
                    self.memory['local'][str(current_function)]['temp']['int'][address] = result 
                elif(44000 <= address <= 44999):
                    self.memory['local'][str(current_function)]['temp']['double'][address] = result
                elif(45000 <= address <= 45999):
                    self.memory['local'][str(current_function)]['temp']['bool'][address] = result

    def write_param_to_memory(self, param_type, param_number, param, function_counter):
        address = int(param_number) + 9000

        if param_type == Types.INT.value:
            var_type = 'int'
            param = int(param)
        elif param_type == Types.DOUBLE.value:
            var_type = 'double'
            param = int(param)
        if param_type == Types.BOOL.value:
            var_type = 'bool'

        # print("function_counter: ", function_counter)
        # print(self.memory['local'][str(function_counter-1)]['var'])
        # print(self.memory['local'][str(function_counter-1)]['var'][var_type])
        self.memory['local'][str(function_counter-1)]['var'][var_type][address] = param
        #print(self.memory['local'][str(function_counter-1)]['var'][var_type][address])

        #self.memory['local'][str(function_counter-1)]['var'][var_type][address] = param

    def clear_memory(self, function):
        self.memory['local'][function].clear()

    def end_program(self):
        self.memory.clear()
    
    def start_local_memory(self, local_vars_quad, temp_vars_quad, function_counter):
        self.memory['local'][str(function_counter)] = {}

        self.memory['local'][str(function_counter)]['var'] = {}
        self.memory['local'][str(function_counter)]['var']['int'] = {}
        self.memory['local'][str(function_counter)]['var']['double'] = {} 
        self.memory['local'][str(function_counter)]['var']['bool'] = {}

        self.memory['local'][str(function_counter)]['temp'] = {}
        self.memory['local'][str(function_counter)]['temp']['int'] = {}
        self.memory['local'][str(function_counter)]['temp']['double'] = {}
        self.memory['local'][str(function_counter)]['temp']['bool'] = {}

    def start_global_memory(self, vars_directory):
        # Initialize spaces in memory global vars:
        for v in vars_directory:
            variable = vars_directory[v]
            # print("adding ", variable, " to memory")
            if self.is_matrix(variable) and variable.var_type != Types.BOOL.value:
                self.create_matrix(variable, 'Mathrix')
            else:
            # Atomic variables
                # Global variables
                if(5000 <= variable.var_address <= 8999):
                    if(variable.var_type == Types.INT.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                    if(variable.var_type == Types.DOUBLE.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                    if(variable.var_type == Types.BOOL.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                # Constant variables
                elif (20000 <= variable.var_address <= 22999):
                    if(variable.var_type == Types.INT.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                    if(variable.var_type == Types.DOUBLE.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                    if(variable.var_type == Types.BOOL.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                # Temp variables
                elif (43000 <= variable.var_address <= 45999):
                    if(variable.var_type == Types.INT.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                    if(variable.var_type == Types.DOUBLE.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                    if(variable.var_type == Types.BOOL.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
            
    
    def is_matrix(self, variable):
        if variable.var_dim1_dict != 0:
            return True

    def create_matrix(self, variable, current_function):
        spaces_needed = self.calculate_m0(variable)
        counter = 0

        for x in range(0, spaces_needed):
            self.write_to_memory(variable.var_address + counter, -1, current_function)
            counter+=1

    def calculate_m0(self, variable):
        # Formulas for 2 dimensional arrays
        r1 = 1 * (variable.var_dim1_dict.lim_s - 0 + 1)
        m0 = r1 * (variable.var_dim2_dict.lim_s - 0 + 1)
        return m0
    
    def convert_constant(self, value):
        number = fast_real(value[1:])
        return number

    def is_address_reference(self, value):
        value = str(value)
        if '(' in value:
            #print("is reference")
            return True

    def dereference(self, address_ref):
        address_ref = address_ref[:-1]
        address_ref = address_ref[1:]
        print("address_ref: ", address_ref)
        return int(address_ref)




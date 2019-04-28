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

        self.memory['global']['var']['int'] = []
        self.memory['global']['var']['double'] = []
        self.memory['global']['var']['bool'] = []

        self.memory['global']['temp']['int'] = []
        self.memory['global']['temp']['double'] = []
        self.memory['global']['temp']['bool'] = []

        self.memory['global']['cte']['int'] = []
        self.memory['global']['cte']['double'] = []
        self.memory['global']['cte']['bool'] = []


        self.memory['local'] = {}

        self.mem_int = {}
        self.mem_double = {}
        self.mem_bool = {}
        self.mem_temp = {}

    def get_variable_value(self, address, current_function):
        # Opcion1
        # Check if it is a global variable
        if (5000 <= address <= 8999):
                if(5000 <= address <= 5999):
                    return self.memory['global']['var']['int'][address]
                elif(6000 <= address <= 6999):
                    return self.memory['global']['var']['double'][address]
                elif(7000 <= address <= 7999):
                    return self.memory['global']['var']['bool'][address]
        elif(current_function == "Mathrix"):
            # Check if it is temp
            if (43000 <= address <= 45999):
                if(43000 <= address <= 43999):
                    return self.memory['global']['temp']['int'][address]
                elif(44000 <= address <= 44999):
                    return self.memory['global']['temp']['double'][address]
                elif(45000 <= address <= 45999):
                    return self.memory['global']['temp']['bool'][address]
            # Check if it is a constant
            if (20000 <= address <= 22999):
                if(20000 <= address <= 20999):
                    return self.memory['global']['cte']['int'][address]
                elif(21000 <= address <= 21999):
                    return self.memory['global']['cte']['double'][address]
                elif(22000 <= address <= 22999):
                    return self.memory['global']['cte']['bool'][address]
            else:
                print("Invalid address")
                exit(1)
        else:
            # Local variables
            # Check if it is temp
            if (43000 <= address <= 45999):
                if(43000 <= address <= 43999):
                    return self.memory['local']['temp']['int'][address]
                elif(44000 <= address <= 44999):
                    return self.memory['local']['temp']['double'][address]
                elif(45000 <= address <= 45999):
                    return self.memory['local']['temp']['bool'][address]

    def write_to_memory(self, address, result, current_function):
        # Check if it is a global variable
        if (5000 <= address <= 8999):
                if(5000 <= address <= 5999):
                    self.memory['global']['var']['int'][address] = result
                elif(6000 <= address <= 6999):
                    self.memory['global']['var']['double'][address] = result
                elif(7000 <= address <= 7999):
                    self.memory['global']['var']['bool'][address] = result
        elif(current_function == "Mathrix"):
            # Check if it is temp
            if (43000 <= address <= 45999):
                if(43000 <= address <= 43999):
                    self.memory['global']['temp']['int'][address] = result
                elif(44000 <= address <= 44999):
                    self.memory['global']['temp']['double'][address] = result
                elif(45000 <= address <= 45999):
                    self.memory['global']['temp']['bool'][address] = result
            # Check if it is a constant
            if (20000 <= address <= 22999):
                if(20000 <= address <= 20999):
                    self.memory['global']['cte']['int'][address] = result
                elif(21000 <= address <= 21999):
                    self.memory['global']['cte']['double'][address] = result
                elif(22000 <= address <= 22999):
                    self.memory['global']['cte']['bool'][address] = result
            else:
                print("Invalid address")
                exit(1)
        else:
            # Local variables
            # Check if it is temp
            if (43000 <= address <= 45999):
                if(43000 <= address <= 43999):
                    self.memory['local']['temp']['int'][address] = result 
                elif(44000 <= address <= 44999):
                    self.memory['local']['temp']['double'][address] = result
                elif(45000 <= address <= 45999):
                    self.memory['local']['temp']['bool'][address] = result

    def write_param_to_memory(self, param_type, param, current_function):
        return True
        # TO-DO

    def clear_memory(self, function):
        self.memory['local'][function].clear()

    def end_program(self):
        self.memory.clear()
    
    def start_local_memory(self, quad):
        return True
        # TO-DO
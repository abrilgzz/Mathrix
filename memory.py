from variable import Variable
from function import Function
from constants import *

class Memory:
    def __init__(self):
        # Global variable addresses
        self.global_int = 1000
        self.global_double = 3000
        self.global_bool = 6000

        # Local variable addresses
        self.local_int = 11000
        self.local_double = 13000
        self.local_bool = 16000

        # Temp variable addresses
        self.temp_int = 21000
        self.temp_double = 23000
        self.temp_bool = 26000

        # Variable counters
        self.global_int_counter = 0
        self.global_double_counter = 0
        self.global_bool_counter = 0

        self.local_int_counter = 0
        self.local_double_counter = 0
        self.local_bool_counter = 0


    def set_address(self, variable, function_id):
        address = -1

        # Set address for global variables
        if (function_id == "Mathrix"):
            # Assign address for int var
            if (variable.var_type == Types.INT.value):
                address = self.global_int + self.global_int_counter
                self.global_int_counter+=1
                return address
            # Assign address for double var
            elif (variable.var_type == Types.DOUBLE.value):
                address = self.global_double + self.global_double_counter
                self.global_double_counter+=1
                return address
            # Assign address for bool var
            elif (variable.var_type == Types.BOOL.value):
                address = self.global_bool + self.global_bool_counter
                self.global_bool_counter+=1
                return address
        # Set address for local variables
        else:
            # Assign address for int var
            if (variable.var_type == Types.INT.value):
                address = self.local_int + self.local_int_counter
                self.local_int_counter+=1
                return address
            # Assign address for double var
            elif (variable.var_type == Types.DOUBLE.value):
                address = self.local_double + self.local_double_counter
                self.local_double_counter+=1
                return address
            # Assign address for bool var
            elif (variable.var_type == Types.BOOL.value):
                address = self.local_bool + self.local_bool_counter
                self.local_bool_counter+=1
                return address

# Reset local variable addresses after done reading function



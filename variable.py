# coding=utf-8
class Variable(dict):
    def __init__(self, var_id, var_type, var_address, var_dim1_dict, var_dim2_dict):
        self.var_id = var_id
        self.var_type = var_type
        self.var_address = var_address
        self.var_dim1_dict = var_dim1_dict 
        self.var_dim2_dict = var_dim2_dict

    # def __getattr__(self, attr):
    #     return self[attr]

    def __str__(self):
        return str(self.__dict__)
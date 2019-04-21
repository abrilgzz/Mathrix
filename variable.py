class Variable(dict):
    def __init__(self, var_id, var_type, var_address):
        self.var_id = var_id
        self.var_type = var_type
        self.var_address = var_address

    def __getattr__(self, attr):
        return self[attr]
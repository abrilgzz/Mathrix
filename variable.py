class Variable(dict):
    def __init__(self, var_ID, var_TYPE):
        self.var_ID = var_ID
        self.var_TYPE = var_TYPE

    def __getattr__(self, attr):
        return self[attr]
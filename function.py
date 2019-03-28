class Function:
    def __init__(self, function_ID, function_TYPE, varsTable):
        self.function_ID = function_ID
        self.function_TYPE = function_TYPE
        self.varsTable = varsTable
    
    def declareVar(self, variable):
        self.varsTable[variable.var_ID] = variable.var_TYPE
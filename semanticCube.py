import numpy as numpy

from constants import Types
from constants import Operations
from constants import Errors

# Create semantic cube:  operation, op1, op2
SemanticCube = numpy.zeros((16,4,4))

def createCube():
    SemanticCube[Operations.PLUS, Types.INT, Types.INT] = Types.INT
    SemanticCube[Operations.PLUS, Types.INT, Types.DOUBLE] = Types.DOUBLE
    SemanticCube[Operations.PLUS, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.PLUS, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.PLUS, Types.DOUBLE, Types.INT] = Types.DOUBLE
    SemanticCube[Operations.PLUS, Types.DOUBLE, Types.DOUBLE] = Types.DOUBLE
    SemanticCube[Operations.PLUS, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.PLUS, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.PLUS, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.PLUS, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.PLUS, Types.BOOL, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.PLUS, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.PLUS, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.PLUS, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.PLUS, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.PLUS, Types.VOID, Types.VOID] = Errors.MISMATCH

    SemanticCube[Operations.MINUS, Types.INT, Types.INT] = Types.INT
    SemanticCube[Operations.MINUS, Types.INT, Types.DOUBLE] = Types.DOUBLE
    SemanticCube[Operations.MINUS, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.MINUS, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.MINUS, Types.DOUBLE, Types.INT] = Types.DOUBLE
    SemanticCube[Operations.MINUS, Types.DOUBLE, Types.DOUBLE] = Types.DOUBLE
    SemanticCube[Operations.MINUS, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.MINUS, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.MINUS, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.MINUS, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.MINUS, Types.BOOL, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.MINUS, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.MINUS, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.MINUS, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.MINUS, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.MINUS, Types.VOID, Types.VOID] = Errors.MISMATCH

    SemanticCube[Operations.DIVIDE, Types.INT, Types.INT] = Types.DOUBLE
    SemanticCube[Operations.DIVIDE, Types.INT, Types.DOUBLE] = Types.DOUBLE
    SemanticCube[Operations.DIVIDE, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.DIVIDE, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.DIVIDE, Types.DOUBLE, Types.INT] = Types.DOUBLE
    SemanticCube[Operations.DIVIDE, Types.DOUBLE, Types.DOUBLE] = Types.DOUBLE
    SemanticCube[Operations.DIVIDE, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.DIVIDE, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.DIVIDE, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.DIVIDE, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.DIVIDE, Types.BOOL, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.DIVIDE, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.DIVIDE, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.DIVIDE, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.DIVIDE, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.DIVIDE, Types.VOID, Types.VOID] = Errors.MISMATCH

    SemanticCube[Operations.MULTIPLY, Types.INT, Types.INT] = Types.INT
    SemanticCube[Operations.MULTIPLY, Types.INT, Types.DOUBLE] = Types.DOUBLE
    SemanticCube[Operations.MULTIPLY, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.MULTIPLY, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.MULTIPLY, Types.DOUBLE, Types.INT] = Types.DOUBLE
    SemanticCube[Operations.MULTIPLY, Types.DOUBLE, Types.DOUBLE] = Types.DOUBLE
    SemanticCube[Operations.MULTIPLY, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.MULTIPLY, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.MULTIPLY, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.MULTIPLY, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.MULTIPLY, Types.BOOL, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.MULTIPLY, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.MULTIPLY, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.MULTIPLY, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.MULTIPLY, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.MULTIPLY, Types.VOID, Types.VOID] = Errors.MISMATCH

    SemanticCube[Operations.ISEQUAL, Types.INT, Types.INT] = Types.BOOL
    SemanticCube[Operations.ISEQUAL, Types.INT, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.ISEQUAL, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.ISEQUAL, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.ISEQUAL, Types.DOUBLE, Types.INT] = Types.BOOL
    SemanticCube[Operations.ISEQUAL, Types.DOUBLE, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.ISEQUAL, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.ISEQUAL, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.ISEQUAL, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.ISEQUAL, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.ISEQUAL, Types.BOOL, Types.BOOL] = Types.BOOL
    SemanticCube[Operations.ISEQUAL, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.ISEQUAL, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.ISEQUAL, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.ISEQUAL, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.ISEQUAL, Types.VOID, Types.VOID] = Errors.MISMATCH

    SemanticCube[Operations.NOTEQUAL, Types.INT, Types.INT] = Types.BOOL
    SemanticCube[Operations.NOTEQUAL, Types.INT, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.NOTEQUAL, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.NOTEQUAL, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.NOTEQUAL, Types.DOUBLE, Types.INT] = Types.BOOL
    SemanticCube[Operations.NOTEQUAL, Types.DOUBLE, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.NOTEQUAL, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.NOTEQUAL, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.NOTEQUAL, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.NOTEQUAL, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.NOTEQUAL, Types.BOOL, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.NOTEQUAL, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.NOTEQUAL, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.NOTEQUAL, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.NOTEQUAL, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.NOTEQUAL, Types.VOID, Types.VOID] = Errors.MISMATCH

    SemanticCube[Operations.GREATERTHAN, Types.INT, Types.INT] = Types.BOOL
    SemanticCube[Operations.GREATERTHAN, Types.INT, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.GREATERTHAN, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHAN, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHAN, Types.DOUBLE, Types.INT] = Types.BOOL
    SemanticCube[Operations.GREATERTHAN, Types.DOUBLE, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.GREATERTHAN, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHAN, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHAN, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHAN, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHAN, Types.BOOL, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHAN, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHAN, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHAN, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHAN, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHAN, Types.VOID, Types.VOID] = Errors.MISMATCH
    

    SemanticCube[Operations.LESSTHAN, Types.INT, Types.INT] = Types.BOOL
    SemanticCube[Operations.LESSTHAN, Types.INT, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.LESSTHAN, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHAN, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHAN, Types.DOUBLE, Types.INT] = Types.BOOL
    SemanticCube[Operations.LESSTHAN, Types.DOUBLE, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.LESSTHAN, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHAN, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHAN, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHAN, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHAN, Types.BOOL, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHAN, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHAN, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHAN, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHAN, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHAN, Types.VOID, Types.VOID] = Errors.MISMATCH

    SemanticCube[Operations.GREATERTHANOREQ, Types.INT, Types.INT] = Types.BOOL
    SemanticCube[Operations.GREATERTHANOREQ, Types.INT, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.GREATERTHANOREQ, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHANOREQ, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHANOREQ, Types.DOUBLE, Types.INT] = Types.BOOL
    SemanticCube[Operations.GREATERTHANOREQ, Types.DOUBLE, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.GREATERTHANOREQ, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHANOREQ, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHANOREQ, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHANOREQ, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHANOREQ, Types.BOOL, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHANOREQ, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHANOREQ, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHANOREQ, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHANOREQ, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.GREATERTHANOREQ, Types.VOID, Types.VOID] = Errors.MISMATCH

    SemanticCube[Operations.LESSTHANOREQ, Types.INT, Types.INT] = Types.BOOL
    SemanticCube[Operations.LESSTHANOREQ, Types.INT, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.LESSTHANOREQ, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHANOREQ, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHANOREQ, Types.DOUBLE, Types.INT] = Types.BOOL
    SemanticCube[Operations.LESSTHANOREQ, Types.DOUBLE, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.LESSTHANOREQ, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHANOREQ, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHANOREQ, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHANOREQ, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHANOREQ, Types.BOOL, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHANOREQ, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHANOREQ, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHANOREQ, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHANOREQ, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.LESSTHANOREQ, Types.VOID, Types.VOID] = Errors.MISMATCH

    SemanticCube[Operations.AND, Types.INT, Types.INT] = Types.BOOL
    SemanticCube[Operations.AND, Types.INT, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.AND, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.AND, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.AND, Types.DOUBLE, Types.INT] = Types.BOOL
    SemanticCube[Operations.AND, Types.DOUBLE, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.AND, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.AND, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.AND, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.AND, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.AND, Types.BOOL, Types.BOOL] = Types.BOOL
    SemanticCube[Operations.AND, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.AND, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.AND, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.AND, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.AND, Types.VOID, Types.VOID] = Errors.MISMATCH

    SemanticCube[Operations.OR, Types.INT, Types.INT] = Types.BOOL
    SemanticCube[Operations.OR, Types.INT, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.OR, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.OR, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.OR, Types.DOUBLE, Types.INT] = Types.BOOL
    SemanticCube[Operations.OR, Types.DOUBLE, Types.DOUBLE] = Types.BOOL
    SemanticCube[Operations.OR, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.OR, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.OR, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.OR, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.OR, Types.BOOL, Types.BOOL] = Types.BOOL
    SemanticCube[Operations.OR, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.OR, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.OR, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.OR, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.OR, Types.VOID, Types.VOID] = Errors.MISMATCH
    

    SemanticCube[Operations.ASSIGN, Types.INT, Types.INT] = Types.INT
    SemanticCube[Operations.ASSIGN, Types.INT, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.ASSIGN, Types.INT, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.ASSIGN, Types.INT, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.ASSIGN, Types.DOUBLE, Types.INT] = Types.DOUBLE
    SemanticCube[Operations.ASSIGN, Types.DOUBLE, Types.DOUBLE] = Types.DOUBLE
    SemanticCube[Operations.ASSIGN, Types.DOUBLE, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.ASSIGN, Types.DOUBLE, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.ASSIGN, Types.BOOL, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.ASSIGN, Types.BOOL, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.ASSIGN, Types.BOOL, Types.BOOL] = Types.VOID
    SemanticCube[Operations.ASSIGN, Types.BOOL, Types.VOID] = Errors.MISMATCH
    SemanticCube[Operations.ASSIGN, Types.VOID, Types.INT] = Errors.MISMATCH
    SemanticCube[Operations.ASSIGN, Types.VOID, Types.DOUBLE] = Errors.MISMATCH
    SemanticCube[Operations.ASSIGN, Types.VOID, Types.BOOL] = Errors.MISMATCH
    SemanticCube[Operations.ASSIGN, Types.VOID, Types.VOID] = Types.VOID

createCube()
    
    




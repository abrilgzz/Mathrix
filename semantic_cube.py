import numpy as numpy

from constants import Types
from constants import Operations
from constants import Errors

# Create semantic cube:  operation, op1, op2
SemanticCube = numpy.zeros((16,4,4))

def createCube():
    SemanticCube[Operations.PLUS.value, Types.INT.value, Types.INT.value] = Types.INT.value
    SemanticCube[Operations.PLUS.value, Types.INT.value, Types.DOUBLE.value] = Types.DOUBLE.value
    SemanticCube[Operations.PLUS.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.PLUS.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.PLUS.value, Types.DOUBLE.value, Types.INT.value] = Types.DOUBLE.value
    SemanticCube[Operations.PLUS.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.DOUBLE.value
    SemanticCube[Operations.PLUS.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.PLUS.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.PLUS.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.PLUS.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.PLUS.value, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.PLUS.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.PLUS.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.PLUS.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.PLUS.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.PLUS.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.MINUS.value, Types.INT.value, Types.INT.value] = Types.INT.value
    SemanticCube[Operations.MINUS.value, Types.INT.value, Types.DOUBLE.value] = Types.DOUBLE.value
    SemanticCube[Operations.MINUS.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MINUS.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MINUS.value, Types.DOUBLE.value, Types.INT.value] = Types.DOUBLE.value
    SemanticCube[Operations.MINUS.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.DOUBLE.value
    SemanticCube[Operations.MINUS.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MINUS.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MINUS.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MINUS.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MINUS.value, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MINUS.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MINUS.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MINUS.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MINUS.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MINUS.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.DIVIDE.value, Types.INT.value, Types.INT.value] = Types.DOUBLE.value
    SemanticCube[Operations.DIVIDE.value, Types.INT.value, Types.DOUBLE.value] = Types.DOUBLE.value
    SemanticCube[Operations.DIVIDE.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.DIVIDE.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.DIVIDE.value, Types.DOUBLE.value, Types.INT.value] = Types.DOUBLE.value
    SemanticCube[Operations.DIVIDE.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.DOUBLE.value
    SemanticCube[Operations.DIVIDE.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.DIVIDE.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.DIVIDE.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.DIVIDE.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.DIVIDE.value, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.DIVIDE.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.DIVIDE.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.DIVIDE.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.DIVIDE.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.DIVIDE.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.MULTIPLY, Types.INT.value, Types.INT.value] = Types.INT.value
    SemanticCube[Operations.MULTIPLY, Types.INT.value, Types.DOUBLE.value] = Types.DOUBLE.value
    SemanticCube[Operations.MULTIPLY, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY, Types.DOUBLE.value, Types.INT.value] = Types.DOUBLE.value
    SemanticCube[Operations.MULTIPLY, Types.DOUBLE.value, Types.DOUBLE.value] = Types.DOUBLE.value
    SemanticCube[Operations.MULTIPLY, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.ISEQUAL, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.ISEQUAL, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.ISEQUAL, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.ISEQUAL, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.ISEQUAL, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL, Types.BOOL.value, Types.BOOL.value] = Types.BOOL.value
    SemanticCube[Operations.ISEQUAL, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.NOTEQUAL, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.NOTEQUAL, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.NOTEQUAL, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.NOTEQUAL, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.NOTEQUAL, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.GREATERTHAN, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHAN, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHAN, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHAN, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHAN, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value
    

    SemanticCube[Operations.LESSTHAN, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHAN, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHAN, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHAN, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHAN, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.GREATERTHANOREQ, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.LESSTHANOREQ, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHANOREQ, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHANOREQ, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHANOREQ, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHANOREQ, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.AND, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.AND, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.AND, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.AND, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.AND, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND, Types.BOOL.value, Types.BOOL.value] = Types.BOOL.value
    SemanticCube[Operations.AND, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.OR, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.OR, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.OR, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.OR, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.OR, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR, Types.BOOL.value, Types.BOOL.value] = Types.BOOL.value
    SemanticCube[Operations.OR, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value
    

    SemanticCube[Operations.ASSIGN.value, Types.INT.value, Types.INT.value] = Types.INT.value
    SemanticCube[Operations.ASSIGN.value, Types.INT.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ASSIGN.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ASSIGN.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ASSIGN.value, Types.DOUBLE.value, Types.INT.value] = Types.DOUBLE.value
    SemanticCube[Operations.ASSIGN.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.DOUBLE.value
    SemanticCube[Operations.ASSIGN.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ASSIGN.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ASSIGN.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ASSIGN.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ASSIGN.value, Types.BOOL.value, Types.BOOL.value] = Types.BOOL.value
    SemanticCube[Operations.ASSIGN.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ASSIGN.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ASSIGN.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ASSIGN.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ASSIGN.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

createCube()
    
    




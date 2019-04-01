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

    SemanticCube[Operations.MULTIPLY.value, Types.INT.value, Types.INT.value] = Types.INT.value
    SemanticCube[Operations.MULTIPLY.value, Types.INT.value, Types.DOUBLE.value] = Types.DOUBLE.value
    SemanticCube[Operations.MULTIPLY.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY.value, Types.DOUBLE.value, Types.INT.value] = Types.DOUBLE.value
    SemanticCube[Operations.MULTIPLY.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.DOUBLE.value
    SemanticCube[Operations.MULTIPLY.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY.value, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.MULTIPLY.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.ISEQUAL.value, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.ISEQUAL.value, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.ISEQUAL.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL.value, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.ISEQUAL.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.ISEQUAL.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL.value, Types.BOOL.value, Types.BOOL.value] = Types.BOOL.value
    SemanticCube[Operations.ISEQUAL.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.ISEQUAL.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.NOTEQUAL.value, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.NOTEQUAL.value, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.NOTEQUAL.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL.value, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.NOTEQUAL.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.NOTEQUAL.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL.value, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.NOTEQUAL.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.GREATERTHAN.value, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHAN.value, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHAN.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN.value, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHAN.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHAN.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN.value, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHAN.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value
    

    SemanticCube[Operations.LESSTHAN.value, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHAN.value, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHAN.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN.value, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHAN.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHAN.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN.value, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHAN.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.GREATERTHANOREQ.value, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.GREATERTHANOREQ.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.LESSTHANOREQ.value, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.BOOL.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.LESSTHANOREQ.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.AND.value, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.AND.value, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.AND.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND.value, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.AND.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.AND.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND.value, Types.BOOL.value, Types.BOOL.value] = Types.BOOL.value
    SemanticCube[Operations.AND.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.AND.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value

    SemanticCube[Operations.OR.value, Types.INT.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.OR.value, Types.INT.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.OR.value, Types.INT.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR.value, Types.INT.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR.value, Types.DOUBLE.value, Types.INT.value] = Types.BOOL.value
    SemanticCube[Operations.OR.value, Types.DOUBLE.value, Types.DOUBLE.value] = Types.BOOL.value
    SemanticCube[Operations.OR.value, Types.DOUBLE.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR.value, Types.DOUBLE.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR.value, Types.BOOL.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR.value, Types.BOOL.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR.value, Types.BOOL.value, Types.BOOL.value] = Types.BOOL.value
    SemanticCube[Operations.OR.value, Types.BOOL.value, Types.VOID.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR.value, Types.VOID.value, Types.INT.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR.value, Types.VOID.value, Types.DOUBLE.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR.value, Types.VOID.value, Types.BOOL.value] = Errors.MISMATCH.value
    SemanticCube[Operations.OR.value, Types.VOID.value, Types.VOID.value] = Errors.MISMATCH.value
    

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
    
    




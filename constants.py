from enum import IntEnum

class Types(IntEnum):
    INT = 0
    DOUBLE = 1
    BOOL = 2
    VOID = 3

class Operations(IntEnum):
    PLUS = 0
    MINUS = 1
    DIVIDE = 2
    MULTIPLY = 3
    ISEQUAL = 4
    NOTEQUAL = 5
    GREATERTHAN = 6
    LESSTHAN = 7
    GREATERTHANOREQ = 8
    LESSTHANOREQ = 9
    AND = 10
    OR = 11
    ASSIGN = 12
    # Parentheses
    LEFT_PAR = 13
    RIGHT_PAR = 14
    # Read, write, return functions
    READ = 15
    WRITE = 16
    RETURN = 17
    # Cycles and conditions operations
    GOTOF = 19
    GOTOT = 20
    GOTO = 21
    # Functions
    PARAM = 22
    GOSUB = 23
    ERA = 24
    ENDPROC = 25
    END = 26
    GLOBALERA = 27
    
    
class Errors(IntEnum):
    MISMATCH = -1

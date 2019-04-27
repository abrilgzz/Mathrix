# -----------------------------------------------------------------------------
# Abril Marina González Ramírez A01280904
# Juan Luis Flores Garza A01280767
# 12/03/2019

# Scanner
# References: https://github.com/dabeaz/ply
# -----------------------------------------------------------------------------
import ply.lex as lex
# -----------------------------------------------------------------------------
# Tokens
# -----------------------------------------------------------------------------
tokens = [
    'ID', 'CTE_I', 'CTE_D', 'CTE_S', 
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
    'IS_EQUAL_TO', 'NOT_EQUAL_TO', 
    'GREATER_THAN', 'LESS_THAN', 
    'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN_OR_EQUAL_TO',
    'AND', 'OR',
    'ASSIGN',
    'LEFT_PAR', 'RIGHT_PAR',
    'LEFT_BRACE', 'RIGHT_BRACE',
    'LEFT_BRACKET', 'RIGHT_BRACKET',
    'SEMICOLON', 'COMMA'
]

# -----------------------------------------------------------------------------
# Dictionary of Reserved words
# -----------------------------------------------------------------------------
reservedWords = {
    'Main': 'MAIN',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'void': 'VOID',
    'int': 'INT',
    'double': 'DOUBLE',
    'bool': 'BOOL',
    'true': 'TRUE',
    'false': 'FALSE',
    'read': 'READ',
    'write': 'WRITE',
    'gotof': 'GOTOF',
    'gotot': 'GOTOT',
    'goto': 'GOTO',
    # Special functions
    'find_determinant': 'FIND_DETERMINANT',
    'transpose_matrix': 'TRANSPOSE_MATRIX',
    'print_matrix': 'PRINT_MATRIX',
    'multiply_matrix': 'MULTIPLY_MATRIX',
    'swap_rows': 'SWAP_ROWS',
    'add_rows': 'ADD_ROWS',
    'multiply_rows': 'MULTIPLY_ROWS',
    'swap_cols': 'SWAP_COLS',
    'add_cols': 'ADD_COLS',
    'multiply_cols': 'MULTIPLY_COLS',
}

tokens = tokens + list(reservedWords.values())

# -----------------------------------------------------------------------------
# Tokens
# -----------------------------------------------------------------------------

# Ignore tabs
t_ignore = " \t"

# Arithmetic Operators
t_PLUS  = r'\+'
t_MINUS  = r'-'
t_MULTIPLY  = r'\*'
t_DIVIDE    = r'/'
# Relational Operators
t_IS_EQUAL_TO  = r'=='
t_NOT_EQUAL_TO  = r'!='
t_GREATER_THAN  = r'>'
t_LESS_THAN  = r'<'
t_GREATER_THAN_OR_EQUAL_TO  = r'>='
t_LESS_THAN_OR_EQUAL_TO  = r'<='
# Logical Operators
t_AND  = r'&&'
t_OR  = r'\|\|'
# Assignment Operator
t_ASSIGN  = r'\='
# Punctuators
t_LEFT_PAR  = r'\('
t_RIGHT_PAR  = r'\)'
t_LEFT_BRACE  = r'{'
t_RIGHT_BRACE  = r'}'
t_LEFT_BRACKET  = r'\['
t_RIGHT_BRACKET  = r'\]'
t_SEMICOLON  = r'\;'
t_COMMA  = r','

# Data Types & ID
def t_ID(t):
    r'[a-zA-Z][_a-zA-Z0-9]*'
    t.type = reservedWords.get(t.value,'ID')
    return t

def t_CTE_D(t):
    r'-?[0-9]*\.[0-9]+'
    t.value = float(t.value)
    return t
    
def t_CTE_I(t):
    r'-?[0-9]+'
    t.value = int(t.value)
    return t



# New lines and errors
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '{}' at: {}".format(t.value[0], t.lexer.lineno))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#### Testing the lexer 
# file = open("example.txt")
# lexer.input(file.read())

# Get tokens
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
# print("\n")


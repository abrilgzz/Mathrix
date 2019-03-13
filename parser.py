# -----------------------------------------------------------------------------
# Abril Marina González Ramírez A01280904
# Juan Luis Flores Garza A01280767
# 12/03/2019

# Parser
# References: https://github.com/dabeaz/ply
# -----------------------------------------------------------------------------

import sys
import ply.yacc as yacc
from scanner import tokens


def p_program(p):
    '''program : PROGRAM MATHRIX COLON program1 main
    '''

# Checar
def p_program1(p):
    '''program1 : program1 function_block
    | program1 vars
    | empty
    '''

# Checar
def p_vars(p):
    '''vars : var_type vars2 SEMICOLON vars3
    '''
    
def p_vars2(p):
    '''vars2 : ID vars3 
    | ID vars4
    '''

def p_vars3(p):
    '''vars3 : ASSIGN var_cte vars5
    '''

def p_vars4(p):
    '''vars4 : LEFT_BRACKET CTE_I RIGHT_BRACKET LEFT_BRACKET CTE_I RIGHT_BRACKET vars2
    | SEMICOLON
    '''

def p_vars5(p):
    '''vars5 : SEMICOLON
    | COMMA vars2
    '''

def p_var_type(p):
    '''var_type : INT
    | DOUBLE
    | BOOL
    | STRING
    '''

def p_var_cte(p):
    '''var_cte : CTE_I
    | CTE_D
    | cte_b
    | CTE_S
    | ID LEFT_BRACKET CTE_I RIGHT_BRACKET LEFT_BRACKET CTE_I RIGHT_BRACKET
    '''

def p_cte_b(p):
    '''cte_b : TRUE
    | FALSE
    '''

# Checar
def p_function_block(p):
    '''function_block : FUNCTION func_type ID LEFT_PAR function_block2 RIGHT_PAR block function_block SEMICOLON
    | empty
    '''

def p_function_block2(p):
    '''function_block2 : var_type ID
    | var_type ID COMMA
    | empty
    '''

def p_func_type(p):
    '''func_type : INT
    | DOUBLE
    | BOOL
    | STRING
    | VOID
    '''

def p_block(p):
    '''block : LEFT_BRACE block2 RIGHT_BRACE
    '''

def p_block2(p):
    '''block2 : block2 vars statement
    | block2 statement
    | empty
    '''

def p_statement(p):
    '''statement : assignment
    | condition
    | call_function
    | return_function
    | while_cycle
    | read
    | write
    '''

def p_assignment(p):
    '''assignment : ID assignment2 expression SEMICOLON
    '''

def p_assignment2(p):
    '''assignment2 : ASSIGN
    | LEFT_BRACKET CTE_I RIGHT_BRACKET LEFT_BRACKET CTE_I RIGHT_BRACKET ASSIGN
    '''

def p_expression(p):
    '''expression : exp expression1
    '''

def p_expression1(p):
    '''expression1 : EQUAL_TO exp
    | NOT_EQUAL_TO exp
    | GREATER_THAN exp
    | LESS_THAN exp
    | GREATER_THAN_OR_EQUAL_TO exp
    | LESS_THAN_OR_EQUAL_TO exp
    | AND exp
    | OR exp
    | empty 
    '''

def p_exp(p):
    '''exp : term exp1
    '''

def p_exp1(p):
    '''exp1 : PLUS exp
    | MINUS exp
    | empty
    '''

def p_term(p):
    '''term : factor term1
    '''

def p_term1(p):
    '''term1 : MULTIPLY term
    | DIVIDE term
    | empty
    '''

def p_factor(p):
    '''factor : LEFT_PAR expression RIGHT_PAR
    | var_cte
    | factor1 var_cte
    '''

def p_factor1(p):
    '''factor1 : PLUS
    | MINUS
    | empty
    '''

def p_condition(p):
    '''condition : IF LEFT_PAR expression RIGHT_PAR block condition2
    '''

def p_condition2(p):
    '''condition2 : ELSE block
    '''

def p_call_function(p):
    '''call_function : ID LEFT_PAR call_function2 RIGHT_PAR SEMICOLON
    '''

def p_call_function2(p):
    '''call_function2 : ID call_function3
    | exp call_function3
    '''

def p_call_function3(p):
    '''call_function3 : COMMA call_function2
    | empty
    '''

def p_return_function(p):
    '''return_function : RETURN exp SEMICOLON
    '''

def p_while_cycle(p):
    '''while_cycle : WHILE LEFT_BRACE exp RIGHT_BRACE block
    '''

def p_read(p):
    '''read : READ LEFT_PAR exp RIGHT_PAR SEMICOLON
    '''

def p_write(p):
    '''write : WRITE LEFT_PAR exp RIGHT_PAR SEMICOLON
    '''

def p_main(p):
    '''main : MAIN block SEMICOLON
    '''

def p_empty(p):
	'''empty :
    '''
	pass

def p_error(p):
    print("Error")

parser_Mathrix = yacc.yacc()

while True:
    try:
        s = input('mathrix > ')   # usar input()
    except EOFError:
        break
    parser_Mathrix.parse(s)
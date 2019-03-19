# -----------------------------------------------------------------------------
# Abril Marina González Ramírez A01280904
# Juan Luis Flores Garza A01280767
# 18/03/2019

# Parser
# References: https://github.com/dabeaz/ply
# -----------------------------------------------------------------------------

import sys
import ply.yacc as yacc
from scanner import tokens


def p_start(p):
    '''start : global_declaration
    '''
    print('COMPILED')

def p_global_declaration(p):
    '''global_declaration : var_declaration global_declaration
    | func_declaration
    '''

# Variable declaration
def p_var_declaration(p):
    '''var_declaration : var_type ID array SEMICOLON
    | empty
    '''

def p_array(p):
    '''array : LEFT_BRACKET expression RIGHT_BRACKET array
    | empty
    '''

# Function declaration
def p_func_declaration(p):
    '''func_declaration : func_signature func_declaration
    | main
    '''

#Example function int [2][3] testFunction(int Y)
def p_func_signature(p):
    '''func_signature : FUNCTION func_type array func_signature_1
    '''

def p_func_signature_1(p):
    '''func_signature_1 : ID LEFT_PAR param_declaration RIGHT_PAR block
    '''

def p_param_declaration(p):
    '''param_declaration : var_type array ID param_declaration_1
    | empty
    '''

def p_param_declaration_1(p):
    '''param_declaration_1 : COMMA var_type array ID param_declaration_1
    | empty
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
    | ID array
    | function_call
    '''

def p_cte_b(p):
    '''cte_b : TRUE
    | FALSE
    '''

def p_func_type(p):
    '''func_type : INT
    | DOUBLE
    | BOOL
    | STRING
    | VOID
    '''

def p_block(p):
    '''block : LEFT_BRACE block_1 
    '''

def p_block_1(p):
    '''block_1 : statement block_1
    | block_2 
    '''

# Added RETURN to block's grammar; values can be returned at any point within block
def p_block_2(p):
    '''block_2 : RETURN expression SEMICOLON block_3
    | block_3
    '''

def p_block_3(p):
    '''block_3 : RIGHT_BRACE
    '''

# function_call example: x = function1() + function2();
def p_statement(p):
    '''statement : var_declaration
    | assignment
    | condition
    | function_call SEMICOLON
    | while_cycle
    | read
    | write
    '''

def p_assignment(p):
    '''assignment : var_type ID ASSIGN expression SEMICOLON
    '''


def p_expression(p):
    '''expression : exp expression_1
    '''

def p_expression_1(p):
    '''expression_1 : IS_EQUAL_TO exp
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
    '''exp : term exp_1
    '''

def p_exp_1(p):
    '''exp_1 : PLUS exp
    | MINUS exp
    | empty
    '''

def p_term(p):
    '''term : factor term_1
    '''

def p_term_1(p):
    '''term_1 : MULTIPLY term
    | DIVIDE term
    | empty
    '''

def p_factor(p):
    '''factor : LEFT_PAR expression RIGHT_PAR
    | var_cte
    | factor_1 var_cte
    '''

def p_factor_1(p):
    '''factor_1 : PLUS
    | MINUS
    | empty
    '''

def p_condition(p):
    '''condition : IF LEFT_PAR expression RIGHT_PAR block condition_1
    '''

def p_condition_1(p):
    '''condition_1 : ELSE block
    | empty
    '''

def p_function_call(p):
    '''function_call : ID LEFT_PAR param_call RIGHT_PAR 
    '''

def p_param_call(p):
    '''param_call : expression param_call_1
    '''

def p_param_call_1(p):
    '''param_call_1 : COMMA param_call_1
    | empty
    '''

def p_while_cycle(p):
    '''while_cycle : WHILE LEFT_PAR expression RIGHT_PAR block
    '''

def p_read(p):
    '''read : READ LEFT_PAR exp RIGHT_PAR SEMICOLON
    '''

def p_write(p):
    '''write : WRITE LEFT_PAR exp RIGHT_PAR SEMICOLON
    '''

def p_main(p):
    '''main : MAIN block 
    '''

def p_empty(p):
	'''empty :
    '''
	pass

def p_error(p):
    print("Syntax error")
    print("Unexpected {} at line {}".format(p.value, p.lexer.lineno))
    sys.exit()

parser_Mathrix = yacc.yacc()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        
        file = sys.argv[1]
        try:
            f = open(file,'r')
            data = f.read()
            f.close()

            parser_Mathrix.parse(data)
        except EOFError:
            print(EOFError)
    else:
        print("No file to test found")

# while True:
#     try:
#         s = input('mathrix > ')   # usar input()
#     except EOFError:
#         break
#     parser_Mathrix.parse(s)
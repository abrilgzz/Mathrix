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

from constants import Types
from constants import Operations
from constants import Errors

from semantic_cube import SemanticCube

from functions_table import Function
from functions_table import Variable
from functions_table import FunctionsTable

from quads import *

functions_directory = FunctionsTable()

# Global function
Mathrix = Function('Mathrix', Types.VOID, {})
functions_directory._functions['Mathrix'] = Mathrix

current_function = functions_directory._functions['Mathrix']
current_type = Types.VOID

operators_stack = []
operands_stack = []
types_stack = []

quadruples_list = []
temp_counter = 0


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
    '''var_declaration : var_type ID sem_add_var array SEMICOLON
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

#Example function int[2][3] testFunction(int Y)
def p_func_signature(p):
    '''func_signature : FUNCTION func_type array func_signature_1 sem_end_func
    '''

def p_func_signature_1(p):
    '''func_signature_1 : ID sem_add_func LEFT_PAR param_declaration RIGHT_PAR block
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
    '''var_type : INT sem_get_type
    | DOUBLE sem_get_type
    | BOOL sem_get_type
    '''

def p_var_cte(p):
    '''var_cte : CTE_I sem_push_constant_int
    | CTE_D sem_push_constant_double
    | cte_b
    | ID sem_push_operand array 
    | function_call
    '''

def p_cte_b(p):
    '''cte_b : TRUE
    | FALSE
    '''

def p_func_type(p):
    '''func_type : INT sem_get_type
    | DOUBLE sem_get_type
    | BOOL sem_get_type
    | VOID sem_get_type
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
    '''assignment : ID sem_push_operand ASSIGN sem_push_operator expression sem_assign_value SEMICOLON
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
    '''exp : term sem_top_term exp_1
    '''

def p_exp_1(p):
    '''exp_1 : PLUS sem_push_operator exp
    | MINUS sem_push_operator exp
    | empty
    '''

def p_term(p):
    '''term : factor sem_top_factor term_1
    '''

def p_term_1(p):
    '''term_1 : MULTIPLY sem_push_operator term
    | DIVIDE sem_push_operator term
    | empty
    '''

def p_factor(p):
    '''factor : LEFT_PAR sem_false_bottom_begin expression RIGHT_PAR sem_false_bottom_end
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
    | empty
    '''

def p_param_call_1(p):
    '''param_call_1 : COMMA param_call
    | empty
    '''

def p_while_cycle(p):
    '''while_cycle : WHILE LEFT_PAR expression RIGHT_PAR block
    '''

def p_read(p):
    '''read : READ sem_push_operator LEFT_PAR exp RIGHT_PAR sem_read_write SEMICOLON
    '''

def p_write(p):
    '''write : WRITE sem_push_operator LEFT_PAR exp RIGHT_PAR SEMICOLON
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

# -----------------------------------------------------------------------------
#   SEMANTIC RULES
# -----------------------------------------------------------------------------
 
def p_sem_get_type(p):
    '''sem_get_type : empty
    '''
    global current_type
    t = p[-1]
    if t == 'int':
        current_type = Types.INT.value
    elif t == 'double':
        current_type = Types.DOUBLE.value
    elif t == 'bool':
        current_type = Types.BOOL.value
    elif t == 'void':
        current_type = Types.VOID.value
    else:
        pass

def p_sem_add_func(p):
    '''sem_add_func : empty
    '''
    global current_function
    function_id = p[-1]
    
    f = Function(function_id, current_type, {})
    functions_directory.add_function(f)
    current_function = f
    #print(functions_directory)

def p_sem_end_func(p):
    '''sem_end_func : empty
    '''
    global functions_directory
    functions_directory._functions[current_function.function_id].variables_directory.clear()
    #print(functions_directory)

def p_sem_add_var(p):
    '''sem_add_var : empty
    '''
    v = Variable(p[-1], current_type)
    #print(p[-1])

    global functions_directory, current_function
    functions_directory.add_variable(v, current_function)
    # print(functions_directory._functions[current_function.function_id].variables_directory)


def p_sem_push_operator(p):
    '''sem_push_operator : empty
    '''
    operator = p[-1]
    operator_number = -1

    if operator == '+':
        operator_number = Operations.PLUS.value
    elif operator == '-':
        operator_number = Operations.MINUS.value
    elif operator == '*':
        operator_number = Operations.MULTIPLY.value
    elif operator == '/':
        operator_number = Operations.DIVIDE.value
    elif operator == '==':
        operator_number = Operations.ISEQUAL.value
    elif operator == '!=':
        operator_number = Operations.NOTEQUAL.value
    elif operator == '>':
        operator_number = Operations.GREATERTHAN.value
    elif operator == '<':
        operator_number = Operations.LESSTHAN.value
    elif operator == '>=':
        operator_number = Operations.GREATERTHANOREQ.value
    elif operator == '<=':
        operator_number = Operations.LESSTHANOREQ.value
    elif operator == '&&':
        operator_number = Operations.AND.value
    elif operator == '||':
        operator_number = Operations.OR.value
    elif operator == '=':
        operator_number = Operations.ASSIGN.value
        
    operators_stack.append(operator_number)
    # print(operator, " was pushed to operators stack with number: ", operator_number)

def p_sem_push_operand(p):
    '''sem_push_operand : empty
    '''
    operand = p[-1]
    operands_stack.append(operand)
    # print(operand, " was pushed to operands stack")

    # Check if variable/operand is declared and get its type
    variable_type = functions_directory.find_variable(operand)
    types_stack.append(variable_type)
    # print(variable_type, " was pushed to types stack")

def p_sem_push_constant_int(p):
    '''sem_push_constant_int : empty
    '''
    constant = p[-1]
    operands_stack.append(constant)
    types_stack.append(Types.INT.value)

def p_sem_push_constant_double(p):
    '''sem_push_constant_double : empty
    '''
    constant = p[-1]
    operands_stack.append(constant)
    types_stack.append(Types.DOUBLE.value)

def p_sem_top_factor(p):
    '''sem_top_factor : empty
    '''
    global temp_counter

    # Multiplication or division of factors
    if (operators_stack[-1:]):  # Check that top of stack exists
        if (operators_stack[-1] == Operations.MULTIPLY.value or operators_stack[-1] == Operations.DIVIDE.value):
            q = create_quad(temp_counter, operators_stack, operands_stack, types_stack)
            quadruples_list.append(q)
            temp_counter+=1

def p_sem_top_term(p):
    '''sem_top_term : empty
    '''
    global temp_counter

    # Addition or substraction of terms
    if (operators_stack[-1:]):  # Check that top of stack exists
        if (operators_stack[-1] == Operations.PLUS.value or operators_stack[-1] == Operations.MINUS.value):
            q = create_quad(temp_counter, operators_stack, operands_stack, types_stack)
            quadruples_list.append(q)
            temp_counter+=1

def p_sem_false_bottom_begin(p):
    '''sem_false_bottom_begin : empty
    '''
    operators_stack.append(Operations.LEFT_PAR.value)

def p_sem_false_bottom_end(p):
    '''sem_false_bottom_end : empty
    '''
    operators_stack.pop()

def p_sem_assign_value(p):
    '''sem_assign_value : empty
    '''
    q = assignment_quad(operators_stack, operands_stack, types_stack)
    quadruples_list.append(q)

def p_sem_read_write(p):
    '''sem_read_write : empty
    '''
    q = read_write_quad(operators_stack, operands_stack)
    quadruples_list.append(q)

parser_Mathrix = yacc.yacc()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        
        file = sys.argv[1]
        try:
            f = open(file,'r')
            data = f.read()
            f.close()

            parser_Mathrix.parse(data)
            print_quads(quadruples_list)
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





    


        

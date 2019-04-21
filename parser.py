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

from memory import Memory

from quads import *

functions_directory = FunctionsTable()
memory = Memory()

# Global function
Mathrix = Function('Mathrix', Types.VOID, {}, [], 0)
functions_directory._functions['Mathrix'] = Mathrix

current_function = functions_directory._functions['Mathrix']
current_type = Types.VOID

operators_stack = []
operands_stack = []
types_stack = []
jumps_stack = []

quadruples_list = []
temp_counter = 0

parameter_counter = 0

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
    '''array : LEFT_BRACKET mega_exp RIGHT_BRACKET array
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
    '''param_declaration : var_type array ID sem_add_param
    | var_type array ID sem_add_param COMMA param_declaration
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
    '''block_2 : RETURN sem_push_operator mega_exp sem_return_function SEMICOLON block_3
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
    '''assignment : ID sem_push_operand ASSIGN sem_push_operator mega_exp sem_assign_value SEMICOLON
    '''

def p_mega_exp(p):
    '''mega_exp : hyper_exp mega_exp_1
    '''
# Logical operators
def p_mega_exp_1(p):
    '''mega_exp_1 : AND sem_push_operator mega_exp sem_top_logical
    | OR sem_push_operator mega_exp sem_top_logical
    | empty
    '''

def p_hyper_exp(p):
    '''hyper_exp : exp hyper_exp_1 
    '''

# Relational operators
def p_hyper_exp_1(p):
    '''hyper_exp_1 : IS_EQUAL_TO sem_push_operator exp sem_top_relational
    | NOT_EQUAL_TO sem_push_operator exp sem_top_relational
    | GREATER_THAN sem_push_operator exp sem_top_relational
    | LESS_THAN sem_push_operator exp sem_top_relational
    | GREATER_THAN_OR_EQUAL_TO sem_push_operator exp sem_top_relational
    | LESS_THAN_OR_EQUAL_TO sem_push_operator exp sem_top_relational
    | empty 
    '''

def p_exp(p):
    '''exp : term sem_top_term exp_1 
    '''

# Arithmetic operators
def p_exp_1(p):
    '''exp_1 : PLUS sem_push_operator exp
    | MINUS sem_push_operator exp
    | empty
    '''

def p_term(p):
    '''term : factor sem_top_factor term_1
    '''

# Arithmetic operators
def p_term_1(p):
    '''term_1 : MULTIPLY sem_push_operator term
    | DIVIDE sem_push_operator term
    | empty
    '''

def p_factor(p):
    '''factor : LEFT_PAR sem_false_bottom_begin mega_exp RIGHT_PAR sem_false_bottom_end
    | var_cte 
    | factor_1 var_cte
    '''

def p_factor_1(p):
    '''factor_1 : PLUS
    | MINUS
    | empty
    '''

def p_condition(p):
    '''condition : IF LEFT_PAR mega_exp RIGHT_PAR sem_end_condition block condition_1 sem_fill_goto
    '''

def p_condition_1(p):
    '''condition_1 : ELSE sem_else_condition block
    | empty
    '''

def p_function_call(p):
    '''function_call : ID sem_check_function LEFT_PAR sem_create_era param_call RIGHT_PAR sem_count_params sem_gosub
    '''

def p_param_call(p):
    '''param_call : mega_exp sem_check_param 
    | mega_exp sem_check_param COMMA param_call
    | empty
    '''

def p_while_cycle(p):
    '''while_cycle : WHILE sem_start_while LEFT_PAR mega_exp RIGHT_PAR sem_end_condition block sem_end_while
    '''

def p_read(p):
    '''read : READ sem_push_operator LEFT_PAR exp RIGHT_PAR sem_read_write SEMICOLON
    '''

def p_write(p):
    '''write : WRITE sem_push_operator LEFT_PAR exp RIGHT_PAR sem_read_write SEMICOLON
    '''

def p_main(p):
    '''main : MAIN  block 
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
    global current_function, temp_counter
    function_id = p[-1]
    
    f = Function(function_id, current_type, {}, [], temp_counter)
    functions_directory.add_function(f)
    current_function = f
    #print(functions_directory)

def p_sem_end_func(p):
    '''sem_end_func : empty
    '''
    global functions_directory, temp_counter
    # Release the current variables table
    functions_directory._functions[current_function.function_id].variables_directory.clear()
    # Generate an action to end the procedure
    q = define_quad (Operations.ENDPROC.value, -1, -1, -1)
    quadruples_list.append(q)
    temp_counter+=1
    #print(functions_directory)

def p_sem_add_var(p):
    '''sem_add_var : empty
    '''
    global current_function, functions_directory

    v = Variable(p[-1], current_type, -1)
    v.var_address = memory.set_address(v, current_function.function_id)

    # print(v.var_id, v.var_type, v.var_address)
    # print(p[-1])

    functions_directory.add_variable(v, current_function)
    #print(functions_directory._functions[current_function.function_id].variables_directory)


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
    elif operator == 'read':
        operator_number = Operations.READ.value
    elif operator == 'write':
        operator_number = Operations.WRITE.value
    elif operator == 'return':
        operator_number = Operations.RETURN.value
    elif operator == 'gotof':
        operator_number = Operations.GOTOF.value
    elif operator == 'gotot':
        operator_number = Operations.GOTOT.value
    elif operator == 'goto':
        operator_number = Operations.GOTO.value
        
    operators_stack.append(operator_number)
    # print(operator, " was pushed to operators stack with number: ", operator_number)

def p_sem_push_operand(p):
    '''sem_push_operand : empty
    '''
    operand = p[-1]
    # Check if variable/operand is declared and get its type
    variable_type = functions_directory.find_variable(operand)
    operands_stack.append(operand)
    # print(operand, " was pushed to operands stack")
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
    q = one_operation_quad(operators_stack, operands_stack)
    quadruples_list.append(q)

def p_sem_return_function(p):
    '''sem_return_function : empty
    '''
    q = one_operation_quad(operators_stack, operands_stack)
    quadruples_list.append(q)

# Expressions
def p_sem_top_logical(p):
    '''sem_top_logical : 
    '''
    global temp_counter

    if(operators_stack[-1:]):
        if (operators_stack[-1] == Operations.AND.value or operators_stack[-1] == Operations.OR.value):
            q = create_quad(temp_counter, operators_stack, operands_stack, types_stack)
            quadruples_list.append(q)
            temp_counter+=1

def p_sem_top_relational(p):
    '''sem_top_relational : 
    '''
    global temp_counter

    if(operators_stack[-1:]):
        if (operators_stack[-1] == Operations.GREATERTHAN.value or operators_stack[-1] == Operations.LESSTHAN.value
        or operators_stack[-1] == Operations.GREATERTHANOREQ.value or operators_stack[-1] == Operations.LESSTHANOREQ.values):
            q = create_quad(temp_counter, operators_stack, operands_stack, types_stack)
            quadruples_list.append(q)
            temp_counter+=1

# Conditions and cycles
def p_sem_end_condition(p):
    '''sem_end_condition : empty
    '''
    global temp_counter
    if (operands_stack[-1:]):
        q = create_GOTOF_quad(operands_stack, types_stack)
        quadruples_list.append(q)
        temp_counter+=1
        jumps_stack.append(temp_counter-1)

def p_sem_fill_goto(p):
    '''sem_fill_goto : empty
    '''
    global temp_counter
    end = jumps_stack.pop()
    fill(quadruples_list, end, temp_counter)

def p_sem_else_condition(p):
    '''sem_else_condition : empty
    '''
    global temp_counter

    if (operands_stack[-1:]):
        q = create_GOTO_quad(types_stack)
        quadruples_list.append(q)
        temp_counter+=1
        false = jumps_stack.pop()
        jumps_stack.append(temp_counter-1)
        fill(quadruples_list, false, temp_counter)

def p_sem_start_while(p):
    '''sem_start_while : empty
    '''
    global temp_counter
    jumps_stack.append(temp_counter)

def p_sem_end_while(p):
    '''sem_end_while : empty
    '''
    global temp_counter
    end = jumps_stack.pop()
    ret = jumps_stack.pop()

    q = define_quad(Operations.GOTO.value, -1, -1, ret) 
    quadruples_list.append(q)
    temp_counter+=1
    fill(quadruples_list, end, temp_counter)

# Functions
def p_sem_add_param(p):
    '''sem_add_param : empty
    '''
    variable_address = 0
    v = Variable(p[-1], current_type, variable_address)
    #print(p[-1])

    global functions_directory, current_function
    # Parameter = local variable
    functions_directory.add_variable(v, current_function)
    functions_directory.add_param(v, current_function)

def p_sem_check_function(p):
    '''sem_check_function : empty
    '''
    function_name = p[-1]

    global functions_directory, current_function
    # Verify that the function exists in functions directory
    current_function = functions_directory.find_function(function_name)

def p_sem_create_era(p):
    '''sem_create_era : empty
    '''
    global temp_counter, current_function, parameter_counter
    # Start the parameter counter in 0
    parameter_counter = 0
    # Get how many parameters of each type the function has
    local_ints = current_function.params_list.count(Types.INT.value)
    local_doubles = current_function.params_list.count(Types.DOUBLE.value)
    local_bools = current_function.params_list.count(Types.BOOL.value)
    # print("ints: ", local_ints, " doubles: ", local_doubles, " bools: ", local_bools)

    # Generate action ERA size

    #Create quad
    q = define_quad(Operations.ERA.value, current_function.function_id, -1, -1) 
    quadruples_list.append(q)
    temp_counter+=1

def p_sem_check_param(p):
    '''sem_check_param : empty
    '''
    global temp_counter, parameter_counter, current_function

    argument = operands_stack.pop()
    argument_type = types_stack.pop()
    
    if(parameter_counter >= len(current_function.params_list)):
        print("Error, invalid number of parameters.")
        exit(1)

    if (len(current_function.params_list) > 0):
        # Verify argument type against current parameter
        current_param_type = current_function.params_list[parameter_counter]

        if(argument_type == current_param_type):
            # Generate PARAM quad
            q = define_quad(Operations.PARAM.value, argument, -1, "param #" + str(parameter_counter))
            quadruples_list.append(q)
            temp_counter+=1
            parameter_counter+=1
        else:
            print("Error, invalid parameter type: {}, expecting: {}".format(argument_type, current_param_type))
            exit(1)

def p_sem_count_params(p):
    '''sem_count_params : empty
    '''
    global parameter_counter

    total_parameters = len(current_function.params_list)

    # Coherence in number of parameters
    if (total_parameters != parameter_counter):
        print("Error, invalid number of parameters.")
        exit(1)

def p_sem_gosub(p):
    '''sem_gosub : empty
    '''
    global temp_counter

    # Generate GOSUB quad
    q = define_quad(Operations.GOSUB.value, current_function.function_id, -1, current_function.start_address)
    quadruples_list.append(q)
    temp_counter+=1



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
            print("# of quads: ", temp_counter+1)

        except EOFError:
            print(EOFError)
    else:
        print("No file to test found")

# while True:
#     try:
#         s = input('mathrix > ')   # use input()
#     except EOFError:
#         break
#     parser_Mathrix.parse(s)





    


        

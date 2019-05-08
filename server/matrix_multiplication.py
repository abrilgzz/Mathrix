#!C:\Users\jluis\AppData\Local\Programs\Python\Python37\python.exe
# coding=utf-8
import cgi
import cgitb; cgitb.enable()
import sys
import ply.yacc as yacc

from scanner import tokens

from constants import *

from semantic_cube import SemanticCube

from functions_table import *

from memory import Memory

from quads import *

from vm import *

functions_directory = FunctionsTable()
memory = Memory()
# Global function
# Mathrix = Function('Mathrix', Types.VOID.value, {}, [], 0)
# functions_directory._functions['Mathrix'] = Mathrix

# current_function = functions_directory._functions['Mathrix']
# current_type = Types.VOID

operators_stack = []
operands_stack = []
types_stack = []
jumps_stack = []

quadruples_list = []
quad_counter = 0
temp_counter = 0

parameter_counter = 0

function_stack = []
era_stack = []

temporal_variables = {}
dimension_stack = []
dimension_counter = 0

matrix = []
row = []

def p_start(p):
    '''start : sem_start_program declaration func_declaration
    '''
    print('COMPILED')


def p_declaration(p):
    '''declaration : var_declaration declaration
    | matrix_declaration declaration
    | empty
    '''

# Variable declaration
def p_var_declaration(p):
    '''var_declaration : var_type ID sem_add_var SEMICOLON 
    '''

# Matrix declaration
def p_matrix_declaration(p):
    '''matrix_declaration : MATRIX var_type ID sem_get_matrix_id LEFT_BRACKET CTE_I sem_get_dim1 RIGHT_BRACKET LEFT_BRACKET CTE_I sem_get_dim2 RIGHT_BRACKET sem_add_matrix SEMICOLON
    '''

def p_matrix(p):
    '''matrix : LEFT_BRACKET sem_check_dim1 exp RIGHT_BRACKET sem_ver_dim1 LEFT_BRACKET sem_check_dim2 exp RIGHT_BRACKET sem_ver_dim2
    | empty
    '''

# Function declaration
def p_func_declaration(p):
    '''func_declaration : func_signature func_declaration
    | main
    '''

# TODO: check func signature and param declaration
def p_func_signature(p):
    '''func_signature : FUNCTION func_type func_signature_1 sem_end_func
    '''

def p_func_signature_1(p):
    '''func_signature_1 : ID sem_add_func LEFT_PAR param_declaration RIGHT_PAR block
    '''

def p_param_declaration(p):
    '''param_declaration : var_type ID sem_add_param
    | var_type ID sem_add_param COMMA param_declaration
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
    | cte_b sem_push_constant_bool
    | ID sem_push_operand matrix 
    | ID sem_check_function LEFT_PAR sem_false_bottom_begin sem_create_era param_call RIGHT_PAR sem_false_bottom_end sem_count_params sem_gosub 
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
    '''block : LEFT_BRACE declaration statements RIGHT_BRACE
    '''

def p_statements(p):
    '''statements : statement statements
    | empty
    '''

def p_statement(p):
    '''statement : var_assignment
    | matrix_assignment
    | condition
    | return
    | function_call  
    | while_cycle
    | read
    | write
    '''

def p_var_assignment(p):
    '''var_assignment : ID sem_push_operand matrix ASSIGN sem_push_operator mega_exp sem_assign_value SEMICOLON
    '''

def p_matrix_assignment(p):
    '''matrix_assignment : MATRIX ID sem_push_operand ASSIGN sem_push_operator matrix_construct sem_assign_matrix SEMICOLON
    '''

def p_matrix_construct(p):
    '''matrix_construct : LEFT_BRACE rows RIGHT_BRACE
    '''

def p_rows(p):
    '''rows : row
    | row COMMA rows
    '''

def p_row(p):
    '''row : LEFT_BRACKET col RIGHT_BRACKET sem_push_row sem_clear_row
    '''

def p_col(p):
    '''col : CTE_I sem_push_col col
    | CTE_B sem_push_col col
    | COMMA col
    | empty
    '''

def p_return(p):
    '''return : RETURN mega_exp sem_return_function SEMICOLON
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

# Arithmetic operators
def p_exp(p):
    '''exp : term sem_top_term
    | term sem_top_term PLUS sem_push_operator exp
    | term sem_top_term MINUS sem_push_operator exp
    '''
    
# Arithmetic operators
def p_term(p):
    '''term : factor sem_top_factor
    | factor sem_top_factor MULTIPLY sem_push_operator term
    | factor sem_top_factor DIVIDE sem_push_operator term
    '''


def p_factor(p):
    '''factor : LEFT_PAR sem_false_bottom_begin mega_exp RIGHT_PAR sem_false_bottom_end
    | var_cte 
    | PLUS sem_push_operator var_cte
    | MINUS sem_push_operator var_cte
    '''


def p_condition(p):
    '''condition : IF LEFT_PAR mega_exp RIGHT_PAR sem_end_condition block condition_1 sem_fill_gotof
    '''

def p_condition_1(p):
    '''condition_1 : ELSE sem_else_condition block
    | empty
    '''

def p_function_call(p):
    '''function_call : ID sem_check_function LEFT_PAR sem_create_era param_call RIGHT_PAR sem_count_params SEMICOLON sem_gosub
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
    '''read : READ sem_push_operator LEFT_PAR mega_exp RIGHT_PAR sem_read_write SEMICOLON
    '''

def p_write(p):
    '''write : WRITE sem_push_operator LEFT_PAR mega_exp RIGHT_PAR sem_read_write SEMICOLON
    '''

def p_main(p):
    '''main : MAIN sem_fill_goto_main block sem_fill_eras sem_end_main
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
    global current_function, quad_counter, temporal_variables
    function_id = p[-1]
    
    
    f = Function(function_id, current_type, {}, [], quad_counter, 0, 0, 0)
    functions_directory.add_function(f)
    current_function = f

    temporal_variables[current_function.function_id] = {}
    temporal_variables[current_function.function_id][Types.INT.value] = 0
    temporal_variables[current_function.function_id][Types.DOUBLE.value] = 0
    temporal_variables[current_function.function_id][Types.BOOL.value] = 0
    #print(functions_directory)

def p_sem_end_func(p):
    '''sem_end_func : empty
    '''
    global functions_directory, quad_counter, memory, temp_counter, function_stack, era_stack
    # print("Vars table for ", current_function.function_id, " at the end of the f.")
    # print("vars counter: ", len(current_function.variables_directory))
    # print("temp_counter: ", temp_counter)
    # print(functions_directory._functions[current_function.function_id].variables_directory)

    local_vars = len(current_function.variables_directory)
    function_size = local_vars + temp_counter
    current_function.size = function_size

    ints = 0
    doubles = 0
    bools = 0

    for v in current_function.variables_directory:
        variable = current_function.variables_directory[v]
        if variable.var_type == Types.INT.value:
            ints = ints + 1
        elif variable.var_type == Types.DOUBLE.value:
            doubles = doubles + 1
        elif variable.var_type == Types.BOOL.value:
            bools = doubles +1

    # Store how many vars & temps this function has
    current_function.ints = ints
    current_function.doubles = doubles
    current_function.bools = bools

    #print("current function: ", current_function.function_id, "ints: ", current_function.ints, "double: ", current_function.doubles, "bools: ", current_function.bools)

    # Release the current variables table
    functions_directory._functions[current_function.function_id].variables_directory.clear()
    
    # Generate an action to end the procedure
    q = define_quad (Operations.ENDPROC.value, -1, -1, -1)
    quadruples_list.append(q)
    quad_counter+=1
    #print(functions_directory)

    # Clear memory addresses for local variables
    temp_counter = 0
    memory.clear_local_temp_addresses()

    function_stack.clear()

def p_sem_add_var(p):
    '''sem_add_var : empty
    '''
    global current_function, functions_directory, memory

    v = Variable(p[-1], current_type, -1, 0, 0)
    # print("current_function: ", current_function)
    # print(p[-1])

    functions_directory.add_variable(v, current_function, memory)
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
    global var_memory_address

    operand = p[-1]
    # Check if variable/operand is declared and get its type
    variable = functions_directory.find_variable(operand, current_function.function_id)
    var_type = variable.var_type

    # Add variable's memory address to the operands stack
    var_memory_address = functions_directory.find_var_address(operand, current_function.function_id)
    operands_stack.append(var_memory_address)

    # print(operand, " was pushed to operands stack")
    types_stack.append(var_type)
    # print(var_type, " was pushed to types stack")

def p_sem_push_constant_int(p):
    '''sem_push_constant_int : empty
    '''
    constant = p[-1]

    types_stack.append(Types.INT.value)

    constant_int = "#" + str(constant)
    constant_int_var = Variable(constant_int, Types.INT.value, -1, 0, 0)
    
    if functions_directory.find_constant(constant_int_var):
        # print("Constant ", constant_int_var.var_id, " was found again")
        constant_int_var.var_address = functions_directory.find_var_address(constant_int_var.var_id, "Mathrix")
    else:
        # Add constants to global variables
        constant_int_var.var_address = memory.set_cte_address(constant_int_var)
        functions_directory.add_constant(constant_int_var)
        
    operands_stack.append(constant_int_var.var_address)


def p_sem_push_constant_double(p):
    '''sem_push_constant_double : empty
    '''
    constant = p[-1]
    
    types_stack.append(Types.DOUBLE.value)

    constant_double = "#" + str(constant)
    constant_double_var = Variable(constant_double, Types.DOUBLE.value, -1, 0, 0)

    if functions_directory.find_constant(constant_double_var):
        # print("Constant ", constant_double_var.var_id, " was found again")
        constant_double_var.var_address = functions_directory.find_var_address(constant_double_var.var_id, "Mathrix")
    else:
        # Add constants to global variables
        constant_double_var.var_address = memory.set_cte_address(constant_double_var)
        functions_directory.add_constant(constant_double_var)

    operands_stack.append(constant_double_var.var_address)

def p_sem_push_constant_bool(p):
    '''sem_push_constant_bool : empty
    '''
    constant = p[-1]
    operands_stack.append(constant)
    types_stack.append(Types.BOOL.value)

def p_sem_top_factor(p):
    '''sem_top_factor : empty
    '''
    global quad_counter, temp_counter, current_function, temporal_variables

    # Multiplication or division of factors
    if (operators_stack[-1:]):  # Check that top of stack exists
        if (operators_stack[-1] == Operations.MULTIPLY.value or operators_stack[-1] == Operations.DIVIDE.value):
            q = create_quad(quad_counter, operators_stack, operands_stack, types_stack, temp_counter, memory, current_function, temporal_variables)
            quadruples_list.append(q)
            quad_counter+=1
            temp_counter+=1

def p_sem_top_term(p):
    '''sem_top_term : empty
    '''
    global quad_counter, temp_counter, current_function, temporal_variables

    # Addition or substraction of terms
    if (operators_stack[-1:]):  # Check that top of stack exists
        if (operators_stack[-1] == Operations.PLUS.value or operators_stack[-1] == Operations.MINUS.value):
            q = create_quad(quad_counter, operators_stack, operands_stack, types_stack, temp_counter, memory, current_function, temporal_variables)
            quadruples_list.append(q)
            quad_counter+=1
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
    global quad_counter

    q = assignment_quad(operators_stack, operands_stack, types_stack)
    quadruples_list.append(q)
    quad_counter+=1

def p_sem_read_write(p):
    '''sem_read_write : empty
    '''
    global quad_counter

    q = one_operation_quad(operators_stack, operands_stack)
    quadruples_list.append(q)
    quad_counter+=1

def p_sem_return_function(p):
    '''sem_return_function : empty
    '''
    global quad_counter, current_function, memory


    if (current_function.function_type != Types.VOID.value):
        # Return variable
        return_var = operands_stack.pop()
        return_var_type = types_stack.pop()
        # print("return var: ", return_var)
        # print("type of return var from types stack: ", return_var_type)

        v = Variable(current_function.function_id, return_var_type, return_var, 0, 0)
        operands_stack.append(return_var)
        types_stack.append(return_var_type)

        global_function = functions_directory.find_function("Mathrix")

        # Check if return address for function already exists
        if v.var_id not in global_function.variables_directory:
            functions_directory.add_variable(v, global_function, memory)
        
        return_address = functions_directory.find_var_address(v.var_id, "Mathrix")
        
        # # Add return value to global variables
        # global_function = functions_directory.find_function("Mathrix")
        # functions_directory.add_variable(v, global_function, memory)
        # var_address = functions_directory.find_var_address(v.var_id, "Mathrix")
        
        # print("return_address: ", return_address)
        # print("return_var: ", return_var)

        # Create RETURN quad
        q = define_quad(Operations.RETURN.value, return_var, -1, return_address)
        quadruples_list.append(q)
        quad_counter+=1

# Expressions
def p_sem_top_logical(p):
    '''sem_top_logical : 
    '''
    global quad_counter, temp_counter, current_function, temporal_variables

    if(operators_stack[-1:]):
        if (operators_stack[-1] == Operations.AND.value or operators_stack[-1] == Operations.OR.value):
            q = create_quad(quad_counter, operators_stack, operands_stack, types_stack, temp_counter, memory, current_function, temporal_variables)
            quadruples_list.append(q)
            quad_counter+=1
            temp_counter+=1

def p_sem_top_relational(p):
    '''sem_top_relational : 
    '''
    global quad_counter, temp_counter, current_function, temporal_variables

    if(operators_stack[-1:]):
        if (operators_stack[-1] == Operations.GREATERTHAN.value or operators_stack[-1] == Operations.LESSTHAN.value or operators_stack[-1] == Operations.GREATERTHANOREQ.value or operators_stack[-1] == Operations.LESSTHANOREQ.value or operators_stack[-1] == Operations.ISEQUAL.value or operators_stack[-1] == Operations.NOTEQUAL.value):
            q = create_quad(quad_counter, operators_stack, operands_stack, types_stack, temp_counter, memory, current_function, temporal_variables)
            quadruples_list.append(q)
            quad_counter+=1
            temp_counter+=1

# Conditions and cycles
def p_sem_end_condition(p):
    '''sem_end_condition : empty
    '''
    global quad_counter, operands_stack, types_stack

    if (operands_stack[-1:]):
        q = create_GOTOF_quad(operands_stack, types_stack)
        quadruples_list.append(q)
        quad_counter+=1
        jumps_stack.append(quad_counter-1)
        # print("jumps_stack: ", jumps_stack)

def p_sem_fill_gotof(p):
    '''sem_fill_gotof : empty
    '''
    global quad_counter
    end = jumps_stack.pop()
    fill(quadruples_list, end, quad_counter)

def p_sem_else_condition(p):
    '''sem_else_condition : empty
    '''
    global quad_counter
    
    q = create_GOTO_quad()
    quadruples_list.append(q)
    quad_counter+=1
    false = jumps_stack.pop()
    jumps_stack.append(quad_counter-1)
    fill(quadruples_list, false, quad_counter)


def p_sem_start_while(p):
    '''sem_start_while : empty
    '''
    global quad_counter
    jumps_stack.append(quad_counter)

def p_sem_end_while(p):
    '''sem_end_while : empty
    '''
    global quad_counter
    end = jumps_stack.pop()
    ret = jumps_stack.pop()

    q = define_quad(Operations.GOTO.value, -1, -1, ret) 
    quadruples_list.append(q)
    quad_counter+=1
    fill(quadruples_list, end, quad_counter)


# Functions
def p_sem_add_param(p):
    '''sem_add_param : empty
    '''
    global functions_directory, current_function, memory
    
    v = Variable(p[-1], current_type, -1, 0, 0)
    #print(p[-1])

    # Parameter = local variable
    functions_directory.add_variable(v, current_function, memory)

    functions_directory.add_param(v, current_function)

def p_sem_check_function(p):
    '''sem_check_function : empty
    '''
    function_name = p[-1]

    global functions_directory, current_function, function_stack, previous_function

    previous_function = current_function
    #print("previous_function: ", previous_function.function_id)
    function_stack.append(previous_function.params_list)

    # Verify that the function called exists in functions directory
    if (functions_directory.function_exists(function_name)):
        current_function = functions_directory.find_function(function_name)
        function_stack.append(current_function.params_list)
    
    # print(function_stack)
    # for f in function_stack:
    #     print ("function id in fs: ", f.function_id)

def p_sem_create_era(p):
    '''sem_create_era : empty
    '''
    global quad_counter, current_function, parameter_counter, previous_function, function_called, era_stack
    # Start the parameter counter in 0
    parameter_counter = 0
   
    # Get the size of the function
    function_called = current_function
    
    #Create quads for vars, temps
    function_vars_quad = define_quad(Operations.ERA.value, function_called.ints, function_called.doubles, function_called.bools)
    quadruples_list.append(function_vars_quad)

    q = define_quad(Operations.ERA.value, function_called.function_id, -1, -1)
    quadruples_list.append(q)

    era_stack.append(quad_counter+1)

    quad_counter += 2
    # Return to previous function in order to check local variables
    current_function = previous_function

def p_sem_check_param(p):
    '''sem_check_param : empty
    '''
    global quad_counter, parameter_counter, current_function, function_called_params

    argument = operands_stack.pop()
    argument_type = types_stack.pop()
    
    # print("function_stack: ", function_stack)

    # current_function = function_stack.pop()
    # print("current_function: ", current_function)

    # Function's params to be checked
    function_called_params = function_stack[-1]

    # print("function_called_params: ", function_called_params)
    # print("parameter_counter: ", parameter_counter)
    # print("len(function_called_params): ", len(function_called_params))

    if(parameter_counter >= len(function_called_params)):
        print("Error, invalid number of parameters 1.")
        exit(1)

    if (len(function_called_params) > 0):
        # Verify argument type against current parameter
        current_param_type = function_called_params[parameter_counter]

        if(argument_type == current_param_type):
            # Generate PARAM quad
            q = define_quad(Operations.PARAM.value, argument, current_param_type, "p#" + str(parameter_counter))
            quadruples_list.append(q)
            quad_counter+=1
            parameter_counter+=1
        else:
            print("Error, invalid parameter type: {}, expecting: {}".format(argument_type, current_param_type))
            exit(1)

def p_sem_count_params(p):
    '''sem_count_params : empty
    '''
    global parameter_counter, function_called_params

    total_parameters = len(function_called_params)

    # Coherence in number of parameters
    if (total_parameters != parameter_counter):
        print("Error, invalid number of parameters.")
        exit(1)

#TODO: GOSUB Y GOSUBASSIGN?
def p_sem_gosub(p):
    '''sem_gosub : empty
    '''
    global quad_counter, current_function, function_called, function_stack, memory, temp_counter, operands_stack
     
    # Generate GOSUB quad
    q = define_quad(Operations.GOSUB.value, function_called.function_id, -1, function_called.start_address)
    quadruples_list.append(q)
    quad_counter+=1

    # print("function called: ", function_called.function_id )
    # print("function called type: ", function_called.function_type )

    print("current_function: ", current_function.function_id)
    print("function_Called: ", function_called.function_id)

    # If function is not void
    if(function_called.function_type != Types.VOID.value):
        # Assign result of return value to a temp var
        temp = "t" + str(temp_counter)
        temp_counter+=1
        temp_var = Variable(temp, function_called.function_type, -1, 0, {})
        temp_var.var_address = memory.set_temp_address(temp_var)
        
        operands_stack.append(temp_var.var_address)
        
        # Store this temporal var in the global var return for this function
        return_var = functions_directory.find_variable(function_called.function_id, "Mathrix")
        
        # Create assignment quad
        q2 = define_quad(Operations.ASSIGN.value, return_var.var_address, temp_var.var_type, temp_var.var_address)
        quadruples_list.append(q2)
        quad_counter+=1

    function_stack.pop()

    # print("functions_stack: ", function_stack)

# Start program
def p_sem_start_program(p):
    '''sem_start_program : empty
    '''
    global functions_directory, current_function, current_type, quad_counter
    
    Mathrix = Function('Mathrix', Types.VOID.value, {}, [], 0, 0, 0, 0)
    functions_directory._functions['Mathrix'] = Mathrix

    current_function = functions_directory._functions['Mathrix']
    current_type = Types.VOID.value

    # Starting quad
    q = define_quad (Operations.GLOBALERA.value, -1, -1, -1)
    quadruples_list.append(q)
    quad_counter+=1

    # Generate FIRST quad (GOTO)
    q = define_quad(Operations.GOTO.value, -1, -1, -1) 
    quadruples_list.append(q)
    quad_counter+=1

def p_sem_fill_goto_main(p):
    '''sem_fill_goto_main : empty
    '''
    global current_function, current_type, temp_counter
    
    temp_counter = 0
    
    current_function = functions_directory._functions['Mathrix']
    current_function.start_address = quad_counter
    current_type = Types.VOID.value

    quadruples_list[1]['result'] = quad_counter


def p_sem_end_main(p):
    '''sem_end_main : empty
    '''
    global quad_counter, temp_counter

    local_vars = len(current_function.variables_directory)
    function_size = local_vars + temp_counter
    
    current_function.size = function_size
    # Fill quad 0 with final main size
    quadruples_list[0]['result'] = current_function.size

    #Generate LAST quad (END)
    q = define_quad(Operations.END.value, -1, -1, -1) 
    quadruples_list.append(q)
    quad_counter+=1

    function_stack.clear()

def p_sem_fill_eras(p):
    '''sem_fill_eras : empty
    '''

    while era_stack[-1:]:
        quad = era_stack.pop()
        function_id = quadruples_list[quad]['left_operand']
        temp_ints = temporal_variables[function_id][Types.INT.value]
        temp_doubles = temporal_variables[function_id][Types.DOUBLE.value]
        temp_bools = temporal_variables[function_id][Types.BOOL.value]
        quadruples_list[quad]['left_operand'] = temp_ints
        quadruples_list[quad]['right_operand'] = temp_doubles
        quadruples_list[quad]['result'] = temp_bools

# Matrices
# Matrix declaration
def p_sem_get_matrix_id(p):
    '''sem_get_matrix_id : empty
    '''
    global matrix_id
    matrix_id = p[-1]

def p_sem_get_dim1(p):
    '''sem_get_dim1 : empty
    '''
    global lim_s1

    lim_s1 = p[-1]

    if lim_s1 < 0:
        print("Error. Invalid matrix dimension")
        exit(1)

def p_sem_get_dim2(p):
    '''sem_get_dim2 : empty
    '''
    global lim_s2

    lim_s2 = p[-1]
    if lim_s2 < 0:
        print("Error. Invalid matrix dimension")
        exit(1)

def p_sem_add_matrix(p):
    '''sem_add_matrix : empty
    '''
    global matrix_id, lim_s1, lim_s2

    dim1_dict = Dimension(0, int(lim_s1), 0)
    dim2_dict = Dimension(0, int(lim_s2), 0)
    # Formulas for 2 dimensional arrays
    r1 = 1 * (dim1_dict.lim_s - 0 + 1)
    m0 = r1 * (dim2_dict.lim_s - 0 + 1)
    
    m1 = m0 / (dim1_dict.lim_s - 0 + 1)
    dim1_dict.k = int(m1)
    m2 = m1 / (dim2_dict.lim_s - 0 + 1)

    suma = 0 + dim2_dict.lim_i * m2
    dim2_dict.k = int(suma * -1)

    # print("dim1_dict: ", dim1_dict)
    # print("dim2_dict: ", dim2_dict)

    v = Variable(matrix_id, current_type, -1, dim1_dict, dim2_dict)
    functions_directory.add_variable(v, current_function, memory)

# Matrix access
def p_sem_check_dim1(p):
    '''sem_check_dim1 : empty
    '''
    global operands_stack, current_function, matrix_var, dimension_stack, lim_s1
    
    matrix_address = operands_stack.pop()

    # Check that current variable is a matrix
    matrix_id = functions_directory.find_var_id(matrix_address, current_function)
    matrix_var = functions_directory.find_variable(matrix_id, current_function.function_id)

    if matrix_var.var_dim1_dict == 0:
        print("Error. Variable is not a matrix.")
        exit(1)
    
    dim = 1
    matrix_dim1 = (matrix_var.var_id, dim)
    dimension_stack.append(matrix_dim1)

    # Get matrix's first dimension lim_s1
    lim_s1 = matrix_var.var_dim1_dict.lim_s
    #print("lim_s1:", lim_s1)

    # Push false bottom into operators stack
    operators_stack.append(Operations.LEFT_BRACKET.value)

def p_sem_ver_dim1(p):
    '''sem_ver_dim1 : empty
    '''
    global quad_counter, operands_stack, lim_s1, operators_stack, temp_counter, types_stack

    operands_stack_top = operands_stack[-1]
    operands_stack_top_id = functions_directory.find_var_id(operands_stack_top, current_function)

    # Verification quad
    q = define_quad(Operations.VER.value, operands_stack_top_id, 0, lim_s1) 
    quadruples_list.append(q)
    quad_counter+=1

    # Create dim1*m1 quad
    operators_stack.append(Operations.MULTIPLY.value)
    m1 = int(matrix_var.var_dim1_dict.k)

    # Register m1 as constant
    types_stack.append(Types.INT.value)
    constant_int = "#" + str(m1)
    # print("m1: ", constant_int)

    constant_int_var = Variable(constant_int, Types.INT.value, -1, 0, 0)
    if functions_directory.find_constant(constant_int_var):
        # print("Constant ", constant_int_var.var_id, " was found again")
        constant_int_var.var_address = functions_directory.find_var_address(constant_int_var.var_id, "Mathrix")
    else:
        # Add constants to global variables
        constant_int_var.var_address = memory.set_cte_address(constant_int_var)
        functions_directory.add_constant(constant_int_var) 
    operands_stack.append(constant_int_var.var_address)

    q = create_quad(quad_counter, operators_stack, operands_stack, types_stack, temp_counter, memory, current_function, temporal_variables)
    quadruples_list.append(q)
    quad_counter+=1
    temp_counter+=1

    # Pop false bottom from operators stack
    operators_stack.pop()

def p_sem_check_dim2(p):
    '''sem_check_dim2 : empty
    '''
    global operands_stack, current_function, matrix_var, dimension_stack, lim_s2
    
    # Get matrix's first dimension lim_s
    lim_s2 = matrix_var.var_dim2_dict.lim_s
    #print("lim_s 2:", lim_s2)

    # Push false bottom into operators stack
    operators_stack.append(Operations.LEFT_BRACKET.value)

def p_sem_ver_dim2(p):
    '''sem_ver_dim2 : empty
    '''
    global quad_counter, operands_stack, lim_s2, temp_counter

    operands_stack_top = operands_stack[-1]
    operands_stack_top_id = functions_directory.find_var_id(operands_stack_top, current_function)

    q = define_quad(Operations.VER.value, operands_stack_top_id, 0, lim_s2) 
    quadruples_list.append(q)
    quad_counter+=1

    # Create dim1*m1 + dim2 quad
    operators_stack.append(Operations.PLUS.value)
    q = create_quad(quad_counter, operators_stack, operands_stack, types_stack, temp_counter, memory, current_function, temporal_variables)
    quadruples_list.append(q)
    quad_counter+=1
    temp_counter+=1

    # Add matrix base address
    operators_stack.append(Operations.PLUS.value)
    base_address = matrix_var.var_address
    base_address_cte = "#" + str(base_address)
    operands_stack.append(base_address_cte)
    types_stack.append(Types.INT.value)

    q = create_quad(quad_counter, operators_stack, operands_stack, types_stack, temp_counter, memory, current_function, temporal_variables)
    quadruples_list.append(q)
    quad_counter+=1
    temp_counter+=1

    # Distinguish address 
    result = operands_stack.pop()
    result_address = '(' + str(result) + ')'
    
    operands_stack.append(result_address)

    # Pop false bottom from operators stack
    operators_stack.pop()

# TODO: check that rows and cols match with declaration
def p_sem_assign_matrix(p):
    '''sem_assign_matrix : empty
    '''
    global matrix, operators_stack, operands_stack, types_stack, quad_counter, var_memory_address

    matrix_address = var_memory_address
    count_spaces = 0

    for i in matrix:
        for j in i:
            operands_stack.append(matrix_address)
            types_stack.append(Types.INT.value)

            # Add constants
            operands_stack.append("#" + str(j))
            types_stack.append(Types.INT.value)

            operators_stack.append(Operations.ASSIGN.value)

            matrix_address+=1

            q = assignment_quad(operators_stack, operands_stack, types_stack)
            quadruples_list.append(q)
            quad_counter+=1

            count_spaces+=1
    
    # Increase memory counter for global ints
    memory.global_int_counter+= count_spaces

    # Clear matrix
    matrix = []

def p_sem_clear_row(p):
    '''sem_clear_row : empty
    '''
    global row
    row = []

def p_sem_push_row(p):
    '''sem_push_row : empty
    '''
    global matrix, row
    matrix.append(row)

def p_sem_push_col(p):
    '''sem_push_col : empty
    '''
    global row 
    row.append(p[-1])

## MATHRIX FUNCTIONS

parser_Mathrix = yacc.yacc()

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Mathrix - </title>")
print ("</head>")
print ("<body>")

try:
    print ("<table>")
    print ("<tr>")
    print ("<th><h2>Mathrix:  </h2></th>")
    print ("<th><h2>Output</h2></th>")
    print ("</tr>")

    print ("<tr>")
    print ("<th>")
    print("<textarea rows='100' cols='50'>")
    data ="""
matrix int m[1][1];
matrix int n[1][1];
matrix int r[1][1];
int i;
int j;
int k;
int t;

Main {
    i = 0;
    j = 0;
    k = 0;
    t = 0;

    matrix m = {[1,2],[3,4]};
    matrix n = {[1,1],[1,1]};
    matrix r = {[0,0],[0,0]};

    
    while(i < 2){
        j = 0;
        while(j < 2){
            k = 0;
            r[i][j] = 0;
            while(k < 2){
                t = r[i][j];
                r[i][j] = t + (m[i][k] * n[k][j]);
                k = k + 1;
            }
            j = j + 1;
        }
        i = i + 1;
    }

    i = 0;
    j = 0;

    while(i < 2){
        j = 0;
        while(j <2){
            write(r[i][j]);
            j = j + 1;
        }
        i = i + 1;
    }
}
        """
    print(data)
    print("</textarea>")
    print ("</th>")

    
    print ("<th>")
    print("<textarea rows='100' cols='100'>")
    parser_Mathrix.parse(data)
    print_quads(quadruples_list)
    #print("quad_counter: ", quad_counter)
    #print("# of quads: ", len(quadruples_list))

    # print("Functions directory: ")
    # functions_directory.print_table()

    # Run virtual machine
    run(functions_directory, quadruples_list)

    # process_quads(quadruples_list)
    print("</textarea>")
    print ("</th>")

    print ("<tr>")
    print ("<table>")
    
    
    
except EOFError:
    print(EOFError)

print ("<br/>")
print ("</body>")
print ("</html>")
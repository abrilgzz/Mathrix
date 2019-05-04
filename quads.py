from semantic_cube import SemanticCube
from constants import Types
from constants import Operations
from constants import Errors

from functions_table import Function
from functions_table import Variable
from functions_table import FunctionsTable

from memory import Memory

def define_quad(operator, left_operand, right_operand, result):
    quad = {'operator' : operator, 'left_operand' : left_operand, 'right_operand' : right_operand, 'result' : result}
    return quad

def create_quad(quad_counter, operators_stack, operands_stack, types_stack, temp_counter, memory, current_function, temporal_variables):
    operator = operators_stack.pop()
    # Get right operator and its type
    right_operand = operands_stack.pop()
    right_operand_type = types_stack.pop()
    # Get left operator and its type
    left_operand = operands_stack.pop()
    left_operand_type = types_stack.pop()
    # Search cube for result type
    result_type = int(SemanticCube[operator, left_operand_type, right_operand_type])

    if(result_type == Errors.MISMATCH):
        print("Error, type mismatch.")
        exit(1)
    else:
        # Create temporary registry 
        temp = "t" + str(temp_counter)
        temp_var = Variable(temp, result_type, -1)
        temp_var.var_address = memory.set_temp_address(temp_var)
        
        # Add to temporal vars dict
        if(current_function.function_id != 'Mathrix'):
                temporal_variables[current_function.function_id][temp_var.var_type] += 1
        
        # Push operands and types obtained to stacks
        operands_stack.append(temp_var.var_address)
        types_stack.append(result_type)
        quad = define_quad(operator, left_operand, right_operand, temp_var.var_address)
        return quad

# Create GOTOF quad
def create_GOTOF_quad(operands_stack, types_stack):
        expression_type = types_stack.pop()

        # Check if expression type is boolean
        if(expression_type == 2):
                result = operands_stack.pop()
                q = define_quad(Operations.GOTOF.value, result, -1, -1)
                return q
        else:
                print("Error, type mismatch, expression is not boolean")
                exit(1)


# Create GOTO quad
def create_GOTO_quad():
        q = define_quad(Operations.GOTO.value, -1, -1, -1)
        return q

        # expression_type = types_stack.pop()

        # # Check if expression type is boolean
        # if(expression_type == 2):
        #         q = define_quad(Operations.GOTO.value, -1, -1, -1)
        #         return q
        # else:
        #         print("Error, type mismatch, expression is not boolean")
        #         exit(1)

# Creates quadruple for assignments
def assignment_quad(operators_stack, operands_stack, types_stack):
        operator = operators_stack.pop()
        operand = operands_stack.pop()
        operand_type = types_stack.pop()
        result = operands_stack.pop()
        result_type = types_stack.pop()
        
        assignment_result = -1

        assignment_result = int(SemanticCube[operator, result_type, operand_type])
        
        if(assignment_result == -1):
                print("Error, cannot assign.")
                exit(1)
        else:
                quad = define_quad(operator, operand, -1, result)
                return quad

def one_operation_quad(operators_stack, operands_stack):
        result = operands_stack.pop()
        operation = operators_stack.pop()
        quad = define_quad(operation, -1, -1, result)
        return quad

# Check fill function
def fill(quadruples_list, end, quad_counter):
        quadruples_list[end]['result'] = quad_counter

def print_quads(quadruples_list):
    counter = 0
    print("Quadruples: ")
    for q in quadruples_list:
            print("q", counter, ": ", q)
            counter+=1

from semantic_cube import SemanticCube
from constants import Types
from constants import Operations
from constants import Errors

def define_quad(operator, left_operand, right_operand, result):
    quad = {'operator' : operator, 'left_operand' : left_operand, 'right_operand' : right_operand, 'result' : result}
    return quad

def create_quad(temp_counter, operators_stack, operands_stack, types_stack):
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
        # Push operands and types obtained to stacks
        operands_stack.append(temp)
        types_stack.append(result_type)
        quad = define_quad(operator, left_operand, right_operand, temp)
        return quad

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
        else:
                quad = define_quad(operator, operand, -1, result)
                return quad

def one_operation_quad(operators_stack, operands_stack):
        result = operands_stack.pop()
        operation = operators_stack.pop()
        quad = define_quad(operation, -1, -1, result)
        return quad

def print_quads(quadruples_list):
    counter = 1
    print("Quadruples: ")
    for q in quadruples_list:
            print("q", counter, ": ", q)
            counter+=1

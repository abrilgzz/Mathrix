from semanticCube import SemanticCube
from constants import Types
from constants import Operations
from constants import Errors

def defineQuad(operator, left_operator, right_operator, result):
    quad = {'operator' : operator, 'left_operator' : left_operator, 'right_operator' : right_operator, 'result' : result}
    return quad

def createQuad(temp_counter, operator_stack, operand_stack, types_stack):
    operator = operator_stack.pop()
    # Get left operator and its type
    left_operator = operand_stack.pop()
    left_operator_type = types_stack.pop()
    # Get right operator and its type
    right_operator = operand_stack.pop()
    right_operator_type = types_stack.pop()
    # Search cube for result type
    result_type = SemanticCube[operator, left_operator, right_operator]

    if(result_type == Errors.MISMATCH):
        print("Error, type mismatch.")
    else:
        # Create temporary registry 
        temp = "t" + str(temp_counter)
        # Push operands and types obtained to stacks
        operand_stack.append(temp)
        types_stack.append(result_type)
        quad = defineQuad(operator, left_operator, right_operator, temp)
        return quad

def printQuads(quads):
    counter = 0
    print("Quadruples: ")
    for q in quads:
        print(str(counter) + ": ", str(q['operator'], " ", str(q['left_operator'], " ", str(q['right_operator'], " ", str(q['result'])))))
        counter+=1

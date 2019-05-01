from execution_memory import ExecutionMemory
from constants import *

instruction_pointer = 2
instruction_pointer_stack = []

function_stack = []
function_counter = 0

em = ExecutionMemory()
current_function = "Mathrix"




def run(functions_directory, quadruples_list):
    # Generate ERA for global function
    print("global var dict: ", functions_directory._functions['Mathrix'].variables_directory)
    em.start_global_memory(functions_directory._functions['Mathrix'].variables_directory)

    # Add global function to function stack
    function_stack.append("Mathrix")
    
    # Process quadruples list
    process_quads(quadruples_list)

# def print_result(result):
#     print("result: ", result)

def process_quads(quadruples_list):
    global instruction_pointer, current_function, function_counter


    while(instruction_pointer < len(quadruples_list)):
        current_quad = quadruples_list[instruction_pointer]

        # print("current_quad: ", current_quad)
        # print("memory: ", em.memory)

        # Determine operations
        if(current_quad['operator'] == Operations.PLUS.value):
            left_operand = em.get_variable_value(current_quad['left_operand'], current_function)
            right_operand = em.get_variable_value(current_quad['right_operand'], current_function)
            result = left_operand + right_operand
            
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1
            print(em.memory)
        elif(current_quad['operator'] == Operations.MINUS.value):
            left_operand = em.get_variable_value(current_quad['left_operand'], current_function)
            right_operand = em.get_variable_value(current_quad['right_operand'], current_function)
            result = left_operand - right_operand
            
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1 
        elif(current_quad['operator'] == Operations.DIVIDE.value):
            left_operand = em.get_variable_value(current_quad['left_operand'], current_function)
            right_operand = em.get_variable_value(current_quad['right_operand'], current_function)
            result = left_operand / right_operand
            # 
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1
        elif(current_quad['operator'] == Operations.MULTIPLY.value):
            left_operand = em.get_variable_value(current_quad['left_operand'], current_function)
            right_operand = em.get_variable_value(current_quad['right_operand'], current_function)
            result = left_operand * right_operand
            
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1 
        elif(current_quad['operator'] == Operations.ISEQUAL.value):
            left_operand = em.get_variable_value(current_quad['left_operand'], current_function)
            right_operand = em.get_variable_value(current_quad['right_operand'], current_function)
            result = left_operand == right_operand
            
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1
        elif(current_quad['operator'] == Operations.GREATERTHAN.value):
            left_operand = em.get_variable_value(current_quad['left_operand'], current_function)
            right_operand = em.get_variable_value(current_quad['right_operand'], current_function)
            result = left_operand != right_operand
            
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1
        elif(current_quad['operator'] == Operations.GREATERTHAN.value):
            left_operand = em.get_variable_value(current_quad['left_operand'], current_function)
            right_operand = em.get_variable_value(current_quad['right_operand'], current_function)
            result = left_operand > right_operand
            
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1
        elif(current_quad['operator'] == Operations.GREATERTHANOREQ.value):
            left_operand = em.get_variable_value(current_quad['left_operand'], current_function)
            right_operand = em.get_variable_value(current_quad['right_operand'], current_function)
            result = left_operand >= right_operand
            
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1
        elif(current_quad['operator'] == Operations.LESSTHAN.value):
            left_operand = em.get_variable_value(current_quad['left_operand'], current_function)
            right_operand = em.get_variable_value(current_quad['right_operand'], current_function)
            result = left_operand < right_operand
            
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1
        elif(current_quad['operator'] == Operations.AND.value):
            left_operand = em.get_variable_value(current_quad['left_operand'], current_function)
            right_operand = em.get_variable_value(current_quad['right_operand'], current_function)
            result = left_operand and right_operand
            
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1 
        elif(current_quad['operator'] == Operations.OR.value):
            left_operand = em.get_variable_value(current_quad['left_operand'], current_function)
            right_operand = em.get_variable_value(current_quad['right_operand'], current_function)
            result = left_operand or right_operand
            
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1
        elif(current_quad['operator'] == Operations.ASSIGN.value):
            result = em.get_variable_value(current_quad['left_operand'], current_function)
            
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1
        elif(current_quad['operator'] == Operations.READ.value):
            result = input("")
            em.write_to_memory(current_quad['result'], result, current_function)
            instruction_pointer+=1
        elif(current_quad['operator'] == Operations.WRITE.value):
            result = em.get_variable_value(current_quad['left_operand'], current_function)
            
            print(result)
            #print_result(result)
            instruction_pointer+=1
        elif(current_quad['operator'] == Operations.RETURN.value):
            result = em.get_variable_value(current_quad['left_operand'], current_function)
            temp_func_storage = current_function
            current_function = "Mathrix"
            em.write_to_memory(current_quad['result'], result, current_function)
            current_function = temp_func_storage
        elif(current_quad['operator'] == Operations.GOTOF.value):
            result = em.get_variable_value(current_quad['left_operand'], current_function)
            
            if not result:
                next_quad = int(current_quad['result'])
                instruction_pointer = next_quad
            else:
                instruction_pointer+=1
        elif(current_quad['operator'] == Operations.GOTO.value):
            instruction_pointer = int(current_quad['result'])
            print(result)
            #print_result(result)
            instruction_pointer+=1
        elif(current_quad['operator'] == Operations.PARAM.value):
            param = em.get_variable_value(current_quad['left_operand'], current_function)
            param_type = current_quad['right_operand']

            em.write_param_to_memory(param_type, param, current_function)
            instruction_pointer+=1
        elif(current_quad['operator'] == Operations.GOSUB.value):
            instruction_pointer_stack.append(instruction_pointer+1)
            function_stack.append(current_function)
            next_quad = current_quad['result']

            instruction_pointer = next_quad
            current_function = str(function_counter-1)
        elif(current_quad['operator'] == Operations.ERA.value):
            #TO-DO
            em.start_local_memory(current_quad)
            function_counter+=1
        # elif(current_quad['operator'] == Operations.GLOBALERA.value):
        #     #TO-DO
        #     em.start_global_memory(current_quad)
        #     function_counter+=1
        elif(current_quad['operator'] == Operations.ENDPROC.value):
            instruction_pointer = instruction_pointer_stack.pop()
            em.clear_memory(current_function)
            current_function = function_stack.pop()
        elif(current_quad['operator'] == Operations.END.value):
            print("final memory looks like this: ", em.memory)
            em.end_program()
            print("Goodbye!")
            exit(1)
        else:
            pass
    

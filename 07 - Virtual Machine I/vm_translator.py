def main():
    global file_path
    global file_name
    vm_file = open(file_path, "r")
    asm_code_array = []
    for line in vm_file:
        line = line.strip()
        if line and line[0] != "/":
            to_array = line.split(" ")
            if len(to_array) > 3:
                vm_commands = removeComments(to_array)
            else:
                vm_commands = to_array
            if len(vm_commands) == 1:
                if(vm_commands[0] != 'return'):
                    asm_code_array.append(
                        arithmeticCommandTranslator(vm_commands[0]))
                else:
                    asm_code_array.append(handleReturn(
                        vm_commands[0]))
            elif len(vm_commands) == 2:
                asm_code_array.append(
                    branchingCommandTranslator(vm_commands))
            elif len(vm_commands) == 3:
                if(to_array[0] == 'function' or to_array[0] == 'call'):
                    asm_code_array.append(functionCommandTranslator(to_array))
                else:
                    asm_code_array.append(
                        memorySegmentCommandTranslator(to_array))

    toWrite = file_name+".asm"
    f = open(toWrite, "w")
    for instruction in asm_code_array:
        f.write(instruction)
    f.close()


def removeComments(array):
    result = []
    index = 0
    for element in array:
        if element == '' or element == '//':
            result = array[0:index]
        else:
            index += 1
    return result


def arithmeticCommandTranslator(command):
    global command_counter
    comment = f"//{command}\n"
    command_code_map = {
        "add": "@SP\nM=M-1\nA=M\nD=M\n@SP\nA=M-1\nM=M+D\n",
        "sub": "@SP\nM=M-1\nA=M\nD=M\n@SP\nA=M-1\nM=M-D\n",
        "neg": "@SP\nA=M-1\nM=-M\n",
        "eq": f"@SP\nM=M-1\nA=M \nD=M\n@SP\nA=M-1\nD=D-M\n@Equal{command_counter}\nD;JEQ\n@SP\nA=M-1\nM=0\n@End{command_counter}\n0;JMP\n(Equal{command_counter})\n@SP\nA=M-1\nM=-1\n(End{command_counter})\n@End{command_counter}\n",
        "gt": f"@SP\nM=M-1\nA=M-1\nD=M\n@SP\nA=M\nD=D-M\n@Greater{command_counter}\nD;JGT\n@SP\nA=M-1\nM=0\n@End{command_counter}\n0;JMP\n(Greater{command_counter})\n@SP\nA=M-1\nM=-1\n(End{command_counter})\n@End{command_counter}\n",
        "lt": f"@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n@Smaller{command_counter}\nD;JLT\n@SP\nA=M-1\nM=0\n@End{command_counter}2\n\n0;JMP\n\n(Smaller{command_counter})\n@SP\nA=M-1\n\nM=-1\n(End{command_counter}2)\n@End{command_counter}2\n",
        "and": "@SP\nM=M-1\nA=M\nD=M\n@SP\nA=M-1\nD=D&M\nM=D\n",
        "or":  "@SP\nM=M-1\nA=M\nD=M\n@SP\nA=M-1\nD=D|M\nM=D\n",
        "not": "@SP\nA=M-1\nM=!M\n"
    }
    command_counter += 1
    result = comment + command_code_map[command]
    return result


def memorySegmentCommandTranslator(command_array):
    comment = "//" + (" ").join(command_array) + "\n"
    asm_code = ""
    if command_array[0] == "push":
        asm_code = handlePushCommand(command_array)
    else:
        asm_code = handlePopCommand(command_array)
    result = comment+asm_code
    return result


def handlePushCommand(command_array):
    target_memory_segment = command_array[1]
    target_index = command_array[2]
    result = ""
    if(target_memory_segment == "constant"):
        result = f"@{target_index}\nD=A\n"
    elif(target_memory_segment == "local"):
        result = f"@{target_index}\nD=A\n@LCL\nA=M\nA=A+D\nD=M\n"
    elif(target_memory_segment == "argument"):
        result = f"@{target_index}\nD=A\n@ARG\nA=M\nA=A+D\nD=M\n"
    elif(target_memory_segment == "this"):
        result = f"@{target_index}\nD=A\n@THIS\nA=M\nA=A+D\nD=M\n"
    elif(target_memory_segment == "that"):
        result = f"@{target_index}\nD=A\n@THAT\nA=M\nA=A+D\nD=M\n"
    elif(target_memory_segment == "pointer"):
        if int(target_index) == 0:
            result = f"@THIS\nD=M\n"
        else:
            result = f"@THAT\nD=M\n"
    elif(target_memory_segment == "static"):
        global file_name
        result = f"@{file_name}.{target_index}\nD=M\n"
    elif(target_memory_segment == "temp"):
        target_index = int(target_index) + 5
        result = f"@{target_index}\nD=M\n"

    push_and_increment_sp = "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
    result += push_and_increment_sp
    return result


def handlePopCommand(command_array):
    global command_counter
    target_memory_segment = command_array[1]
    target_index = command_array[2]
    result = ""

    if(target_memory_segment == "local"):
        result = f"@{target_index}\nD=A\n@LCL\nA=M+D\nD=A\n@location{command_counter}\nM=D\n@SP\nA=M-1\nD=M\n@location{command_counter}\nA=M\nM=D\n"
    elif(target_memory_segment == "argument"):
        result = f"@{target_index}\nD=A\n@ARG\nA=M+D\nD=A\n@location{command_counter}\nM=D\n@SP\nA=M-1\nD=M\n@location{command_counter}\nA=M\nM=D\n"
    elif(target_memory_segment == "this"):
        result = f"@{target_index}\nD=A\n@THIS\nA=M+D\nD=A\n@location{command_counter}\nM=D\n@SP\nA=M-1\nD=M\n@location{command_counter}\nA=M\nM=D\n"
    elif(target_memory_segment == "that"):
        result = f"@{target_index}\nD=A\n@THAT\nA=M+D\nD=A\n@location{command_counter}\nM=D\n@SP\nA=M-1\nD=M\n@location{command_counter}\nA=M\nM=D\n"
    elif(target_memory_segment == "pointer"):
        if int(target_index) == 0:
            result = f"@SP\nA=M-1\nD=M\n@THIS\nM=D\n"
        else:
            result = f"@SP\nA=M-1\nD=M\n@THAT\nM=D\n"
    elif(target_memory_segment == "static"):
        global file_name
        result = f"@SP\nA=M-1\nD=M\n@{file_name}.{target_index}\nM=D\n"
    elif(target_memory_segment == "temp"):
        target_index = int(target_index) + 5
        result = f"@SP\nA=M-1\nD=M\n@{target_index}\nM=D\n"
    command_counter += 1
    decrement_sp = "@SP\nM=M-1\n"
    result = result + decrement_sp
    return result


def branchingCommandTranslator(command_array):
    comment = commentGenerator(command_array)
    result = ''

    if(command_array[0] == 'label'):
        result = f'({command_array[1]})\n'
    elif(command_array[0] == 'goto'):
        result = f'@{command_array[1]}\n0;JMP\n'
    elif(command_array[0] == 'if-goto'):
        result = f'@SP\nM=M-1\nA=M\nD=M\n@{command_array[1]}\nD;JGT\n'

    return comment+result


def functionCommandTranslator(command_array):
    comment = commentGenerator(command_array)
    command = command_array[0]
    result = ''
    if command == 'function':
        result = translateFunctionDefinition(command_array)
    elif command == 'call':
        result = translateFunctionCall(command_array)
    return comment+result


def translateFunctionDefinition(array):
    comment = commentGenerator(array)
    local_vars = array[2]
    result = f'({array[0]})\n'
    for i in range(int(local_vars)):
        result += '@SP\nA=M\nM=0\n@SP\nM=M+1\n'
    return comment + result


def translateFunctionCall(array):
    return 1


def handleReturn(command_array):
    comment = commentGenerator(command_array)

    result = '@SP\nA=M-1\nD=M'
    # result = '@LCL\nD=A\n@Frame\nM=D\n@LCL\n'
    # for i in range(5):
    #     result += 'A=A-1\n'
    # result += 'D=M\n@RET\nM=D\n'
    # # pop
    # result += '@SP\nM=M-1\nA=M\nD=M\n@ARG\nA=M\nM=D\n'
    # #sp = ARG + 1
    # result += '@ARG\nD=A+1\n@SP\nM=D\n'
    # # THAT
    # result += '@Frame\nA=M-1\nD=M\n@THAT\nM=D\n'
    # # THIS
    # result += '@Frame\nA=M-1\nA=A-1\nD=M\n@THIS\nM=D\n'
    # # ARG
    # result += '@Frame\nA=M-1\nA=A-1\nA=A-1\nD=M\n@ARG\nM=D\n'
    # # LCL
    # result += '@Frame\nA=M-1\nA=A-1\nA=A-1\nA=A-1\nD=M\n@LCL\nM=D\n'
    # # goto RET
    # result += '@RET\n0;JMP\n'

    return comment + result


def commentGenerator(array):
    comment = ' '
    comment = comment.join(array)
    comment = '//' + comment + '\n'

    return comment


def getUserInput():
    global file_path
    global file_name
    user_input = input(
        "Index of the VM file to translate: \n 1- SimpleAdd \n 2-StackTest \n 3-BasicTest \n 4-PointerTest \n 5-StaticTest\n 6- Basic Loop\n 7- Fibonacci Series\n 8-Simple Function\n ")
    user_input = int(user_input)
    if(user_input == 1):
        file_name = "SimpleAdd"
        file_path = "./StackArithmetic/SimpleAdd/SimpleAdd.vm"
    if(user_input == 2):
        file_name = "StackTest"
        file_path = "./StackArithmetic/StackTest/StackTest.vm"
    if(user_input == 3):
        file_name = "BasicTest"
        file_path = "./MemoryAccess/BasicTest/BasicTest.vm"
    if(user_input == 4):
        file_name = "PointerTest"
        file_path = "./MemoryAccess/PointerTest/PointerTest.vm"
    if(user_input == 5):
        file_name = "StaticTest"
        file_path = "./MemoryAccess/StaticTest/StaticTest.vm"
    if(user_input == 6):
        file_name = "BasicLoop"
        file_path = "../08/ProgramFlow//BasicLoop/BasicLoop.vm"
    if(user_input == 7):
        file_name = "FibonacciSeries"
        file_path = "../08/ProgramFlow//FibonacciSeries/FibonacciSeries.vm"
    if(user_input == 8):
        file_name = "SimpleFunction"
        file_path = "../08/FunctionCalls/SimpleFunction/SimpleFunction.vm"


command_counter = 0
file_path = "not assigned"
file_name = "not assigned"
getUserInput()
main()

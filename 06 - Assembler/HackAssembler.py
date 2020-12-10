from baseconv import base2

file_name = input("Which assembly file to translate: \n")
file_name = file_name.lower()
file_path = "./" + file_name + "/" + file_name.capitalize()+".asm"
asm_file = open(file_path, "r")

variable_address_counter = 15
symbols_table = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4
}


def isCInstruction(ins):
    if(ins[0] != "@"):
        return True
    else:
        return False


def convertTo15BitBinary(str):
    number = base2.encode(int(str))
    zeros = 16 - len(number)
    zero_str = zeros * "0"
    result = zero_str+number
    return(result)


def handleAinstruction(instruction):
    instruction = instruction.replace("@", "")
    try:
        instruction = int(instruction)
        return convertTo15BitBinary(instruction)
    except:
        try:
            var_address = symbols_table[instruction]
            return convertTo15BitBinary(var_address)
        except:
            global variable_address_counter
            variable_address_counter += 1
            symbols_table[instruction] = variable_address_counter
            return convertTo15BitBinary(variable_address_counter)


def returnCCode(c):

    comp_table = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "!D": "0001101",
        "!A": "0110001",
        "-D": "0001111",
        "-A": "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D|A": "0010101",
        "M": "1110000",
        "!M": "1110001",
        "-M": "1110011",
        "M+1": "1110111",
        "M-1": "1110010",
        "D+M": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "D|M": "1010101",
    }
    dest_table = {
        "null": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111"
    }
    jump_table = {
        "null": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
    }

    if "=" in c:
        if ";" in c:  # both destination and jump
            dest = c.split("=")[0]
            comp = c.split("=")[0].split(";")[0]
            jump = c.split("=")[0].split(";")[1]
        else:
            dest = c.split("=")[0]
            comp = c.split("=")[1]
            jump = "null"
    elif ";" in c:  # no destination but Jump
        dest = "null"
        comp = c.split(";")[0]
        jump = c.split(";")[1]
    else:  # no destination, no jump
        dest = "null"
        comp = c.split(";")[0]
        jump = "null"

    comp_code = comp_table[comp]
    dest_code = dest_table[dest]
    jump_code = jump_table[jump]

    return({"dest": dest_code, "comp": comp_code, "jump": jump_code})


def handleCinstruction(instruction):
    result = "111"
    C_obj = returnCCode(instruction)

    result += C_obj["comp"]
    result += C_obj["dest"]
    result += C_obj["jump"]

    return result


def parser(asm_file):
    instructions = []
    for line in asm_file:
        new_line = line.strip()

        if(new_line):
            if(new_line[0] != "/"):
                # remove inline commands
                line_without_comments = new_line.split("/")[0].strip()
                instructions.append(line_without_comments)
    return instructions


def filterLoopLabels(instructions):
    loops_removed = []
    instruction_counter = 0
    for instruction in instructions:
        if(instruction[0] == "("):
            instruction = instruction.replace("(", "")
            instruction = instruction.replace(")", "")
            try:
                symbols_table[instruction]
            except KeyError:
                symbols_table[instruction] = instruction_counter
        else:
            loops_removed.append(instruction)
            instruction_counter += 1
    return loops_removed


def secondMarch(instructions):
    converted_lines = []
    for instruction in instructions:
        converted = ""
        isC = isCInstruction(instruction)
        if(isC):
            converted = handleCinstruction(instruction)
        else:
            converted = handleAinstruction(instruction)
        converted_lines.append(converted)
    return(converted_lines)


instructions = parser(asm_file)
instructions_without_labels = filterLoopLabels(instructions)
machine_language_instructions_array = secondMarch(instructions_without_labels)

toWrite = file_name.capitalize()+".hack"
f = open(toWrite, "w")
for instruction in machine_language_instructions_array:
    f.write(instruction+"\n")
f.close()

//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 0         // initializes sum = 0
@0
D=A
@LCL
A=M+D
D=A
@location0
M=D
@SP
A=M-1
D=M
@location0
A=M
M=D
@SP
M=M-1
//label LOOP_START
(LOOP_START)
//push argument 0
@0
D=A
@ARG
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 0
@0
D=A
@LCL
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=M+D
//pop local 0	        // sum = sum + counter
@0	
D=A
@LCL
A=M+D
D=A
@location2
M=D
@SP
A=M-1
D=M
@location2
A=M
M=D
@SP
M=M-1
//push argument 0
@0
D=A
@ARG
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D
//pop argument 0      // counter--
@0
D=A
@ARG
A=M+D
D=A
@location4
M=D
@SP
A=M-1
D=M
@location4
A=M
M=D
@SP
M=M-1
//push argument 0
@0
D=A
@ARG
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//if-goto LOOP_START
@SP
M=M-1
A=M
D=M
@LOOP_START
D;JGT
//push local 0
@0
D=A
@LCL
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 10
@10
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 0
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
//push constant 21
@21
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 22
@22
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop argument 2
@2
D=A
@ARG
A=M+D
D=A
@location1
M=D
@SP
A=M-1
D=M
@location1
A=M
M=D
@SP
M=M-1
//pop argument 1
@1
D=A
@ARG
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
//push constant 36
@36
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop this 6
@6
D=A
@THIS
A=M+D
D=A
@location3
M=D
@SP
A=M-1
D=M
@location3
A=M
M=D
@SP
M=M-1
//push constant 42
@42
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 45
@45
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop that 5
@5
D=A
@THAT
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
//pop that 2
@2
D=A
@THAT
A=M+D
D=A
@location5
M=D
@SP
A=M-1
D=M
@location5
A=M
M=D
@SP
M=M-1
//push constant 510
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop temp 6
@SP
A=M-1
D=M
@11
M=D
@SP
M=M-1
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
//push that 5
@5
D=A
@THAT
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
//push argument 1
@1
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
//sub
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D
//push this 6
@6
D=A
@THIS
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push this 6
@6
D=A
@THIS
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
//sub
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D
//push temp 6
@11
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

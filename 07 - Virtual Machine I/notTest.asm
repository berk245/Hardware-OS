@SP
M=M-1
A=M
D=M
@ZERO
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@END
0;JMP
(ZERO)
@SP
A=M
M=1
@SP
M=M+1
@END
0;JMP
(END)
@END
0;JMP
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
M=M-1
A=M 
D=M
@SP
A=M-1
D=D-M
@Equal0
D;JEQ
@SP
A=M-1
M=0
@End0
0;JMP
(Equal0)
@SP
A=M-1
M=-1
(End0)
@End0
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
M=M-1
A=M 
D=M
@SP
A=M-1
D=D-M
@Equal1
D;JEQ
@SP
A=M-1
M=0
@End1
0;JMP
(Equal1)
@SP
A=M-1
M=-1
(End1)
@End1
//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
M=M-1
A=M 
D=M
@SP
A=M-1
D=D-M
@Equal2
D;JEQ
@SP
A=M-1
M=0
@End2
0;JMP
(Equal2)
@SP
A=M-1
M=-1
(End2)
@End2
//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@Smaller3
D;JLT
@SP
A=M-1
M=0
@End32

0;JMP

(Smaller3)
@SP
A=M-1

M=-1
(End32)
@End32
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@Smaller4
D;JLT
@SP
A=M-1
M=0
@End42

0;JMP

(Smaller4)
@SP
A=M-1

M=-1
(End42)
@End42
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@Smaller5
D;JLT
@SP
A=M-1
M=0
@End52

0;JMP

(Smaller5)
@SP
A=M-1

M=-1
(End52)
@End52
//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@Greater6
D;JGT
@SP
A=M-1
M=0
@End6
0;JMP
(Greater6)
@SP
A=M-1
M=-1
(End6)
@End6
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@Greater7
D;JGT
@SP
A=M-1
M=0
@End7
0;JMP
(Greater7)
@SP
A=M-1
M=-1
(End7)
@End7
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
M=M-1
A=M-1
D=M
@SP
A=M
D=D-M
@Greater8
D;JGT
@SP
A=M-1
M=0
@End8
0;JMP
(Greater8)
@SP
A=M-1
M=-1
(End8)
@End8
//push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 53
@53
D=A
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
//push constant 112
@112
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
//neg
@SP
A=M-1
M=-M
//and
@SP
M=M-1
A=M
D=M
@SP
A=M-1
D=D&M
M=D
//push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
//or
@SP
M=M-1
A=M
D=M
@SP
A=M-1
D=D|M
M=D
//not
@SP
A=M-1
M=!M

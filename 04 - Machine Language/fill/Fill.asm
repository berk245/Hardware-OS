// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.




//Listen to the keyboard endlessly
    //Change R0 when key pressed

(LOOP1)
@SCREEN
  D=A
@address
  M=D
@address
    D=M
@R0
  M=D
@KBD
  D=M
@R3
  M=D
@CLEAR
 D;JEQ
@FILL
 D;JGT

(FILL)
(LOOP3)
@address
  A = M
  M = -1
@address
  M = M+1
@24576
  D=A
@address
  D= D-M
@LOOP3
 D;JGT
@END
 D;JEQ

 

(CLEAR)
(LOOP2)
@address
  A = M
  M = 0
@address
  M = M+1
@24576
  D=A
@address
  D= D-M
@LOOP2
 D;JGT
@END
 D;JEQ


(END)

@LOOP1
0;JMP





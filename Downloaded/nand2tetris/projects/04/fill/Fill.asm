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

(START)
@SCREEN
D=A
@R0
M=D

@24576
D=A
@R1
M=D

@temp
M=-1

(LOOP)
@24576
D=M
@SWITCH
D;JEQ

(CONT)
@temp
D=M
@R0
A=M
M=D

@R0
M = M+1
D=M
@R1
D = D-M
@START
D;JEQ

@LOOP
0;JMP

(SWITCH)
@temp
M=0
@CONT
0;JMP

(END)
@START
0;JMP




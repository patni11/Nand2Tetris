// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

//Take value in R0 and store it in a variable caled value1
@R0
D=M
@value1
M=D

//Take value in R1 and store it in a variable caled value2
@R1
D=M
@value2
M=D

//SET R2 to 0
@R2 
M=0

// IF value2 is 0 END THE PROGRAM
@value2
D=M
@END
D; JEQ

// Loop. Add value1 to r2 as long as value2 is above 0
(LOOP)

//Take value in R2, and value1, then add them and store in R2
@R2
D=M
@value1
D = D + M
@R2
M=D

//Reduce value2 by 1
@value2
M=M-1
D=M

//Loop as long as value2 is > 0
@LOOP
D; JGT

//END THE PROGRAM
(END)
@END
0; JMP




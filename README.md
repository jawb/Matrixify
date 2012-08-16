<<<<<<< HEAD
‎#Matrixify
#‎#What's Matrixify:
Matrixify is a **Sublime text 2 plugin** that facilitates formatting lines of code into matrix shape.

If you dealt with a code with large data sets inside an array, list or a map like Hex data or countries list for example.
Then it's interesting to format it into a matrix shape , that's much elegant than a single line or element per line approach and make the code readable and compact.
#‎#How to use it:
=======
#Matrixify
##What's Matrixify:
Matrixify is a **Sublime text 2 plugin** that make it easy to format lines of code into matrix shape.

If you dealt with a code with large data sets inside an array, list or a map like Hex data or countries list for example.
Then it's interesting to format it in a matrix shape , that's much elegant than a single line or element per line approach and make the code readable and compact.
##How to use it:
>>>>>>> 206c8fbd4da940218feaa06c139a376de8787930
To use Matrixify you need to follow the steps:

* Choose lines that would be formated.
* Above the lines you have to write a format line (described below).
* Select the lines and use Edit > Matrixify or use the keyboard shortcut Ctrl+Alt+X (Ctrl+Super+X on Mac).
You can also use multiple selections but every region must have the format line.

<<<<<<< HEAD
#‎#Writing the format line:
A format line specify the position of each line with the character "%" and separators that will separate columns of the matrix.
**P.S:** the number of "%" used in the format line indicates the number of columns in the matrix.
#‎#Examples:
###‎#Example 1:
```
  %,%,%,      <-- Format line
=======
##Writing the format line:
A format line specify the position of each line with the caracter "%" and separators that will separate columns of the matrix.
**P.S:** the number of "%" used in the format line indicate the number of columns in the matrix.
##Examples:
####Example 1:
```
  %,%,%,
>>>>>>> 206c8fbd4da940218feaa06c139a376de8787930
  a
  b
  c
  d
  e
  f
  g
  h
  i
  j
  k
```
```
a,b,c,
d,e,f,
g,h,i,
j,k
```
<<<<<<< HEAD
###‎#Example 2:
```
>> %,-%,--%,---%, &&     <-- Format line
=======
####Exaple 2:
```
>> %,-%,--%,---%, &&
>>>>>>> 206c8fbd4da940218feaa06c139a376de8787930
aaa
b
cc
d
e
f
g
h
i
jjjjj
k
l
m
nnnnnn
o
pppppppp
q
```
```
>> aaa,-b     ,--cc,---d       , &&
>> e  ,-f     ,--g ,---h       , &&
>> i  ,-jjjjj ,--k ,---l       , &&
>> m  ,-nnnnnn,--o ,---pppppppp, &&
>> q  
<<<<<<< HEAD
```
=======
```
>>>>>>> 206c8fbd4da940218feaa06c139a376de8787930

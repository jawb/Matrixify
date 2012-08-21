‎
#Matrixify

##What's Matrixify:
Matrixify is a **Sublime text 2 plugin** that facilitates formatting lines of code into matrix shape.

If you dealt with a code with large data sets inside an array, list or a map like Hex data or countries list for example.
Then it's interesting to format it into a matrix shape , that's much elegant than a single line or element per line approach and make the code readable and compact.

##How to use it:
To use Matrixify select the lines and use one of these three methods:
  1. From menu **Edit > Matrixify**.
  2. Keyboard shortcut **Ctrl+Alt+X** or **Ctrl+Super+X** on Mac (Change the key binding in case of conflict).
  3. The command **Matrixify** from the command palette.

Then enter your format line (described below) in the input field and press Enter.

You can also use multiple selections, but the format line will be applied to all of them.

##Writing the format line:
A format line specify the position of each line with the character "%" and separators that will separates columns of the matrix.

**P.S:** The number of "%" used in the format line indicates the number of columns in the matrix.

####Example 1:
```
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
--------Format line--------
%,%,%,
```
####Output:
```
a,b,c,
d,e,f,
g,h,i,
j,k
```
####Example 2:
```
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
--------Format line--------
>> %,-%,--%,---%, &&
```
####Output:
```
>> aaa,-b     ,--cc,---d       , &&
>> e  ,-f     ,--g ,---h       , &&
>> i  ,-jjjjj ,--k ,---l       , &&
>> m  ,-nnnnnn,--o ,---pppppppp, &&
>> q  
```
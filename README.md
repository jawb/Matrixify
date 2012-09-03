‎
#Matrixify 2.0

##What's Matrixify:
Matrixify is a **Sublime text 2 plugin** that facilitates formatting lines of code into matrix shape.

If you dealt with a code with large data sets inside an array, list or a map like Hex data or countries list for example.
Then it's interesting to format it into a matrix shape , that's much elegant than a single line or element per line approach and make the code readable and compact.

##How to use it:
Matrixify has 5 modes :
###1-Default (requires format and uses lines):
Can be accessed :
  1. From menu **Edit > Matrixify**.
  2. Keyboard shortcut **ctrl+super+x**
  3. The command **Matrixify** from the command palette.

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
--------Format: %,%,%,--------
```
####Output:
```
a,b,c,
d,e,f,
g,h,i,
j,k
```
###2-Auto (uses lines and automatic format):
Can be accessed using keyboard shortcut **ctrl+super+keypadi , i in [1-9]**.

####Example 2:
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
--------Press ctrl+super+keypad3--------
```
####Output:
```
a,b,c,
d,e,f,
g,h,i,
j,k
```

###3-Separator (requires format):
Can be accessed using keyboard shortcut **alt+super+i , i is ',' or ';' **.

####Example 3:
```
a;b;c;d;e;f;g;h;i;j;k
--------Press alt+super+;--------
----------Format %,%,%,----------
```
####Output:
```
a,b,c,
d,e,f,
g,h,i,
j,k
```

###4-Separator Auto (requires separator):
Can be accessed using keyboard shortcut **alt+super+keypadi , i in [1-9]**.
####Example 4:
```
a _ b _ c _ d _ e _ f _ g _ h _ i _ j _ k
--------Press alt+super+keypad3--------
-----------Separator: " _ " -----------
```
####Output:
```
a,b,c,
d,e,f,
g,h,i,
j,k
```
###5-Verbose (requires format and separator):
Can be accessed using keyboard shortcut **ctrl+super+s**.
You should enter a valid python tuple (format,separator).
####Example 5:
```
a::b::c::d::e::f::g::h::i::j::k
--------Input: ("%  %  %","::")--------
```
####Output:
```
a  b  c
d  e  f
g  h  i
j  k
```

**P.S:** You can also use multiple selections, but the format line will be applied to all of them.

##Writing the format line:
A format line specify the position of each line with the character "%" and separators that will separates columns of the matrix.

**P.S:** The number of "%" used in the format line indicates the number of columns in the matrix.

####Example 6:
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
-----Format: >> %,-%,--%,---%, &&-----
```
####Output:
```
>> aaa,-b     ,--cc,---d       , &&
>> e  ,-f     ,--g ,---h       , &&
>> i  ,-jjjjj ,--k ,---l       , &&
>> m  ,-nnnnnn,--o ,---pppppppp, &&
>> q
```

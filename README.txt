# DSP
python program to convolute or correlate 2 signals

to use the code download the file and make another python file in the same directory
#import the module

from dts import dts

#declaring the variables dts(vec,z) vec is the signal and z impiles where the zero is at relative to starting element
x = dts([0,1,2,3],1)
h = dts([1,1,2,1],1)

#x*h is convolution
x*h
#x^h is corelation
x^h

# Sample output for convolution

x[n] convolution h[n]
given x[n]  : [ 0^ 1 2 3 ]
given h[n]  : [ 1^ 1 2 1 ]
hence h[-n] : [ 1 2 1 1^ ]

n ranges in lim(x[n])+lim(h[n]) from 0 to 6

y[0]=summation(x[n]*h[0-n])
y[0]=summation([ 0^ 1 2 3 ].[ 1 2 1 1^ ])
y[0]=0

y[1]=summation(x[n]*h[1-n])
y[1]=summation([ 0^ 1 2 3 ].[ 1 2 1^ 1 ])
y[1]=1

y[2]=summation(x[n]*h[2-n])
y[2]=summation([ 0^ 1 2 3 ].[ 1 2^ 1 1 ])
y[2]=3

y[3]=summation(x[n]*h[3-n])
y[3]=summation([ 0^ 1 2 3 ].[ 1^ 2 1 1 ])
y[3]=7

y[4]=summation(x[n]*h[4-n])
y[4]=summation([ 0^ 1 2 3 ].[ 0^ 1 2 1 1 ])
y[4]=8

y[5]=summation(x[n]*h[5-n])
y[5]=summation([ 0^ 1 2 3 ].[ 0^ 0 1 2 1 1 ])
y[5]=8

y[6]=summation(x[n]*h[6-n])
y[6]=summation([ 0^ 1 2 3 ].[ 0^ 0 0 1 2 1 1 ])
y[6]=3
hence y[n]=[ 0^ 1 3 7 8 8 3 ]

# Sample output for corelation

x[n] correlation h[n]
given x[n]  : [ 0^ 1 2 3 ]
given h[n]  : [ 1^ 1 2 1 ]

n ranges in lim(x[n])+lim(h[-n]) from -3 to 3

y[-3]=summation(x[n]*h[n+-3])
y[-3]=summation([ 0^ 1 2 3 ].[ 1 1 2 1^ ])
y[-3]=0

y[-2]=summation(x[n]*h[n+-2])
y[-2]=summation([ 0^ 1 2 3 ].[ 1 1 2^ 1 ])
y[-2]=1

y[-1]=summation(x[n]*h[n+-1])
y[-1]=summation([ 0^ 1 2 3 ].[ 1 1^ 2 1 ])
y[-1]=4

y[0]=summation(x[n]*h[n+0])
y[0]=summation([ 0^ 1 2 3 ].[ 1^ 1 2 1 ])
y[0]=8

y[1]=summation(x[n]*h[n+1])
y[1]=summation([ 0^ 1 2 3 ].[ 0^ 1 1 2 1 ])
y[1]=9

y[2]=summation(x[n]*h[n+2])
y[2]=summation([ 0^ 1 2 3 ].[ 0^ 0 1 1 2 1 ])
y[2]=5

y[3]=summation(x[n]*h[n+3])
y[3]=summation([ 0^ 1 2 3 ].[ 0^ 0 0 1 1 2 1 ])
y[3]=3
hence y[n]=[ 0 1 4 8^ 9 5 3 ]

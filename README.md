# DSP

only need to download dsp.py and put it in ur current directory of python file to work

python program to perform discrete time operations

check tutorial.py for sample uses

## This Module can perform Addition ,Subsraction, Dot-product, Convolution, Corelation, Scalar-product, Right and Left Shifting time, Time-scaling, Time reversal, Z-Transform, Fourier-Transform and more On discrete time Signals
<p>

## Sample output for addition
adding signals([ 0^ 1 2 3 ],[ 1^ 1 2 1 ])
range is 0,4

y[0]=x[0]+h[0]=1+0=1

y[1]=x[1]+h[1]=1+1=2

y[2]=x[2]+h[2]=2+2=4

y[3]=x[3]+h[3]=1+3=4

hence y = [ 1^ 2 4 4 ]

## Sample output for Subsraction
substracting signals ([ 0^ 1 2 3 ],[ 1^ 1 2 1 ])
range is 0,4

y[0]=x[0]-h[0]=0-1=-1

y[1]=x[1]-h[1]=1-1=0

y[2]=x[2]-h[2]=2-2=0

y[3]=x[3]-h[3]=3-1=2

hence y = [ -1^ 0 0 2 ]

## Sample output for dot_product

multipyting signals([ 0^ 1 2 3 ],[ 1^ 1 2 1 ])
range is 0,4

y[0]=x[0]*h[0]=1*0=0

y[1]=x[1]*h[1]=1*1=1

y[2]=x[2]*h[2]=2*2=4

y[3]=x[3]*h[3]=1*3=3

hence y = [ 0^ 1 4 3 ]


## Sample output for convolution

x[n] convolution h[n]
  
given x[n]  : [ 0^ 1 2 3 ]
  
given h[n]  : [ 1^ 1 2 1 ]
  
hence h[-n] : [ 1 2 1 1^ ]

n ranges in lim(x[n])+lim(h[n]) from 0 to 6

y[0]=Σ(x[n]*h[0-n])
  
y[0]=Σ([ 0^ 1 2 3 ].[ 1 2 1 1^ ])
  
y[0]=0

  
y[1]=Σ(x[n]*h[1-n])
  
y[1]=Σ([ 0^ 1 2 3 ].[ 1 2 1^ 1 ])
  
y[1]=1
  

y[2]=Σ(x[n]*h[2-n])
  
y[2]=Σ([ 0^ 1 2 3 ].[ 1 2^ 1 1 ])
  
y[2]=3
  

y[3]=Σ(x[n]*h[3-n])
  
y[3]=Σ([ 0^ 1 2 3 ].[ 1^ 2 1 1 ])
  
y[3]=7
  

y[4]=Σ(x[n]*h[4-n])
  
y[4]=Σ([ 0^ 1 2 3 ].[ 0^ 1 2 1 1 ])
  
y[4]=8
  

y[5]=Σ(x[n]*h[5-n])
  
y[5]=Σ([ 0^ 1 2 3 ].[ 0^ 0 1 2 1 1 ])
  
y[5]=8

y[6]=Σ(x[n]*h[6-n])
  
y[6]=Σ([ 0^ 1 2 3 ].[ 0^ 0 0 1 2 1 1 ])
  
y[6]=3
  
hence y[n]=[ 0^ 1 3 7 8 8 3 ]
  

## Sample output for corelation

x[n] correlation h[n]
  
given x[n]  : [ 0^ 1 2 3 ]
  
given h[n]  : [ 1^ 1 2 1 ]

n ranges in lim(x[n])+lim(h[-n]) from -3 to 3

y[-3]=Σ(x[n]*h[n+-3])
  
y[-3]=Σ([ 0^ 1 2 3 ].[ 1 1 2 1^ ])
  
y[-3]=0

  
y[-2]=Σ(x[n]*h[n+-2])
  
y[-2]=Σ([ 0^ 1 2 3 ].[ 1 1 2^ 1 ])
  
y[-2]=1
  

y[-1]=Σ(x[n]*h[n+-1])
  
y[-1]=Σ([ 0^ 1 2 3 ].[ 1 1^ 2 1 ])
  
y[-1]=4
  

y[0]=Σ(x[n]*h[n+0])
  
y[0]=Σ([ 0^ 1 2 3 ].[ 1^ 1 2 1 ])
  
y[0]=8
  

y[1]=Σ(x[n]*h[n+1])
  
y[1]=Σ([ 0^ 1 2 3 ].[ 0^ 1 1 2 1 ])
  
y[1]=9
  

y[2]=Σ(x[n]*h[n+2])
  
y[2]=Σ([ 0^ 1 2 3 ].[ 0^ 0 1 1 2 1 ])
  
y[2]=5
  

y[3]=Σ(x[n]*h[n+3])
  
y[3]=Σ([ 0^ 1 2 3 ].[ 0^ 0 0 1 1 2 1 ])
  
y[3]=3
  
hence y[n]=[ 0 1 4 8^ 9 5 3 ]


## Sample output Fourier Transfrom 
Fourier_Transfrom([ 0^ 1 2 3 ])

range is 0,4

y(z)=Σx[n]e**(-iwn)

n=0 -> 0

n=1 -> exp(-1.0*I*w)

n=2 -> 2*exp(-2.0*I*w)

n=3 -> 3*exp(-3.0*I*w)

hence y(z)=3*exp(-3.0*I*w) + 2*exp(-2.0*I*w) + exp(-1.0*I*w)

## Sample output for Z Transform
Z_Transfrom([ 0^ 1 2 3 ])

range is 0,4

y(z)=Σx[n]z**(-n)        

n=0 -> 0

n=1 -> 1/z

n=2 -> 2/z**2

n=3 -> 3/z**3

hence y(z)=1/z + 2/z**2 + 3/z**3
</p>

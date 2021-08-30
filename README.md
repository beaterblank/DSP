# DSP
python program to perform discrete time operations

check tutorial.py for tutorial 

# Sample output for convolution
<p>
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
  

# Sample output for corelation

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
  
</p>

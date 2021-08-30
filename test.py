from dts import dts
#steps are available only for convolution and corelation
#for right now more maybe added to disable steps just use
#x.steps = False
x = dts([7,3,4,9,5],1)
x.steps = False
h = dts([1,2,4,5,5],1)
h.steps = False
scalar = 5
print(x)                 #will print the list with ^ pointing at 0   
x[int(scalar)]=10        #assign 10 at integer coordinate
y = x[int(scalar)]       #get the value at integer coordinate   
y = x*h                  #Convolution
y = x^h                  #Corelation
y = x@h                  #Dotproduct
y = x*scalar             #Amplitude scaling  
y = x+h                  #Addition of signals
y = x-h                  #subsraction of signals
y = x.shift(int(scalar)) #time shifting
a,b = x.spread(y)        #gives the combined range of x and y   
a,b = x.range()          #provides range of x
y = x.sum()              #sum of entire signal
y = x.mul()              #multiplication of entire signal
y = len(x)               #gives the length of signal   
y = x.z_transfom()       #Z transform
y = x.fourier_transform()#Fourier trasform

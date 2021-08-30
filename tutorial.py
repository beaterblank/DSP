import dsp
#steps are available only for convolution,corelation,dotproduct
# ,addition,substraction,ztransform and fourier transform
#for right now more maybe added to disable steps just use
dsp.steps = False                      #disabling steps
x = dsp.dts([7,3,4,9,5],1)             #input dts declration  vec, pos of x=0(coordinate)
h = dsp.dts([1,2,4,5,5],1)             #input dts declaration vec, pos of x=0(coordianate)    
scalar = 5                             #initializing a scalar to use later    
print(x)                               #will print the list with ^ pointing at 0   
x[int(scalar)]=10                      #assign 10 at integer coordinate
y = x[int(scalar)]                     #get the value at integer coordinate   
y = x*h                                #Convolution
y = x^h                                #Corelation
y = x@h                                #Dotproduct
y = x*scalar                           #Amplitude scaling  
y = x+h                                #Addition of signals
y = x-h                                #subsraction of signals
y = x>>int(scalar)                     #time shifting rightside
y = x<<int(scalar)                     #time shifting leftside
y = x[::-1]                            #time reversal
t = x^(abs(int(scalar))+1)             #time scaling (only upsampling)
a,b = x.spread(y)                      #gives the combined range of x and y   
a,b = x.range()                        #provides range of x
y = x.sum()                            #sum of entire signal
y = x.mul()                            #multiplication of entire signal
y = len(x)                             #gives the length of signal   
y = x.z_transform()                    #Z transform
y = x.z_transform(int(scalar))         #Z transform at a location
y = x.fourier_transform()              #Fourier trasform
y = x.fourier_transform(int(scalar))   #Fourier trasform at a location
del x[int(scalar)]                     #Deltes the sample at the coordinate
#version control - 0.0
#under devlopment 
#-----------------------------------------------------------#
#-------------------import statements-----------------------#
#-----------------------------------------------------------#
#sympy required for fourier and z transform
try:
    import sympy
except:
    #if not installed install
    import os
    os.system("pip install sympy")
#-----------------------------------------------------------#
steps = True #global variable to dictate if steps are to be printed or not
#-----------------------------------------------------------#
#-----------------------dts class---------------------------#
#-----------------------------------------------------------#
class dts:
    #constructor takes in a vec and zero location
    def __init__(self,vec=[0],z=1) -> None:
        self.vec = vec
        self.z = z
        #if the zero location is not present add 0's to make it present
        if(self.z<0):
            self.vec = [0]*(self.z*-1)+self.vec
            self.z=0
        elif(self.z>len(self.vec)):
            self.vec += [0]*(self.z-len(self.vec))
            self.z-=1
        else:
            self.z-=1
    #get method takes input as like a list and can handle a format of slicing
    def __getitem__(self, key):
        #if given query is a slice 
        if isinstance(key,slice):
            if(key.step==-1):
                temp = dts([0]*len(self.vec),self.z)
                l = self.range()
                for i in range(l[0],l[1]):
                    temp[-i] = self[i]
                while(temp.vec[-1]==0):
                    del temp.vec[-1]
                return temp
        #if given query is a int
        elif isinstance(key,int):  
            if(key+self.z<0 or key+self.z>=len(self.vec)):
                return 0  
            return self.vec[key+self.z]
    #set method takes in key and value and sets the object accordigly
    def __setitem__(self, key, value):
        if(key+self.z>=len(self.vec)):
            self.vec += [0]*(key+self.z-len(self.vec)+1)
        if(key+self.z<0):
            self.vec = [0]*((key+self.z)*-1)+self.vec
            self.z+=(key+self.z)*-1
        self.vec[key+self.z]=value
    #method to delete item
    def __delitem__(self, key):
        if(key+self.z<0 or key+self.z>=len(self.vec)):
            return
        del self.vec[key+self.z]
        if(key<self.z):
            self.z-=1
            return
    #str conversion of the class
    def __str__(self) -> str:
        string = "[ "
        for i,j in enumerate(self.vec):
            string+=str(j)
            if(i==self.z):
                string+="^"
            string+=" "
        string+="]"
        return string
    #wrapper of the class
    def __repr__(self) -> str:
        return self.__str__()
    #shifting the class
    def __lshift__(self,x):
        x*=-1
        if(isinstance(x,int)):
            temp = dts(self.vec,self.z+1)
            temp.z+=x
            if(temp.z<0):
                temp.vec = [0]*((temp.z*-1))+temp.vec
                temp.z=0
            elif(temp.z>len(temp.vec)):
                temp.vec += [0]*(temp.z-len(temp.vec))
                temp.z-=1
            return temp
        else:
            return self
    def __rshift__(self,x):
        if(isinstance(x,int)):
            temp = dts(self.vec,self.z+1)
            temp.z+=x
            if(temp.z<0):
                temp.vec = [0]*((temp.z*-1))+temp.vec
                temp.z=0
            elif(temp.z>len(temp.vec)):
                temp.vec += [0]*(temp.z-len(temp.vec))
                temp.z-=1
            return temp
        else:
            return self
    def range(self):
        pos = len(self.vec)-self.z
        neg = -self.z
        return (neg,pos)
    def __len__(self):
        return len(self.vec)
    def __add__(self,other):
        string = f"\nadding signals({self},{other})"
        y = dts()
        lo = other.range()
        ls = self.range()
        pos = max(lo[1],ls[1])
        neg = min(lo[0],ls[0])
        string +=f"\nrange is {neg},{pos}"
        for i in range(neg,pos):
            string+=f"\n\ny[{i}]=x[{i}]+h[{i}]={other[i]}+{self[i]}={other[i]+self[i]}"
            y[i]=other[i]+self[i]
        string+=f"\n\nhence y = {y}"
        if(steps):
            print(string)
        return y
    def __sub__(self,other):
        string=f"\nsubstracting signals ({self},{other})"
        y = dts()
        lo = other.range()
        ls = self.range()
        pos = max(lo[1],ls[1])
        neg = min(lo[0],ls[0])
        string +=f"\nrange is {neg},{pos}"
        for i in range(neg,pos):
            string+=f"\n\ny[{i}]=x[{i}]-h[{i}]={self[i]}-{other[i]}={-other[i]+self[i]}"
            y[i]=self[i]-other[i]
        string+=f"\n\nhence y = {y}"
        if(steps):
            print(string)
        return y
    def spread(self,other):
        lo = other.range()
        ls = self.range()
        pos = max(lo[1],ls[1])
        neg = min(lo[0],ls[0])
        return (neg,pos)
    def __matmul__(self,other):
        string=f"\nmultipyting signals({self},{other})"
        y = dts()
        neg,pos = self.spread(other)
        string +=f"\nrange is {neg},{pos}"
        for i in range(neg,pos):
            string+=f"\n\ny[{i}]=x[{i}]*h[{i}]={other[i]}*{self[i]}={other[i]*self[i]}"
            y[i]=other[i]*self[i]
        string+=f"\n\nhence y = {y}"
        if(steps):
            print(string)
        return y
    def sum(self):
        s = 0
        for i in self.vec:
            s+=i
        return s
    def mul(self):
        s = 1
        for i in self.vec:
            s*=i
        return s
    def __mul__(self,other):
        if(isinstance(other,dts)):
            string = ""
            string+="given x[n]  : "+str(self)+"\ngiven h[n]  : "+str(other)
            temp = other[::-1]
            string+="\nhence h[-n] : "+str(temp)
            neg1,pos1 = self.range()
            neg2,pos2 = other.range()
            neg = neg1+neg2
            pos = pos1+pos2-2
            string+="\n\nn ranges in lim(x[n])+lim(h[n]) from "+str(neg)+" to "+str(pos)
            y = dts([0]*(abs(neg)+pos),neg)
            for i in range(neg,pos+1):
                string+=f"\n\ny[{i}]=Σ(x[n]*h[{i}-n])\ny[{i}]=Σ({self}.{temp<<i})\ny[{i}]={(self@(temp<<i)).sum()}"
                y[i] = (self@(temp<<i)).sum()
            while(y.vec[-1]==0):
                del y.vec[-1] 
            string+="\nhence y[n]="+str(y)
            if(steps):
                print(string)
            return y
        if(isinstance(other,float) or isinstance(other,int)):
            temp = self
            neg,pos = temp.range()
            for i in range(neg,pos):
                temp.vec[i]*=other
            return temp
    def __xor__(self,other):
        if(isinstance(other,dts)):
            string = ""
            string+="given x[n]  : "+str(self)+"\ngiven h[n]  : "+str(other)
            temp = other
            neg1,pos1 = self.range()
            neg2,pos2 = other[::-1].range()
            neg = neg1+neg2
            pos = pos1+pos2-2
            string+="\n\nn ranges in lim(x[n])+lim(h[-n]) from "+str(neg)+" to "+str(pos)
            y = dts([0]*(abs(neg)+pos),neg)
            for i in range(neg,pos+1):
                string+=f"\n\ny[{i}]=Σ(x[n]*h[n+{i}])\ny[{i}]=Σ({self}.{temp<<i})\ny[{i}]={(self@(temp<<i)).sum()}"
                y[i] = (self@(temp<<(i))).sum()
            while(y.vec[-1]==0):
                del y.vec[-1] 
            string+="\nhence y[n]="+str(y)
            if(steps):
                print(string)
            return y
        if(isinstance(other,int)):
            if(other>=1):
                temp = dts()
                neg,pos = self.range()
                for i in range(other*neg,other*pos):
                    temp[i]=self[int(i/other)]
                return temp
        return self
    def __eq__(self,other) -> bool:
        if(isinstance(other,dts) and self.vec==other.vec and self.z==other.z):
            return True
        return False
    def z_transform(self,at=None):
        string=f"\nZ_Transfrom({self})"
        temp = dts(self.vec,self.z+1)
        neg,pos = temp.range()
        y = 0
        z = sympy.symbols('z')
        string+=f"\n\nrange is {neg},{pos}"
        string+=f"\n\ny(z)=Σx[n]z**(-n)"
        for n in range(neg,pos):
            string+=f"\n\nn={n} -> {temp[n]*(z**(-n))}"
            y+=temp[n]*(z**(-n))
        if(at):
            return y.subs(z,at)
        string+=f"\n\nhence y(z)={y}"
        if(steps):
            print(string)
        return y
    def fourier_transform(self,at=None):
        string=f"\nFourier_Transfrom({self})"
        temp = dts(self.vec,self.z+1)
        neg,pos = temp.range()
        y = 0
        w = sympy.symbols('w')
        c = -1j
        string+=f"\n\nrange is {neg},{pos}"
        string+=f"\n\ny(z)=Σx[n]e**(-iwn)"
        for n in range(neg,pos):
            string+=f"\n\nn={n} -> {temp[n]*(sympy.exp(c*w*n))}"
            y+=temp[n]*(sympy.exp(c*w*n))
            pass
        string+=f"\n\nhence y(z)={y}"
        if(at):
            return y.subs(w,at)
        if(steps):
            print(string)
        return y
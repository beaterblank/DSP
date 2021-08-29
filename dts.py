class dts:
    def __init__(self,vec=[0],z=1) -> None:
        self.vec = vec
        self.z = z
        self.steps = True
        if(self.z<0):
            self.vec = [0]*(self.z*-1)+self.vec
            self.z=0
        elif(self.z>len(self.vec)):
            self.vec += [0]*(self.z-len(self.vec))
            self.z-=1
        else:
            self.z-=1
    def __getitem__(self, key):
        if isinstance(key,slice):
            if(key.step==-1):
                temp = dts([0]*len(self.vec),self.z)
                l = self.range()
                for i in range(l[0],l[1]):
                    temp[-i] = self[i]
                while(temp.vec[-1]==0):
                    del temp.vec[-1]
                return temp
        elif isinstance(key,int):  
            if(key+self.z<0 or key+self.z>=len(self.vec)):
                return 0  
            return self.vec[key+self.z]

    def __setitem__(self, key, value):
        if(key+self.z>=len(self.vec)):
            self.vec += [0]*(key+self.z-len(self.vec)+1)
        if(key+self.z<0):
            self.vec = [0]*((key+self.z)*-1)+self.vec
            self.z+=(key+self.z)*-1
        self.vec[key+self.z]=value
    def __delitem__(self, key):
        self[key]=0
    def __str__(self) -> str:
        while(self.vec[-1]==0):
            del self.vec[-1]
        string = "[ "
        for i,j in enumerate(self.vec):
            string+=str(j)
            if(i==self.z):
                string+="^"
            string+=" "
        string+="]"
        return string
        pass
    def __repr__(self) -> str:
        return self.__str__()
    def shift(self,x):
        x*=-1
        temp = dts(self.vec,self.z+1)
        temp.z+=x
        if(temp.z<0):
            temp.vec = [0]*((temp.z*-1))+temp.vec
            temp.z=0
        elif(temp.z>len(temp.vec)):
            temp.vec += [0]*(temp.z-len(temp.vec))
            temp.z-=1
        return temp
    def range(self):
        pos = len(self.vec)-self.z
        neg = -self.z
        return (neg,pos)
    def __len__(self):
        return len(self.vec)
    def __add__(self,other):
        o = dts()
        lo = other.range()
        ls = self.range()
        pos = max(lo[1],ls[1])
        neg = min(lo[0],ls[0])
        for i in range(neg,pos):
            o[i]=other[i]+self[i]
        return o
    def spread(self,other):
        lo = other.range()
        ls = self.range()
        pos = max(lo[1],ls[1])
        neg = min(lo[0],ls[0])
        return (neg,pos)
    def __matmul__(self,other):
        o = dts()
        neg,pos = self.spread(other)
        for i in range(neg,pos):
            o[i]=other[i]*self[i]
        return o
    def sum(self):
        s = 0
        for i in self.vec:
            s+=i
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
                string+=f"\n\ny[{i}]=summation(x[n]*h[{i}-n])\ny[{i}]=summation({self}.{temp.shift(i)})\ny[{i}]={(self@temp.shift(i)).sum()}"
                y[i] = (self@temp.shift(i)).sum()
            string+="\nhence y[n]="+str(y)
            if(self.steps):
                print(string)
            return y
        if(isinstance(other,float) or isinstance(other,int)):
            temp = self
            neg,pos = temp.range()
            for i in range(neg,pos):
                temp.vec[i]*=other
            return temp
    def __xor__(self,other):
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
            string+=f"\n\ny[{i}]=summation(x[n]*h[n+{i}])\ny[{i}]=summation({self}.{temp.shift(i)})\ny[{i}]={(self@temp.shift(i)).sum()}"
            y[i] = (self@temp.shift(i)).sum()
        string+="\nhence y[n]="+str(y)
        if(self.steps):
            print(string)
        return y
    def __eq__(self,other) -> bool:
        if(isinstance(other,dts) and self.vec==other.vec and self.z==other.z):
            return True
        return False

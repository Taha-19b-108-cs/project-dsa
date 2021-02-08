class DynamicArray:
    def __init__(self):
        self.n=0
        self.capacity=1
        self.array=self.new_array(self.capacity)
    
    def __len__(self):
        Len=self.n
        return Len
    
    def __getitem__(self,k):
        if not 0<= k <= self.n:
            return "element is out of index"
        else:
            return self.array[k]
    
    def append(self,element):
        if self.n==self.capacity:
            self._resize(2*self.n)
        self.array[self.n]=element
        self.n+=1
        #return self.array
    
    def _resize(self,nc):
        x=self.new_array(nc)
        for i in range(self.n):
            x[i]=self.array[i]
            
        self.array=x
        self.capacity=nc
    
    def new_array(self,lenght):
        return [None]*lenght
    
    def Pop(self):
        element=None
        if self.n>0:
            element=self.array[self.n-1]
            self.array[self.n-1]=None
            self.n-=1
            
            if self.n <= self.capacity // 4:
                self._resize(self.capacity // 2)
        
        return element
    def Print(self):
        return self.array
    
D=DynamicArray()
print("INSERTING ELEMENT ")
D.append(1)
D.append(2)
D.append(3)
D.append(4)
D.append(5)
D.append(5)
D.append(10)
D.append(14)
print(D.Print())
print("LENGTH BEFORE DELETING")
print(D.__len__())
print("DELETING ELEMENT")
print(D.Pop())
print("LENGTH AFTER DELEING")
print(D.__len__())
D.Print()


class shift:
    
    def __init__(self):
        self.arr=[]
        self.n=0
        
        
    def inp(self):
        self.n=int(input("Enter the Length of the Array:: "))
        
        i=1
        while(i==1):
            self.p=int(input("Enter the Position:: "))
            if (self.p >= 0 and self.p < self.n):
                i = 0
            else:
                print("INVALID INPUT!! The Position should be greater than equal to 0 and less than equal to N\n")
        
        i=1
        while(i==1):
            self.d = int(input("Enter the Direction (either 0 for left or 1 for right):: "))
            if(self.d==1 or self.d==0):
                i=0
            else:
                print("INVALID INPUT!! The Entered Number should be either 0 or 1\n")
                
        print("\nNow Enter the Numbers:: ")
        for i in range(0,self.n):
            self.arr.append(int(input("Element:: ")))
        
        print("\n")
        self.shifting()
                
    def shifting(self):
        print("\nTHE ENTERED ARRAY:: "+str(self.arr))
        print("\n")
        
        if(self.d==0):
            self.arr=self.arr[self.p:]+self.arr[0:self.p]
            print("Rotated Array:: "+str(self.arr))
        else:
            self.arr = self.arr[(self.n-self.p):]+self.arr[0:(self.n-self.p)]
            print("Rotated Array:: "+str(self.arr))
    
        
ob=shift()
ob.inp()
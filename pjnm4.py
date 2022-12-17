class A:
    def _init_(self):
        print("Init of class A")
    def method1(self):
        print("this is method 1")
    def method2(self):
        print("this is method 2")


class B():#inheritence
    def _init_(self):# jb uske ps hai to uska chlega a ka nhin
        super()._init_()
        print("Init of class B")
    def method3(self):
        print("this is method 3")
    
    def method4(self):
         print("this is method 4")


class C(B,A) :#multilevelinheritence as it has b which has a in it (A,B) karke bhi likh skte
    #pr (-,-)me preference left ko milti hai
    def _init_(self):
        super()._init_()
        print("Init of class C")
    def method5(self):
        print("this is method 5")


obj=C()
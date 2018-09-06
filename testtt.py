class Test:
    def __init__(self,a=0,b=0,c=0):
        self.a=a
        self.b=b
        self.c=c

    def __repr__(self):
        return '<This is Test a:{},b:{},c{}>'.format(self.a, self.b,self.c)

    def func1(self):
        print("this is func1_1")
        self.visit={}
        print(self.visit)

        print("this is func1_2")
        self.func2()
        print(self.visit)
        print('This is func1_3')

    def func2(self):
        self.visit[1]=1
        self.visit[2]=2
        self.visit[3]=3
        print("This is func2")


# print(Test())

print(Test().func1())
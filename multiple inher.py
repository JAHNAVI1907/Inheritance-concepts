# Multiple inheritance
class base1:
    def __init__(self):
       super(base1,self).__init__()
       print("Base class1")
class base2:
    def __init__(self):
        super(base2,self).__init__()
        print("Base class2")
class derived(base1,base2):
    def __init__(self):
        super(derived,self).__init__()
        print("derived class from both both classes")
obj=derived()

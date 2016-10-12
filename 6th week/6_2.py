x=10
y=11
def foo():
    x = 20
    def bar():
        a=30
        print(a,x,y)
    bar()
    x=40
    bar()
foo()
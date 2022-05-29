def pdec(*a, **b):
    def dec(f):
        def wrap(*args, **kwargs):
            print a
            f(*args, **kwargs)
            print b
        return wrap
    return dec


@pdec(1, a=1)
def teszt(*args, **kwargs):
    print args
    print "teszt f"
    print kwargs
    # return "teszt"

teszt(2, b=2)

print

#https://www.artima.com/weblogs/viewpost.jsp?thread=240845#decorator-functions-with-decorator-arguments
class D():
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        # print self.args, self.kwargs

    def __call__(self, f):
        def wf(*args, **kwargs):
            print self.args
            f(*args, **kwargs)
            print self.kwargs
        return wf

@D(3, c=3)
def t2(*args, **kwargs):
    print args
    print "t2"
    print kwargs

t2(4, d=4)
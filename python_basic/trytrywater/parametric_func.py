# %%
def func_a(func, *args, **kwargs):
    print(func(*args, **kwargs))

def func_b(*args):
    return args

func_a(func_b, 1, 2, 3)

# %%
def outer1(fun, *args):
    print("This is outer1 function")
    fun(*args)

def inner1(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

outer1(inner1(1), 2)

# %%

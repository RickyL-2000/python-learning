# %%
from memory_profiler import profile

# %%
@profile(precision=6)
def test1():
    c = 1
    l = []
    for _ in range(10000):
        c += 1
        l.append(c)
    return c

# %%
import sys
import os

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

# %%

# from ..test.temp import test1
from python_basic.test.temp import test1

# %%
# if __name__ == "__main__":
a = test1()
print(a)


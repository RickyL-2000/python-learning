"""Numbers"""
# %%
print(17/3)
print(17 // 3)
print(17 % 3)

"""Strings"""

# %%
print('doesn\'t')
print('"Isn\'t," they said.')   ## 不会出现doc里说的那种情况啊？

# %%
# raw string: 用r打头，里面就不会用\进行转义了
print(r'C:\some\name')  ## 虽然intellisense 还是会把颜色标出来...

# %%
## concatenation
text = ('AHHHHHHHHHHHHHHH ' 
        'Hello World!')
print(text)

# %%
text2 = 'python'
print(text2[0] == text2[-0])
# negative indices start from -1

# %%

import pandas as p 

d = [0,1,2,3,4,5,6,7,8,9]

df = p.DataFrame(d)
df.columns = ['REV']

df['New_col'] = 5

# df['New_col'] = df['New_col']+11
# print (df)

# del df['New_col']

i = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
df.index = i

# print (df)

# b = df.loc['b']
# print (b)

# m = df.loc[:"d"]
# print (m)

# p = df.iloc[0:3]
# print (p)

# print (df['REV'])

# b = df.loc[df.index[:3], "REV"]
g = df.loc[df.index[:5],["REV", "New_col"]]
print (g)
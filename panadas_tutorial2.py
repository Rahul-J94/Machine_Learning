import pandas as pd
from numpy import random
import matplotlib.pyplot as plt

names = ['Rob','Mike','Mel','Adam','Breka']

random.seed(500)

random_names = [names[random.randint(low=0, high=len(names))] for i in range(1000)]

birth = [random.randint(low=0, high=1000) for i in range(1000)]

# print (random_names[:20])
# print ("+++++++++++++++++++++")
# print (birth[:20])

BirthDataset = list(zip(random_names, birth))
# print (BirthDataset[:20])

df = pd.DataFrame(data = BirthDataset, columns = ['Names', 'Birth'])
# print (df[:10])


df.to_csv('birth.txt', index = 0, header = 0)


fg = pd.read_csv('birth.txt', names = ['Names', 'Birth'])
# print (fg.info())
# print (fg.head(5))
# print (fg['Birth'].unique())
# print (fg['Birth'].describe())

name = fg.groupby('Names')
df = name.sum()
# print (df)


# Sort = df.sort_values(['Birth'], ascending= False)
# print (Sort.head(1))

# print (df['Birth'].max())

# print (df['Birth'].plot.bar())

print("The most popular name")
mf = df.sort_values(by='Birth', ascending=False)
print (mf.head(1))
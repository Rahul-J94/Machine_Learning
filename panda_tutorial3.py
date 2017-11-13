import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np

np.seed(111)

def CreateDataSet(Number=1):
	Output = []

	for i in range(Number):
		rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')
		data = np.randint(low=25, high=1000, size=len(rng))
		status = [1,2,3]
		random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]
		states = ['GA','FL','fl','NY','NJ','TX']
		random_states = [states[np.randint(low=0,high=len(states))] for i in range(len(rng))]
		Output.extend(zip(random_states, random_status, data, rng))

	return Output


dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])
# print (df.info())
# print (df.head())

# df.to_excel("dataset.xlsx", index=False)

df = pd.read_excel("dataset.xlsx",0, index_col='StatusDate')
print (df.dtypes)


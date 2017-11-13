from pandas import DataFrame, read_csv
import pandas as pd
import matplotlib.pyplot as plt


list1 = ["Rahul Jadhav", "kuldeep jadeja", "Pratik Kadam", "sushil pawar", "Daniel Beniston", "Rahul Jadhav", "Rahul Jadhav", "Ajay Salunkey", "Rahul Jadhav"]

list2 = ["rahul.j@infiny.in", "kuldeep.j@infiny.in", "pratik@infiny.in", "sushil.p@infiny.in", "daniel@kingdomsg.com", "rahulj9432@gmail.com", "rahulj9432@rediffmail.com", "ajay.s@infiny.in", "rahulj9432@yahoo.in"]

list3 = ["YypOKdhB5BrW1GSgt7MnNg", "xZDOauoOjonwHwge0Xvj4Q", "JsyMRZ8WgOc2gHscLQPVcw", "TniKxtB2f5U6mBAOY3lPXg", "L9n6ySVvrgQdIbPn7AMuxA", "_9yNetyJYOD9-djqY0iFCw", "caDN_1Lxns-syxyBYzsLzw", "ab4SFl-wA5GNAFq9JZBWpA", "D2MVSBZij5i7elhsqBIfGQ"]

list4 = [1496049921, 1497961323, 1498030138, 1498052801, 1498132920, 1499075101, 1499784730, 1501046553, 1502176467]
UserDataset = list(zip(list1,list2,list3,list4))
#print (UserDataset)

df = pd.DataFrame(data = UserDataset, columns = ['Name', 'Email', 'Activation_code','Value'])
df
#print (df)
df.to_csv('test1.csv', index=False, header=False)

ft = pd.read_csv('test1.csv', names = ['Name', 'Email', 'Activation_code', 'Value'])
print ("______________")
#print (ft.dtypes)
#print (ft.Email.dtypes)
#print (ft.Name.min())

Sort = df.sort_values(['Email'], ascending=False)
print (Sort)

df['Value'].plot()


MaxValue = df['Value'].max()

# Name associated with the maximum value
MaxName = df['Name'][df['Value'] == df['Value'].max()].values

# Text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')

print("The most popular name")
print (df[df['Value'] == df['Value'].max()])


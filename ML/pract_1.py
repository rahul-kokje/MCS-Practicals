#Write a python program to Prepare Scatter Plot (Use Forge Dataset / Iris Dataset)
import seaborn as sb
import matplotlib.pyplot as mp

data = sb.load_dataset('iris')
print(data)

fig = mp.figure()

#Comment out one of the following..
fig = fig.add_axes([0, 0, 1, 1])    #use it for jupyter notebook
fig = fig.add_subplot(111)          #use it for command line

fig.set_xlabel('Species')
fig.set_ylabel('Petal Width')

x = data['species']
y1 = data['petal_width']
y2 = data['sepal_width']

fig.scatter(x, y1, c='m', marker='+', s=100)
fig.scatter(x, y2, c='c', s=100)

mp.show()

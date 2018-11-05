import matplotlib.pyplot as plt 
import csv
x=[]
y=[]
z=[]
with open ('e1.csv','r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))
		z.append(int(row[2]))
plt.plot(x,y, label='Loaded from file!',color='black')
plt.plot(x,z, label='i rocked it!',color='white')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\n Check it out')
plt.legend()
plt.show()
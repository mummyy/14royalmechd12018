'''l=[1,2,3,4]
for i in l:
	print(i)
for j in range(10):
	print(j)'''
n=int(input("Enter the table to be printed"))
for i in range(n,n+1):
	for j in range(1,11):
		print(i,'X',j,'=',i*j)
lst=[1000,7899,4,6777777]
print(min(lst))
print(max(lst))

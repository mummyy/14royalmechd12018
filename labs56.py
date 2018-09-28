import random
count=0
def myroll():
	return random.randint(1,6)

while(count<=100):
	n=input("press r to roll the dice")
	if(n=='r'):
		r=myroll()
		count=count+r
		print("u got",r)
		print("new positon is",count)

		if(count==11):
			count=2
			print("sorry, i got snake")
		elif(count==13):
			count=34
			print("i got the ladder")
		elif(count==52):
			count=81
			print("i got the ladder")
		elif(count==93):
			count=64
			print("sorry, i got snake")
		elif(count==76):
			count=97
			print("i got the ladder")
		elif(count>100):
			count=count-r
			print("more than hundred")
		elif(count==100):
			
			print("i won the game")



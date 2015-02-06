import random
import sys
random.seed(12757231768L)
for i in range (8):
	print random.randint(5,54)

seed = random.randint(0, sys.maxint)
#can take this seed and replace it in seed()
print seed 
myRand = random.Random(seed)
print myRand 
#can also put this as a seed 

#just replicating some code i saw on Quora 
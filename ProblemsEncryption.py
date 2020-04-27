# This will enabe to match two people randomly
# //Randomly arrange sequences
import random

name = ["a", "b", "c", "d", "e"]
name1 = ["1", "2", "3", "4", "5"]

print ( random.randrange ( 2, 45 ) )

random.shuffle(name)
random.shuffle(name1)

print(name+name1)

for j in range(0,5):
    print(name[j]+" ---paired up with----  "+name1[j])

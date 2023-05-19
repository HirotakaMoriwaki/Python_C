import sys
args = sys.argv
num = int(args[1])
name = args[2]
animallist = ["giraffe", "tiger", "zebra", "elephant", "lion"]
kazu=len(animallist)
animallist.insert(num,name)
#del animallist[-1]
matsubi = animallist.pop()
print(matsubi)
animallist.sort()
print(animallist)
newlist = animallist[1:4]
print(newlist)
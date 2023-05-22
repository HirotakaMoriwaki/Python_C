from introfamily_Moriwaki import IntroFam
import sys

list_Family = sys.argv[1:]
myFam = IntroFam(list_Family[0],list_Family[1],list_Family[2])

print(myFam.name_out())
print(myFam.age_out())
print(myFam.cat_out())
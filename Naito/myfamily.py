import introfamily
import sys

args =sys.argv
name = args[1]
age = args[2]
neko = args[3]

#s1 = introfamily.intro.Intro(name,age)
#s = introfamily.IntroFam(neko)

#print(s)
#print(s1.name_out())
#print(s1.age_out())
#print(s.cat_out())

s = introfamily.IntroFam(name,age,neko)

print(s)
print(s.name_out())
print(s.age_out())
print(s.cat_out())
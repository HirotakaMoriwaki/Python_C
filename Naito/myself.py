import intro
import sys

args =sys.argv
name = args[1]
age = args[2]

s = intro.Intro(name,age)
print(s.name_out())
print(s.age_out())
import sys
from introduce_Moriwaki import Intro
list_info = sys.argv[1:]

i = Intro(list_info[0],list_info[1])
print(i.name_out())
print(i.age_out())
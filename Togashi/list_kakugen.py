import random

kakugen = [
    "能ある鷹は爪を隠す",
    "豚に真珠",
    "二兎を追う者は一兎をも得ず",
    "叩き続けなさい。そうすれば開かれます。"
]

for i in kakugen:
    print(i)
    
i = random.randint(0, len(kakugen)-1)
print(kakugen[i])
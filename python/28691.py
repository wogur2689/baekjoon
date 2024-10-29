def switch(key):
   dic = {"M": "MatKor", "W" : "WiCys", "C": "CyKor", "A" : "AlKor", "$" : "$clear"}.get(key, "")
   print(dic)

s = input()
switch(s)

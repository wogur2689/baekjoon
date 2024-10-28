def switch(key):
  school = {"NLCS": "North London Collegiate School", "BHA" : "Branksome Hall Asia", "KIS": "Korea International School", "SJA" : "St. Johnsbury Academy"}.get(key, "")
  print(school)

n = input()
switch(n)

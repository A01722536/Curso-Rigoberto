import re

match=re.search(r"eeee","eeeeeee")
print(match)
print(match.group())

match=re.search(r"igs","ieeee")
print(match)

#Metacaracteres:
#1: "."
match=re.search(r"..o","remolino")
print(match)
match=re.search(r".....o","remolino")
print(match)
match=re.search(r".........o","remolino")
print(match)

#2: "\d"
match=re.search(r"\d","mid4nldj2331lodkoedn")
print(match)
match=re.search(r"\d\d\d","mid4nldj2331lodkoedn")
print(match)
match=re.search(r"\d\d\d\d\d","mid4nldj2331lodkoedn")
print(match)
match=re.search(r"\d{4}","mid4nldj2331lodkoedn")
print(match)

#2: "\w"
match=re.search(r"\w","@@ks!s2w")
print(match)
match=re.search(r"\w\w\w","@@ks!s2w")
print(match)
match=re.search(r"\w\w\w\w","@@ks!s2w")
print(match)
match=re.search(r"\w{2}","@@ks!s2w")
print(match)
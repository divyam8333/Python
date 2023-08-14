d={"A":"Apple","B":"Boy","C":"Cat","D":"Dog"}
print(d)

#Adding new element
d["E"]="Elephant"
print(d)

#Edit or Update an Element
d["A"]="Aman"
print(d)

#delete any Key Value Pair from dict
del(d["C"])
print(d)

#Remove all Key Value Pair from dict
d.clear()
print(d)
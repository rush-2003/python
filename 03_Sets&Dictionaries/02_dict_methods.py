marks = {
    "harry" : 56,
    "Rudalph" : "100",
    "list" : [1,2,3,4]
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Rudalph":500}) #jo nahi hai vo add honge, jo hai vo update honge
print(marks.get("Rudalph"))
print(marks["Rudalph"])

print(marks.get("Rudalph2")) #prints None
print(marks["Rudalph2"]) #prints error
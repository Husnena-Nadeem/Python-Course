marks={}           #empty dictionary
marks={
    "Husnena":80,
    "sana":90,
    "tazeen":70,
    "Iram":90,
}
print(marks.items())
print(marks.values())
print(marks.keys())
marks.update({"Husnena":90})
print(marks)
print(marks.get("Husnena2"))       #return non
# print(marks["Husnena2"])           #return error
value=marks.pop("Husnena")            #remove this key or value in dictionary
print(value)        # Output: 90
print(marks)

# last_item = marks.popitem()
# print(last_item)     # Output: ('Iram', 90)
# print(marks)       # Output: {'name': 'Ali', 'age': 22}
# print(len(marks))

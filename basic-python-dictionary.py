# IN THIS MODUL WE WILL LEARN ABOUT PYTON DICTIONARY OR JSON OR REST API

users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
}

print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"]["street"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])

# WE WILL CHANGE DATA TYPE FROM DICTIONARY INTO JSON AND YOU WILL SEE THE DIFFERENT BETWEEN THEM
print("\nChange Python Dictionary into JSON")
print("This is Dictionary :")
print(users)
print(type(users))

print("\nThis is JSON :")
import json
result = json.dumps(users)
print(result)
print(type(result))

# WE WILL CONVERT JSON INTO DIFFERENT FILE WITH DUMP FUNCTION WITHOUT -S
with open ('result.json', 'w') as file:
    json.dump(users, file)


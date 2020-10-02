import json
from collections import Counter

#Open json data file and set data variable
with open('Contacts.json') as f:
      data = json.load(f)

#Parse through each contact and sort in ascending order.
data = sorted(data, key = lambda i:i['fullName'])
city_errors = []
cities = []
#Print full name and statement of validity.
for i in data:

    #If Email is invalid then set statement to "Email is invalid."
    if i['emailAddress'].count("@") == 1 and i['emailAddress'].find('@') != 0 and i['emailAddress'].find('@') != len(i['emailAddress'])-1: statement = 0
    else: statement = 1
    
    #If Phone is invalid then set statement to "Phone is invalid."
    allowed_phone = '1234567890- '
    if all(j in allowed_phone for j in i['phoneNumber']): statement += 0
    else: statement += 2

    #If both are invalid then set statement to "Email and Phone are invalid."
    #If both Email and Phone are valid then set statement to "Valid"
    if statement == 3:   statement = "Email and Phone are invalid."
    elif statement == 2: statement = "Phone is invalid."
    elif statement == 1: statement = "Email is invalid."
    else:                statement = "Valid"
    print(f'{i["fullName"]} || {statement}')
    cities.append(i['cityName'])

    if statement != "Valid":
        city_errors.append(i['cityName'])
    
print('==========================')

#List each city, list the amount of error each city has.
city = set(cities)
for item in city:
    city_errors.append(item)


sorted(city_errors,key=city_errors.count)
counts = Counter(city_errors)
for item in counts:
    print(f'{item}: {counts[item]-1} errors')

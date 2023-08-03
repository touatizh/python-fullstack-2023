#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
print("*"*5)

#2 Iterate Through a List of Dictionaries
def iterateDictionary(lst: list[dict]) -> None:
    for item in lst:
        print(f"first_name - {item['first_name']}, last_name - {item['last_name']}")
        
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
print("*"*5)

# Get Values From a List of Dictionaries
def iterateDictionary2(key: str, lst: list[dict]) -> None:
    for item in lst:
        if key not in item.keys():
            pass #to avoid throwing KeyError exception and continuing execution
        else:
            print(item[key])
iterateDictionary2("first_name", students)
iterateDictionary2('gender', students) 
print("*"*5)

#4 Iterate Through a Dictionary with List Values
def printInfo(dct: dict[list]) -> None:
    for key, value in dct.items():
        print(f"{len(value)} {key}")
        for item in value:
            print(item)
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
print(x)
x[1][0] = 15
print(x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(students)
students[0]['last_name']='Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print(sports_directory)
sports_directory['soccer'][0]='Andres'
print(sports_directory)

print(z)
z[0]['y']=30
print(z)


# # Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


    
def iterateDictionary(some_list):
    for i in range(0,len(some_list)):
        output = ""
        print(output)
        for key, val in some_list[i].items():
            output += f"{key}-{val},"
        print(output)
print (iterateDictionary(students))



# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

def iterateDictionary2(key_value, some_list):
    for i in range(0,len(some_list)):
        for key,val in some_list[i].items():
            if key == key_value:
                print(val)
print(iterateDictionary2('first_name', students))


# # Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo( dictionary):
    for key,val in dictionary.items():
        print(f"{len(val)} {key.upper()} ")
        for i in range(0, len(val)):
            print(val[i])

print(printInfo(dojo))

# # # output:
# # #7  LOCATIONS
# # San Jose
# # Seattle
# # Dallas
# # Chicago
# # Tulsa
# # DC
# # Burbank
    
# # 8 INSTRUCTORS
# # Michael
# # Amy
# # Eduardo
# # Josh
# # Graham
# # Patrick
# # Minh
# # Devon
# # None
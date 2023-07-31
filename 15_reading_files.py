employees_file=open("employees.txt", "r")
#r- read file
#w- edit file
#a- append file
#r+- read and edit file

print(employees_file.readable()) #fuction that checks if a file is readable or not and returns a boolean value
#here the value will be 'true' since we mentioned r above

# print(employees_file.read())

# print(employees_file.readline())

#print(employees_file.readlines()) #takes all the lines from the txt file and puts them into an list
#print(employees_file.readlines()[2])

for employee in employees_file.readlines():
    print(employee)


employees_file.close()
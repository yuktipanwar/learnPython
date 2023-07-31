employees_file=open("employees.txt", "a")
# employees_file=open("employees.txt", "w")
# going to overwrite on the entire file
# print(employees_file.write("\nKelly - Customer Service"))
print(employees_file.write("\nToby - Human Resources"))

employees_file.close()

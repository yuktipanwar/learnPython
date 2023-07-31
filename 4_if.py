is_female= True
is_tall= False

# if is_female or is_tall:
#     print("you are female or tall or both")
      #will return this statement if either both are true or either one of the variables are true
# else: 
#     print("you are neither male nor tall")
#will return this statement if both are false only

# if is_female and is_tall:
#     print("you are female or tall or both")
#     ##will return this statement if both are true only
# else: 
#     print("you are neither male nor tall")
    
if is_female and is_tall:
    print("you are female or tall or both")
elif is_female and not(is_tall): 
    print("you are short female")
elif not(is_female) and is_tall: 
    print("you are tall male")
else:
    print("you are neither male nor tall")
    
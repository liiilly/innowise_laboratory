def generate_profile(age=int):
 if age <=12:
   return "Child"
 elif 13<=age<=19:
    return "Teenager" 
 else:
    return "Adult"

user_name = input("Enter your full name: ")

birth_year_str = input("Enter your birh year: ")
birth_year = int(birth_year_str)
hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
       break
    else:
         hobbies.append(hobby) 
current_age = 2025-birth_year
life_stage=generate_profile(current_age)

print ("---")

user_profile = {"name" : user_name, "age" : current_age, "stage" : life_stage, "hobby" : hobbies }
print ("Profile Summary:")
print ("Name:", user_profile["name"])
print ("Age:", user_profile["age"])
print ("Life Stage:", user_profile["stage"])
if len(hobbies)!=0: 
   print (f"Favorite hobbies ({len(hobbies)}): ")
   for i in user_profile["hobby"]:
      print ('-', i)
else: 
   print ("You didn't mention any hobbies.")
print ("---")
        
            


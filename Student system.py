print("="*35)
print("--WELCOME To Student Management System--")
print("="*35)
student = {
    "name" : input("Enter name :"),
    "cgpa" : float(input("Enter CGPA :")),
    "semester":int(input("Enter semester :"))
}
while True:
    print("=======MENU=======")
    print("1.Show Student" )
    print("2.Update CGPA")
    print("3.Add Phone")
    print("4.Delete Semester")
    print("5.Exit")
    choice = int(input("Enter your choice:"))
    if choice <1 or choice > 5:
      print("Invalid choice!!")
      continue
    if choice == 1:
        for key,value in student.items():
         print(key,value)
    elif choice == 2:
       newcgpa = float(input("Enter new cgpa :")) 
       student["cgpa"] = newcgpa 
       print("CGPA Updated")
       print("New cgpa is :",newcgpa)
    elif choice == 3:
        phone = input("Enter Phone Number") 
        student["phone"] = phone  
        print("Phone number added successfully")
        print("Phone number is:", phone)
        for key,value in student.items():
           print(key,value)
    elif choice == 4:
        if "semester" in student:
         del student["semester"] 
         print("Semester deleted sucessfully")
        else:
           print("Semester already deleted")
    elif choice == 5:
       break    
    
print("="*35)
print("===Thank you for using the system===")
print("="*35)
student_names = ["James", "Katarina", "Ahri", "Zed", "Talon", "Ekko", "Ori"]

# Testing break function
for name in student_names:
    if name == "Ekko":
        print ("Found Them! " + name)
        break
    print("Currently testing " + name)

# Testing Continue function
for name in student_names:
    if name == "Zed":
        print ("Found Them! " + name)
        continue
    print("Currently testing " + name)


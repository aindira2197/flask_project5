username = "admin"
password = "1234"

while True:
    user = input("Login: ")
    parol = input("Parol: ")

    if user == username and parol == password:
        print("Tizimga kirdingiz")
        break
    else:
        print("Xato login yoki parol")

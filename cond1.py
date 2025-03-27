imkoniyat = 3

while imkoniyat > 0:
    print("#"*10)
    login = input("Login: ")
    parol = input("Parol: ")

    if login == "admin" and parol == "pwd2025**":
        print(f"Salom {login}.")
        break
    else:
        print("Notog'ri qiymat kiritildi.")

    print("#"*10)
    print("\n")
    imkoniyat -= 1

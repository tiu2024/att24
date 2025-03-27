import sys, random

print("TOSH QOG'OZ QAYCHI")

glb = 0
mglbyt = 0
drng = 0

while True:
    print(f"{glb} Galaba, {mglbyt} Mag'lubiyat, {drng} Durang")

    while True:
        qadam = input("Tanla: T (tosh), QO (qog'oz), QA (qaychi), x (tugatish): ")

        if qadam == 'x':
            sys.exit()

        if qadam == 'T' or qadam == "QO" or qadam == "QA":
            break

    if qadam == 'T':
        print("Toshga qarshi ...")

    elif qadam == "QO":
        print("Qog'ozga qarshi ...")
    else:
        print("Qaychiga qarshi ...")

    raqam = random.randint(1, 3)

    if raqam == 1:
        kompQadam = 'T'
        print("TOSH")
    elif raqam == 2:
        kompQadam = "QO"
        print("QOG'OZ")
    else:
        kompQadam = "QA"
        print("QAYCHI")

    if qadam == kompQadam:
        print("Durang!")
        drng += 1
    elif qadam == "T" and kompQadam == "QA":
        print("Siz yutdiz.")
        glb += 1
    elif qadam == "QO" and kompQadam == "TO":
        print("Siz yutdiz.")
        glb += 1
    elif qadam == "QA" and kompQadam == "QO":
        print("Siz yutdiz.")
        glb += 1
    else:
        print("Qoldiz.")
        mglbyt += 1


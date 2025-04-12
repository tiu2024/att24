import datetime

def salom(ism="hoji"):
    print(f"Qale ishlar! {ism}boy")
    print("Bolvotdimi!")
    print("Qanaqasan?")

def hafta_topish(y, o, k):
    tugilgan_sana = datetime.date(y, o, k)
    sana = datetime.date.today()

    haftalar = (sana - tugilgan_sana)

    return haftalar.days / 7

def kun_topish(y, o, k):
    kunlar = hafta_topish(y,o,k) * 7

    return kunlar

def main():
    ism = input("Nma gap? Isming nma? ")
    #salom(ism)

    while True:

        yil = int(input("Tugilgan yiling: "))
        if yil < 1924 or yil > 2025:
            print("Notog'ri yil kiritildi!")
            continue

        oy = int(input("Qaysi oy: "))
        if oy > 12 or oy < 0:
            print("Notog'ri oy kiritildi!")
            continue

        kun = int(input("Qaysi kun: "))
        if kun > 31 or kun < 0:
            print("Notog'ri oy kiritildi!")
            continue

    #haftalar = round(kun_topish(yil, oy, kun),0)
    #print(f"Dostm sen {haftalar}!")

main()


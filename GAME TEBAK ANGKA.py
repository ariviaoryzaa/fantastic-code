from random import randint as rdm
    # GAME TEBAK ANGKA
# looping program berjalan
while True:
    level =  input("masukkan level [easy/medium/hard] : ")
    while(level != "easy" and level != "medium" and level != "hard") :
        level = input("\nsorry your inut has wrong. please try again.\nMasukkan level [easy/medium/hard]: ")
    if level == "easy" :
        kesempatan = 3
        bilRandom = rdm(1,10)
    elif level == "medium" :
        kesempatan = 4
        bilRandom = rdm(1,20)
    elif level == "hard" :
        kesempatan = 5
        bilRandom = rdm(1,30)
    print("level ", level, " dengan kesempatan ", kesempatan, " kali")

# looping tebak angka
    while (kesempatan >= 0) :
        if kesempatan != 0 :
            print("kesempatan : ", kesempatan)
            tebak =  int(input("masukkan angka yang ditebak : "))
            if tebak == bilRandom :
                print("nice, bener nih.")
                break
            elif tebak > bilRandom : 
                print("angkanya dibawah ", tebak)
                kesempatan -= 1
            elif tebak < bilRandom :
                print("angkanya diatas ", tebak)
                kesempatan -= 1
        else :
            print ("angkanya :  " , bilRandom)
            print("yah gagal tebak angka nih :(")
            break

#konfirmasi ulang 
    ulang = input("Mau main lagi? :  ")
    while( ulang != "y" and ulang != "n" ) :
        ulang = input("\nMaaf inputan anda salah. silahkan coba lagi. \nmau main lagi? : ")
    if ulang == "y" :
        print("\nsilahkan main lagi.\n")
    elif ulang == "n" : 
        print("\nthankyou for the joining this game.\n")
        break
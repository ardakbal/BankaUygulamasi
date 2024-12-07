bakiye = 100
hesap_bakiyesi = float(bakiye)

while True:
    print("Arda Bankası'na hoş geldiniz!")
    print(f"Hesap bakiyeniz: {hesap_bakiyesi} TL")
    print("Yapmak istediğiniz işlemi, numarasını girerek seçebilirsiniz:\n 1 - Hesaba para yatır\n 2 - Hesaptan para çek\n 3 - Hesap bakiyesini görüntüle\n 4 - Güvenli Çıkış ")
    secim = int(input("Seçim: "))
    if secim == 1:
        print("Yatırmak istediğiniz tutarı seçiniz.\n 1 - 100 TL\n 2 - 250 TL\n 3 - 500 TL\n 4 - Başka Tutar")
        secim1 = int(input("Seçim: "))
        if secim1 == 1:
            hesap_bakiyesi += 100
            print("\n----> Hesabınıza 100 TL yatırılmıştır.")
            print(f"----> Yeni bakiyeniz: {hesap_bakiyesi} TL\n\n")

        elif secim1 == 2:
            hesap_bakiyesi += 250
            print("\n----> Hesabınıza 250 TL yatırılmıştır.")
            print(f"----> Yeni bakiyeniz: {hesap_bakiyesi} TL\n\n")

        elif secim1 == 3:
            hesap_bakiyesi += 500
            print("\n----> Hesabınıza 500 TL yatırılmıştır.")
            print(f"----> Yeni bakiyeniz: {hesap_bakiyesi} TL\n\n")

        elif secim1 == 4:
            baska_tutar = float(input("Tutarı TL cinsinden giriniz: "))
            if baska_tutar < 0:
                print("\n----> Hatalı giriş yaptınız, lütfen tekrar deneyiniz.\n\n")
            else:
                hesap_bakiyesi += baska_tutar
                print(f"\n----> Hesabınıza {baska_tutar} TL yatırılmıştır.")
                print(f"----> Yeni bakiyeniz: {hesap_bakiyesi} TL\n\n")

        else:
            print("\n---->Hatalı giriş yaptınız, lütfen tekrar deneyiniz.\n\n")
       
    elif secim == 2:
        print("Çekmek istediğiniz tutarı seçiniz.\n 1 - 100 TL\n 2 - 250 TL\n 3 - 500 TL\n 4 - Başka Tutar")
        secim2 = int(input("Seçim: "))

        if secim2 == 1:
            if 100 > hesap_bakiyesi:
                print("\n----> Yetersiz bakiye.\n\n")
            else: 
                hesap_bakiyesi -= 100
                print("\n----> Hesabınızdan 100 TL çekilmiştir.")
                print(f"----> Yeni bakiyeniz: {hesap_bakiyesi} TL\n\n")

        elif secim2 == 2:
            if 200 > hesap_bakiyesi:
                print("\n----> Yetersiz bakiye.\n\n")
            else: 
                hesap_bakiyesi -= 250
                print("\n----> Hesabınızdan 250 TL çekilmiştir.")
                print(f"----> Yeni bakiyeniz: {hesap_bakiyesi} TL\n\n")

        elif secim2 == 3:
            if 500 > hesap_bakiyesi:
                print("\n----> Yetersiz bakiye.\n\n")
            else: 
                hesap_bakiyesi -= 500
                print("\n----> Hesabınızdan 500 TL çekilmiştir.")
                print(f"----> Yeni bakiyeniz: {hesap_bakiyesi} TL\n\n")

        elif secim2 == 4:
            baska_tutar2 = float(input("Tutarı TL cinsinden giriniz: "))
            if baska_tutar2 > hesap_bakiyesi:
                print("\n----> Yetersiz bakiye.\n\n")
            elif baska_tutar2 < 0:
                print("\n----> Hatalı giriş yaptınız, lütfen tekrar deneyiniz.\n\n")
            else: 
                hesap_bakiyesi -= baska_tutar2
                print(f"\n----> Hesabınızdan {baska_tutar2} TL çekilmiştir.")
                print(f"----> Yeni bakiyeniz: {hesap_bakiyesi} TL\n\n") 
        
        else:
            print("\n----> Hatalı giriş yaptınız, lütfen tekrar deneyiniz.\n\n")
             
    elif secim == 3:
        print(f"\n---> Hesap bakiyeniz: {hesap_bakiyesi} TL\n\n")

    elif secim == 4:
        print("\n---->Güvenli çıkış yapılıyor...\n-------->Çıkış yapıldı.")
        break
 
    else:
        print("\n---->Hatalı giriş yaptınız, lütfen tekrar deneyiniz.\n\n")
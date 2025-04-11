kullanicilar_ve_bilgiler = {
    "Arda" : {"sifre": "123456", "bakiye": 1000},
    "Cem"  : {"sifre": "234567", "bakiye": 1500},
    "Barış": {"sifre": "345678", "bakiye": 2000},
    "Erkin": {"sifre": "456789", "bakiye": 2500}
}

def banka(k_adi_giris):
    while True:
        try:
            print("*"*25)
            print(f"Arda Bankası'na hoş geldin, {k_adi_giris} !")
            print(f"Hesap bakiyen: {kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]} TL")
            print("Yapmak istediğin işlemi, numarasını girerek seçebilirsin:\n 1 - Hesaba para yatır.\n 2 - Hesaptan para çek.\n 3 - Havale yap.\n 4 - Güvenli Çıkış yap.")
            print("*"*25)
            secim = int(input("Seçim: "))

            if secim == 1:
                print("*"*25)
                print("Yatırmak istediğin tutarı seç.\n 1 - 100 TL\n 2 - 250 TL\n 3 - 500 TL\n 4 - Başka Tutar")
                print("*"*25)
                secim1 = int(input("Seçim: "))
                if secim1 == 1:
                    kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"] += 100
                    print("\n----> Hesabına 100 TL yatırılmıştır.")
                    print(f"----> Yeni bakiyen: {kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]} TL\n\n")

                elif secim1 == 2:
                    kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"] += 250
                    print("\n----> Hesabına 250 TL yatırılmıştır.")
                    print(f"----> Yeni bakiyen: {kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]} TL\n\n")

                elif secim1 == 3:
                    kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"] += 500
                    print("\n----> Hesabına 500 TL yatırılmıştır.")
                    print(f"----> Yeni bakiyen: {kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]} TL\n\n")

                elif secim1 == 4:
                    baska_tutar = input("Tutarı TL cinsinden gir: ").strip()
                    if "." in baska_tutar:
                        print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")

                    elif len((str(baska_tutar))) > 9:
                        print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")

                    elif str(baska_tutar) < "0":
                        print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")
                    else:
                        kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"] += float(baska_tutar)
                        print(f"\n----> Hesabına {baska_tutar} TL yatırılmıştır.")
                        print(f"----> Yeni bakiyen: {kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]} TL\n\n")

                else:
                    print("\n---->Hatalı giriş yaptın, lütfen tekrar dene.\n\n")
            
            elif secim == 2:
                print("*"*25)
                print("Çekmek istediğin tutarı seç.\n 1 - 100 TL\n 2 - 250 TL\n 3 - 500 TL\n 4 - Başka Tutar")
                print("*"*25)
                secim2 = int(input("Seçim: "))

                if secim2 == 1:
                    if 100 > kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]:
                        print("\n----> Yetersiz bakiye.\n\n")
                    else: 
                        kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"] -= 100
                        print("\n----> Hesabından 100 TL çekilmiştir.")
                        print(f"----> Yeni bakiyen: {kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]} TL\n\n")

                elif secim2 == 2:
                    if 200 > kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]:
                        print("\n----> Yetersiz bakiye.\n\n")
                    else: 
                        kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"] -= 250
                        print("\n----> Hesabından 250 TL çekilmiştir.")
                        print(f"----> Yeni bakiyen: {kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]} TL\n\n")

                elif secim2 == 3:
                    if 500 > kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]:
                        print("\n----> Yetersiz bakiye.\n\n")
                    else: 
                        kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"] -= 500
                        print("\n----> Hesabından 500 TL çekilmiştir.")
                        print(f"----> Yeni bakiyen: {kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]} TL\n\n")

                elif secim2 == 4:
                    baska_tutar2 = input("Tutarı TL cinsinden gir: ").strip()
                    
                    if "." in baska_tutar2:
                        print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")
                             
                    elif len((str(baska_tutar2))) > 9:
                        print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")

                    elif float(baska_tutar2) > kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]:
                        print("\n----> Yetersiz bakiye.\n\n")
                    elif float(baska_tutar2) < 0:
                        print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")
                    else: 
                        kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"] -= float(baska_tutar2)
                        print(f"\n----> Hesabından {baska_tutar2} TL çekilmiştir.")
                        print(f"----> Yeni bakiyen: {kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]} TL\n\n") 
                
                else:
                    print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")

            elif secim == 3:
                print("*"*25)
                havale_kisi = str(input(f"Havale yapmak istediğin kullanıcının adını gir: ").capitalize())
                
                if havale_kisi == k_adi_giris:
                    print("\n----> Kendine para gönderemezsin.\n\n")
            
                elif havale_kisi not in kullanicilar_ve_bilgiler:
                    print("\n----> Böyle bir kullanıcı bulunamadı, lütfen tekrar dene.\n\n")
                
                else:
                    havale_tutar = input("Göndermek istediğin tutarı TL cinsinden gir: ").strip()

                    if "." in havale_tutar:
                        tam_kisim3, ondalik_kisim3 =  havale_tutar.split(".")
                             
                        if len(str(ondalik_kisim3)) > 2:
                            print("\n----> Ondalıklı kısmı hatalı girdin.\n\n")

                        elif len((str(havale_tutar))) > 9:
                            print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")

                        elif float(havale_tutar) < 0:
                            print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")
                    
                        elif float(havale_tutar) > kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]:
                            print("\n----> Yetersiz bakiye.\n\n")
                            
                        elif havale_kisi in kullanicilar_ve_bilgiler:

                            kullanicilar_ve_bilgiler[havale_kisi]["bakiye"] += float(havale_tutar)
                            kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"] -= float(havale_tutar)
                            print(f"\n----> {havale_kisi} isimli kullancıya {havale_tutar} TL havale işlemi gerçekleşmiştir.\n\n")
                                                  
                    elif len((str(havale_tutar))) > 9:
                        print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")      
                    elif float(havale_tutar) < 0:
                            print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")
                    elif float(havale_tutar) > kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"]:
                        print("\n----> Yetersiz bakiye.\n\n")
                    elif havale_kisi in kullanicilar_ve_bilgiler:

                        kullanicilar_ve_bilgiler[havale_kisi]["bakiye"] += float(havale_tutar)
                        kullanicilar_ve_bilgiler[k_adi_giris]["bakiye"] -= float(havale_tutar)
                        print(f"----> {havale_kisi} isimli kullancıya {havale_tutar} TL havale işlemi gerçekleşmiştir.\n")
                        
            elif secim == 4:
                print("*"*25)
                print("\n----> Güvenli çıkış yapılıyor...\n----> Çıkış yapıldı, görüşürüz!\n\n")
                print("*"*25)
                break
            
            else:
                print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")

        except ValueError:
            print("\n---->Hatalı giriş yaptın, lütfen tekrar dene.\n\n")

while True:
    print("*"*25)
    print("Arda Bankası'na hoş geldin!")
    oturum_secimi = input("- Oturum açmak için 1'i\n- Yeni hesap oluşturmak için 2'yi\n- Programı sonlandırmak için 3'ü seç\n----> Seçim: ")
    if oturum_secimi == "1":
            kullanici_adi = str(input("Kullanıcı adını gir: ").capitalize())

            if kullanici_adi not in kullanicilar_ve_bilgiler:
                print("\n----> Böyle bir kullanıcı bulunamadı.\n\n")
            elif not kullanici_adi:
                print("\n----> Bu alan boş bırakılamaz.\n\n")
            else:   
                kullanici_sifre = input("Şifreni gir: ")
                if kullanici_sifre == kullanicilar_ve_bilgiler[kullanici_adi]["sifre"]:
                    banka(kullanici_adi)
                else:
                    print("\n---->Hatalı giriş yaptın, lütfen tekrar dene.\n\n")

    elif oturum_secimi == "2":
        print("*"*25)
        yeni_kullanici = input("KULLANICI ADI BELİRLEME:\nKullanıcı adında sayılar ve özel karakterler bulunmamalıdır, büyük-küçük harf ve boşluklar dikkate alınmayacaktır.\nYeni kullanıcı adı: ").strip().capitalize()
        if yeni_kullanici in kullanicilar_ve_bilgiler:
            print("\n----> Bu kullanıcı adı kullanılmıştır.\n\n")
        elif not yeni_kullanici:
            print("\n----> Bu alan boş bırakılamaz.\n\n")
        elif not yeni_kullanici.isalpha():
            print("\n----> Kullanıcı adı sadece harflerden oluşmalıdır.\n\n")
        else:
            print("ŞİFRE BELİRLEME:")
            yeni_sifre = input("6 haneli ve rakamlardan oluşan şifreni belirle: ")
            if not yeni_sifre:
                print("\n----> Bu alan boş bırakılamaz.\n\n")
            elif not yeni_sifre.isdigit() and len(yeni_sifre) != 6:
                print("\n----> Şifren 6 haneli ve rakamlardan oluşmalıdır.\n\n")
            elif not yeni_sifre.isdigit():
                print("\n----> Şifren rakamlardan oluşmalıdır.\n\n")
            elif len(yeni_sifre) != 6:
                print("\n----> Şifren 6 haneli olmalıdır.\n\n")
            else:
                kullanicilar_ve_bilgiler[yeni_kullanici] = {"sifre": yeni_sifre, "bakiye": 0}
                print("*"*25)
                print(f"Hesabın başarıyla oluşturuldu, Arda Bankası'na hoş geldin {yeni_kullanici}!\nOturum açarak işlemlerine devam edebilirsin!")
    
    elif oturum_secimi == "3":
        print("*"*25)
        print("----> Program sonlandırılıyor...\nProgram sonlandırıldı!")
        print("*"*25)
        break
    else:
        print("\n----> Hatalı giriş yaptın, lütfen tekrar dene.\n\n")
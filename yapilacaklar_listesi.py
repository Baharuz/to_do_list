def menu_goster():
    print("\n----- Yapılacaklar Listesi Menüsü -----")
    print("1. Görev Ekle")
    print("2. Görev Sil")
    print("3. Listeyi Göster")
    print("4. Çıkış")


def gorev_ekle(liste):
    yeni_gorev = input("Yeni görev giriniz: ").strip()
    if yeni_gorev:
        liste.append(yeni_gorev)
        print(f"'{yeni_gorev}' başarıyla eklendi.")
    else:
        print("Boş görev eklenemez.")


def gorev_sil(liste):
    if not liste:
        print("Liste boş.")
        return

    liste_goster(liste)
    try:
        sil_index = int(input("Silmek istediğiniz görevin numarasını giriniz: "))
        if 1 <= sil_index <= len(liste):
            silinen_gorev = liste.pop(sil_index - 1)
            print(f"'{silinen_gorev}' başarıyla silindi.")
        else:
            print("Geçersiz görev numarası.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")


def liste_goster(liste):
    if not liste:
        print("Liste boş.")
    else:
        print("\n--- Yapılacaklar Listesi ---")
        for i, gorev in enumerate(liste, start=1):
            print(f"{i}. {gorev}")


def main():
    yapilacaklar = []

    while True:
        menu_goster()
        try:
            secim = int(input("Bir seçim yapın (1-4): "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue

        if secim == 1:
            gorev_ekle(yapilacaklar)
        elif secim == 2:
            gorev_sil(yapilacaklar)
        elif secim == 3:
            liste_goster(yapilacaklar)
        elif secim == 4:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main() 

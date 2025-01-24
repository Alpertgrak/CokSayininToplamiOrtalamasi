import tkinter as tk
from tkinter import messagebox

class SayilarApp:
    def __init__(self, root):
        self.sayi_adedi = 11 # Toplam girilecek sayı adedi
        self.root = root
        self.root.title("{} Sayının Toplamı ve Ortalaması Hesabı".format(self.sayi_adedi))  # Uygulama penceresinin başlığı

        self.sayilar = []  # Sayı giriş alanlarını saklamak için liste

        for i in range(self.sayi_adedi):  # Kullanıcıdan sayı almak için döngü
            label = tk.Label(root, text=f"{i+1}. Sayıyı Girin:")  # Her sayı için etiket oluştur
            label.grid(row=i, column=0, padx=10, pady=10)  # Etiketi yerleştir

            entry = tk.Entry(root)  # Sayı girişi için giriş alanı oluştur
            entry.grid(row=i, column=1, padx=10, pady=5)  # Giriş alanını yerleştir
            entry.insert(0, str(i + 1))  # Otomatik olarak i + 1 değerini ekle
            self.sayilar.append(entry)  # Giriş alanını listeye ekle

        # Hesapla butonunu oluştur ve tıklama olayını bağla
        self.hesapla_button = tk.Button(root, text="Hesapla", command=self.TopOrtHesapla)
        self.hesapla_button.grid(row=self.sayi_adedi, column=0, columnspan=2, padx=10, pady=10)

        # Sonuçlar için etiketler oluştur
        self.Toplam_label = tk.Label(root, text="")  # Toplam sonucunu gösterecek etiket
        self.Toplam_label.grid(row=self.sayi_adedi + 1, column=0, columnspan=2, padx=10, pady=5)

        self.Ortalama_label = tk.Label(root, text="")  # Ortalama sonucunu gösterecek etiket
        self.Ortalama_label.grid(row=self.sayi_adedi + 2, column=0, columnspan=2, padx=10, pady=5)

    def TopOrtHesapla(self):
        try:
            # Kullanıcıdan alınan giriş alanlarından değerleri al ve tam sayıya çevirerek yeni bir liste oluştur
            sayilar_degerleri = [int(entry.get()) for entry in self.sayilar]
            Toplam = sum(sayilar_degerleri)  # Sayıların toplamını hesapla
            Ortalama = Toplam / len(sayilar_degerleri)  # Ortalama hesapla

            # Sonuçları etiketlerde göster
            self.Toplam_label.config(text=f"Toplam: {Toplam}")
            self.Ortalama_label.config(text=f"Ortalama: {Ortalama:.2f}")

        except ValueError:  # Eğer dönüşüm sırasında hata olursa
            messagebox.showerror("Hatalı Giriş", "Lütfen geçerli bir değer girin.")  # Hata mesajı göster

# Tkinter arayüzünü başlatma
if __name__ == "__main__":
    root = tk.Tk()  # Tkinter uygulamasını başlat
    app = SayilarApp(root)  # Uygulama sınıfını başlat
    root.mainloop()  # Uygulamanın ana döngüsünü başlat

import tkinter as tk
# hesapla
def hesaplama():
    try:
        kilo_hesap = float(kilo_entry.get())
        boy_hesap = float(boy_entry.get()) / 100  # Boyu metreye çeviriyoruz
        obe = kilo_hesap / (boy_hesap ** 2)
        sonuc_label.config(text=f"OBE: {obe:.2f}")

        #aralık
        if obe <= 18.5:
            aralık_label.config(text ="Zayıfsınız bir vücuda sahipsiniz, sağlığınız için kilo almanızı öneririm.",
                                     fg ="blue")


        elif  18.5 < obe <= 24.5:
            aralık_label.config(text ="Normal bir vücuda sahipsiniz.",
                                     fg ="green")

        elif 24.5 < obe <= 29.9:
            aralık_label.config(text ="kilolu bir vücudunuz var, sağlığınız için biraz kilo vermenizi öneririz.",
                                     fg ="yellow", bg ="black")

        elif obe > 30:
            aralık_label.config(text ="obezsiniz ve sağlığınız için bir an önce kilo vermelisiniz!",
                                     fg ="red")

    except ValueError:
        eror = tk.Label(text ="Lütfen geçerli bir boy ve kilo girin!", fg ="red",
                        font="Times 12 bold")
        eror.pack()

# pencere
pencere = tk.Tk()
pencere.title("Vücut Kütle Endeksi")
pencere.geometry("300x300")

# boy
boy_label = tk.Label(pencere, text="Boy (cm)", fg="green", font="Times 18 bold")
boy_label.pack(pady=10)
boy_entry = tk.Entry(pencere)
boy_entry.pack(pady=5)

# kilo
kilo_label = tk.Label(pencere, text="Kilo (kg)", fg="green", font="Times 18 bold")
kilo_label.pack(pady=10)
kilo_entry = tk.Entry(pencere)
kilo_entry.pack(pady=5)

# Hesapla Butonu
hesapla_butonu = tk.Button(pencere, text="Hesapla", command=hesaplama)
hesapla_butonu.pack(pady=15)

# Sonuç Etiketi
sonuc_label = tk.Label(pencere, text ="", font="Times 12")
sonuc_label.pack(pady=5)

#aralık etiketi
aralık_label = tk.Label(pencere, text ="", font="Helvetice 13", wraplength=300, justify="left")
aralık_label.pack()


pencere.mainloop()

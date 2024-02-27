import re
import tkinter as tk
from tkinter import messagebox

def calculate():
    tümce = entry.get()
    if not tümce :
        messagebox.showerror(title="HATA!", message="Lütfen bir sözcük ya da tümce giriniz!", icon="warning")
        return

    karakterSayisi = len(tümce)
    kSayisi = len(re.findall(r'\S', tümce))
    liste = re.findall(r'\w+', tümce)
    sozcukSayisi = len(liste)
    ortalamaKarakter = round(karakterSayisi/sozcukSayisi, 2)

    result = f"Girdi: {tümce}\n" \
            f"Liste: {liste}\n" \
            f"Boşluk dahil Karakter Sayısı: {karakterSayisi}\n" \
              f"Boşluksuz Karakter Sayısı: {kSayisi}\n" \
              f"Sözcük Sayısı: {sozcukSayisi}\n" \
              f"Sözcük Başına Ortalama Karakter Sayısı: {ortalamaKarakter}" 
            

    messagebox.showinfo("Sonuç", result,)




app = tk.Tk()
app.title("Sözcük ve Karakter Uygulaması")
app.geometry("500x250")

label = tk.Label(app, text="Sözcük veya Tümce Giriniz:")
label.pack()

entry = tk.Entry(app, width=50)
entry.insert(0, "Metin giriniz!")
entry.configure(fg="black")
entry.bind("<FocusIn>", lambda args: entry.delete(0,"end"))
entry.pack()

button = tk.Button(app, text="Bul", command=calculate)
button.pack(pady=10)

app.mainloop()
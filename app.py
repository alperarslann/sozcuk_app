import re
import tkinter as tk
from tkinter import messagebox

def surerlik(sozcuk): # Türkçedeki sürerlik görünüşü var mı yok mu
    cikti = "Sürerlik görünüşü yok." # False döndürüyor.
    #cikti = "Sürerlik görünüşü yok."
    arama = re.search("..yor*", sozcuk)
    if arama:
        cikti = "Sürerlik görünüşü var." # True döndürüyor. 
        #cikti = "Sürerlik görünüşü var." 
    return (cikti)

def surerlilikSayac(tümceDizisi):
    sozcukListesi = tümceDizisi.split()
    #print("Sözcük List:",sozcukListesi) #kontrol amaçlı
    surerlikEkleri = []
    for sozcuk in sozcukListesi:
        sozcukDegis = sozcuk.replace(".", "")
        if surerlik(sozcukDegis) == "Sürerlik görünüşü var.":
            if surerlik(sozcukDegis):
                surerlikEkleri.append(sozcukDegis.replace("yor", "YOR"))
    return surerlikEkleri


def calculate():
    tümce = entry.get()
    if not tümce:
        messagebox.showerror(title="HATA!", message="Lütfen bir sözcük ya da tümce giriniz!", icon="warning")
        return
    
    elif tümce.isdigit():
        messagebox.showerror(title="HATA!", message="Lütfen bir sözcük ya da tümce giriniz!", icon="warning")
        return  

    elif tümce == "Metin giriniz!":
        messagebox.showerror(title="HATA!", message="Lütfen bir sözcük ya da tümce giriniz!", icon="warning")
        return  

    karakterSayisi = len(tümce)
    kSayisi = len(re.findall(r'\S', tümce))
    liste = re.findall(r'\w+', tümce)
    surerlilikBul = surerlik(tümce)
    surerlilikSay = surerlilikSayac(tümce)
    sozcukSayisi = len(liste)
    ortalamaKarakter = round(karakterSayisi/sozcukSayisi, 2)

    if not surerlilikSay:
        surerlilikSay = ("Sürerlik görünüşüyle çekimlenmiş eylem bulunamadı.").upper()
        
    result = f"Girdi: {tümce}\n" \
        f"Liste: {liste}\n" \
        f"Sürerlik Görünüşüyle Çekimlenmiş Eylem Var mı?: {surerlilikBul}\n" \
        f"Sürerlik Görünüşüyle Çekimlenmiş Eylem(ler): {surerlilikSay}\n" \
        f"Boşluk dahil Karakter Sayısı: {karakterSayisi}\n" \
        f"Boşluksuz Karakter Sayısı: {kSayisi}\n" \
        f"Sözcük Sayısı: {sozcukSayisi}\n" \
        f"Sözcük Başına Ortalama Karakter Sayısı: {ortalamaKarakter}"

    result_label = tk.Label(app, text=result, width=100, wraplength=500, justify="left", bg="lightgrey", font=("Arial", 10), relief="groove", padx=10, pady=10, anchor="w", borderwidth=2, highlightthickness=2, highlightbackground="black",)
    result_label.pack()

    


result_label = None  # Result_Label'ı global yapmak için                

# önceki sonuçları temizleme fonksiyonu
def clearAll():
    for widget in app.winfo_children():
        if isinstance(widget, tk.Label) and widget != result_label:
            widget.destroy()
        elif isinstance(widget, tk.Entry):
            widget.delete(0, "end")
            widget.insert(0, "Metin giriniz!")
            widget.configure(fg="black")



app = tk.Tk()
app.title("Sözcük ve Karakter Uygulaması")
app.geometry("1000x500")

label = tk.Label(app, text="Sözcük veya Tümce Giriniz:")
label.pack()

entry = tk.Entry(app, width=50, borderwidth=2, highlightthickness=2, justify="center", font=("Arial", 10))
entry.insert(0, "Metin giriniz!")
entry.configure(fg="black")


entry.bind("<FocusIn>", lambda args: entry.delete(0,"end"))
entry.pack()

button = tk.Button(app, text="Bul", bg="lightgrey", fg="black", command=calculate)
button.pack(pady=10)
app.bind('<Return>', lambda event: calculate()) # Enter tuşuna basıldığında da çalıştır


silButton = tk.Button(app, text="Sonuçları Temizle", command=clearAll, bg="crimson")
silButton.pack(pady=10)




app.mainloop()
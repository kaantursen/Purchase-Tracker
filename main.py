import datetime
import dotenv
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("DB_NAME")
client = MongoClient(mongo_uri)
db = client["butceDB"]

print(f"Database successfully connected: {db.name}")
koleksiyon = db["harcamalar"]
while True:
    print("\n1. Yeni Harcama Ekle")
    print("2. Tüm Harcamaları Listele ve Toplamı Gör")
    print("3. Çıkış")
    
    secim = input("\nYapmak istediğiniz işlemi seçin (1/2/3): ")

    if secim == "1":
        try:
            tt = input("Harcama başlığını giriniz: ")
            pr = float(input("Harcama tutarını giriniz: "))
            cat = input("Harcama kategorisini giriniz: ")

            butceDB = {
            "kategori": cat,
            "baslik": tt,
            "fiyat": pr,
            "olusturulma_tarihi": datetime.now()}
            sonuc = koleksiyon.insert_one(butceDB)
            print(f"Kayıt başarıyla eklendi! ID: {sonuc.inserted_id}")
        except ValueError:
            print("!!! Hata: Tutar kısmına sadece sayı girmelisiniz.")
    elif secim == "2":
        tum_harcamalar = koleksiyon.find()
        for harcama in tum_harcamalar:
            print(f"Başlık: {harcama['baslik']} | Tutar: {harcama['fiyat']} TL | Kategori: {harcama['kategori']} | Tarih: {harcama['olusturulma_tarihi']}")
        toplam_tutar = 0
        print("\n--- HARCAMA RAPORU ---")
        for harcama in tum_harcamalar:
            tutar = harcama["fiyat"]
            toplam_tutar += tutar
            print(f"• {harcama['baslik']}: {tutar} TL")
            print("-" * 20)
            print(f"TOPLAM HARCAMANIZ: {toplam_tutar} TL")
            print("-" * 20)
    elif secim == "3":
        print("Programdan çıkılıyor... İyi günler!")
        break
    else:
        print("Geçersiz seçim! Lütfen 1, 2 veya 3 giriniz.")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Demleyici 3000
Dünyanın en bilimsel, en ciddi, en abartılı çay demleme sistemi.
Bu kod gerçekten çay demler. Sadece dijital olarak.
"""

import time
import random
import sys

def demle_cay(tur, seker=False):
    print(f"\n🍵 {tur.upper()} ÇAYI DEMLEMİ BAŞLIYOR...")
    print("Bilimsel hesaplamalar yapılıyor...")
    time.sleep(1.5)
    
    # Gizli not: Bürokrasi de çay gibi demlenir, acele etme.
    sicaklik = random.randint(85, 98)
    sure = random.randint(3, 7)
    
    print(f"İdeal sıcaklık tespit edildi: {sicaklik}°C")
    print(f"Demleme süresi: {sure} dakika (evrenin dengesine göre)")
    
    for i in range(sure):
        print(f"Demleniyor... {i+1}/{sure} dakika geçti. Çay yaprakları düşünüyor.")
        time.sleep(1)  # Gerçek hayatta 60 saniye olsun diye, ama sabırsızlar için 1 sn
    
    print("\n✨ ÇAY HAZIR!")
    if seker:
        print("Şeker eklendi. Dişler üzüldü ama kalp mutlu.")
    else:
        print("Şekersiz. Sağlıklı ve çok ciddi.")
    
    kalite = random.choice(["Mükemmel", "İyi", "Orta", "Büyükannem daha iyisini yapar", "NASA onaylı"])
    print(f"Kalite puanı: {kalite}")
    print("Afiyet olsun. Bir sonraki demleme için evreni beklemeye alıyoruz.")

if __name__ == "__main__":
    print("=== ABARTILI ÇAY DEMLEYİCİ 3000 v1.0 ===")
    print("Bu program çay demler. Gerçekten.")
    tur = input("Hangi çay? (siyah/yeşil/ıhlamur/kaçak): ").strip() or "siyah"
    seker_input = input("Şeker ister misin? (e/h): ").strip().lower()
    seker = seker_input in ["e", "evet", "yes", "1"]
    demle_cay(tur, seker)
    print("\nProgram sona erdi. Çay bitti, hayat devam ediyor.")

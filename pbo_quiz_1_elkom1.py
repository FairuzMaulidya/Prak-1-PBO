# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:25:11 2024

@author: Fairuz Maulidya
"""

class KalkulatorPenjumlahan: #mendefinisikan sebua class
    def __init__(self): #initializer / konstruktor
        self.hasil = 0  # Inisialisasi nilai awal untuk hasil

    def penjumlahan(self): #method penjumlahan
        self.hasil = self.angka1 + self.angka2 #menghitung

    def input_angka(self): #method untuk menginput angka
        print("======Kalkulator Penjumlahan====")
        self.angka1 = float(input("Masukkan angka pertama: ")) #menginput sebuah nilai
        self.angka2 = float(input("Masukkan angka kedua: "))

# Membuat objek dari class KalkulatorPenjumlahan
kalkulator = KalkulatorPenjumlahan()

# Memanggil method untuk menerima input
kalkulator.input_angka()

# Memanggil method untuk melakukan penjumlahan
kalkulator.penjumlahan()

# Mencetak hasil
print("Hasil penjumlahan:", kalkulator.hasil)


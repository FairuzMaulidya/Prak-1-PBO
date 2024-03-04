# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:03:55 2024

@author: Fairuz Maulidya
"""

class GradeMahasiswa: #mendefinisikan sebuah class
    def __init__(self): #initializer / konstruktor
        self.nama = ""
        self.nim = ""
        self.nilai = 0.0
        self.grade = ""

    def input_data(self): #method untuk menginput data
        self.nama = input("Nama: ")
        self.nim = input("NIM: ")
        self.nilai = float(input("Masukkan nilai: "))

    def hitung_grade(self): #method untuk menentukan grade
       if 80 <= self.nilai <= 100:
           self.grade = "A"
       elif 77 <= self.nilai <= 79.99:
           self.grade = "A-"
       elif 74 <= self.nilai <= 76.99:
           self.grade = "B+"
       elif 68 <= self.nilai <= 73.99:
           self.grade = "B"
       elif 65 <= self.nilai <= 67.99:
           self.grade = "B-"
       elif 62 <= self.nilai <= 64.99:
           self.grade = "C+"
       elif 56 <= self.nilai <= 61.99:
           self.grade = "C"
       elif 45 <= self.nilai <= 55.99:
           self.grade = "D"
       else:
           self.grade = "E"

    def tampilkan_info(self): #menampilkan hasil
        print("--- DATA PRAKTIKAN PBO 2024 ---")
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Grade:", self.grade)


# Membuat objek dari class GradeMahasiswa
mahasiswa = GradeMahasiswa()

# Memanggil method untuk input data
mahasiswa.input_data()

# Memanggil method untuk menghitung grade
mahasiswa.hitung_grade()

# Memanggil method untuk menampilkan informasi
mahasiswa.tampilkan_info()

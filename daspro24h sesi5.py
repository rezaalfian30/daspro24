#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name = input("isikan nama anda:")

print("selamat datang",name)
print("ini adalah urutan angka:")
print("1",end='')
print("2",end='')
print("3")
print("A","B","C",sep='-')


# # string format

# In[ ]:


val1 = int(input("isikan bilangan 1:"))
val2 = int(input("isikan bilangan 2"))

print("Hasil Penjumlahan",val1,"+",val2,"=",val1+val2)
print("Hasil Penjumlahan {} {} = {}".format(val1,val2,val1+val2))


# # format index

# In[ ]:


fname = input("isikan nama awal:")
mname = input("isikan nama tengah:")
iname = input("isikan nama akhir:")
print("nama lengkap: {} {} {}".format(fname,mname,iname))
print("nama lengkap: {1} {0} {2}".format(fname,mname,iname))
#menggunakan key variabel
print("nama lengkap: {f} {m} {i}".format(f=fname,i=iname,m=mname))


# <h1>slicing</h1> <br>
# 
# Mengambil karakter pada string berdasarkan index

# In[ ]:


kalimat = input("isikan kalimat:")
#mencetak karakter ke 2
print("karakter kedua adalah:",kalimat[1])
#mencetak karakter ke 3 sampai seterusnya
print("karalter ke 3 dst:",kalimat[2])
#mencetak karakter ke 2 sampai ke 4
print("karakter ke 2-4:",kalimat[1:4])
#mencetak paling akhir
print("karakter terakhir adalah:",kalimat[-1])
#reverse
print("kalimat di balik menjadi:",kalimat[::-1])


# <h1>fungsi string</h1> 

# In[ ]:


namaLengkap = "Rasyah Bengal S.TkPaud"
nama = namaLengkap.split(' ')
print("Nama awal:",nama[0])
print("Nama akhir:",nama[1])
print("Gelar:",nama[2])

#fungsi find
#jika ketemu mengembalikan indeks dari posisi karakter yang di cari
#jika tidak akan menghasilkan-1
nomorPlat = "F1234GR"
cari = nomorPlat.find("G")
print(cari)

#buatlah program untuk memvalidasi apakah email valid atau tidak
#valid -> mempunyai tanda @ sama . -> adi@gmail
#adi.nu@gmail.com => tidak valid
#posisi @ disebelah kiri dari posisi .

email = input("isikan email anda:")
findAt = email.find("@")
findPeriod = email.find(".")

validation = "A Valid email" if findAt != -1 and findPeriod != -1 and findAt < findPeriod else "Not A Valid email"
print(validation)


# In[ ]:


#fungsi string random bilangan
from random import random #float
nilai = random ()
#fstring
print (f"nilai acak pecahan :{nilai}")

from random import randint
intNilai = randint(0,100)
print(f"nilai acak antar 0-100 :{intNilai}")

from random import choice
month = ("Jan","Feb","mar","apr","May","jun","Jul","Aug","Sep","Okt","Nov","Des")
cmonth = choice (month)
print(f"Sekarang Bulan : {cmonth}")

nilai1 = radint(0,100)
nilai2 = radint(0,100)
print(f"berapakah hasil :{nilai1}+{nilai2}?")
answer = input ("isikan jawabn anda :")
chek = "anda benar!!" if nilai1 + nilai2 == answer else "anda salah!"
print(chek)


# In[ ]:





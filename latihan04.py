#Program untuk menghitung Waktu Tempuh

jarak1=125
kecepatan1=62
jarak2=256
kecepatan2=70

waktu1=jarak1/kecepatan1
waktu2=jarak2/kecepatan2
#waktu istirahat 45 menit=0.75 jam
waktuIstirahat=0.75

#hasil waktuTotal adalah 6.4327 jam dalam keadaan float
waktuTotal=waktu1+waktu2+waktuIstirahat

#kemudian dikonversi menjadi menit dengan dikali 60, hasilnya 385.3963 menit
totalMenit=waktuTotal*60

#totalMenit kemudian di//60 untuk menghasilkan jam yaitu 6 jam
totalSemua= int(totalMenit//60)

#totalMenit kemudian di % 60 untuk menghasilkan menit yaitu 25 menit
totalSemua1=int(totalMenit%60)

#untuk menghitung total waktu berkendara = menggabungkan 6 jam 25 menit dalam string hingga menjadi 6.25
totalFix=str(totalSemua)+ str('.')+str(totalSemua1)

#untuk menghitung waktu sampai yaitu dengan mengubah 6.25 yang tadinya string menjadi float , kemudian di tambah jam berangkat
waktuSampai= 6+float(totalFix)

print(waktuSampai)

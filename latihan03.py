#Program Untuk Menghitung berapa kali pengisian bahan bakar di sebuah perjalanan 
import math

jarakTotal=795
print('Jarak yang akan ditempuh Pak Budi adalah sejauh 795 km'+ '\n')

jarakPerLiter=12
print('Untuk 1liter mobil, mobil pak Budi bisa menempuh jarak 12 km'+'\n')

kapasitasTanki=50
print('kapasitas tanki mobil Pak Budi adalah 50 liter'+'\n')

bensinYangDiperlukan=jarakTotal/jarakPerLiter - kapasitasTanki
pengisianTanki=bensinYangDiperlukan/kapasitasTanki

minimalPengisian= math.ceil(pengisianTanki)

print('Pak Budi harus mengisi mobilnya minimal sebanyak'+str(minimalPengisian)+'kali') 

phi=22/7
jari=int(input())
tinggi=int(input())
volume=phi*jari*jari*tinggi
Luas=2*phi*jari*(tinggi+jari)
Kel=2*phi*jari
print("Volume= %.2f"%volume)
print("Luas= %.2f"%Luas)
print("Keliling= %.2f\n"%Kel)

jari2,tinggi2=input().split()
jari2=int(jari2)
tinggi2=int(tinggi2)
volume2=phi*jari2*jari2*tinggi2
Luas2=2*phi*jari2*(tinggi2+jari2)
Kel2=2*phi*jari2
print("Volume= %.2f"%volume2)
print("Luas= %.2f"%Luas2)
print("Keliling= %.2f"%Kel2)
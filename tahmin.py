#Kodlayan: İlkcan Doğan
#Tarih: 22.09.2019

from random import randint
sayi = randint(1,100)

while True:
	try:
		tahmin = int(input("Lütfen 1 İle 100 Arasında Bir Sayı Giriniz: "))
		if sayi == tahmin:
			print("Doğru Tahmin Ettiniz. Tebrikler... :-)")
			break
		elif sayi < tahmin:
			print("Sayı tahmin ettiğinizden daha küçük!")
		elif sayi > tahmin:
			print("Sayı tahmin ettiğinizden daha büyük")

	except:
		print("Lütfen Sadece Sayı Giriniz!!!")

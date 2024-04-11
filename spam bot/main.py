import pyautogui
import time
import sys
import webbrowser

sayi = int(input("Kaç mesaj göndermek istiyorsunuz (max 3000): "))
text = input("Hedef kullanıcıya ne yazmak istersiniz: ")

if sayi > 3000:
    print("Maksimum 3000 mesaj gönderebilirsiniz.")
    sys.exit()
else:
    pass

izin = input("Hedef kullanıcıya " + str(sayi) + " kadar mesaj gönderecektir. Devam etmek istiyor musunuz? (E/H): ")

if izin.upper() == 'E':
    pass
else:
    print("Program sonlandırıldı.")
    sys.exit()

print("5 dakika içinde WhatsApp Web'e giriş yapın ve hedef kişinin sohbet ekranına girin. Ardından mesaj atma butonunun üzerine fareyi getirin; yoksa bilgisayar rastgele bir yere tıklar.")

time.sleep(30)  # Ortalama en yavaş 30 saniyede okunur olucağı için yeterli
webbrowser.open("https://web.whatsapp.com/")
time.sleep(30)

# Mesaj gönderme döngüsü
for i in range(sayi):
    pyautogui.write(text)
    time.sleep(0.1)
    pyautogui.click()
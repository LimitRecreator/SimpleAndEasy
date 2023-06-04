import os
os.system("sudo apt update && sudo apt upgrade")
install = input("Já possuí o Kali-Anonsurf instalado?(y/n): ")
if install == ("n"):
    os.system("git clone https://github.com/Und3rf10w/kali-anonsurf")
    os.system("cd kali-anonsurf")
    os.system("sudo bash installer.sh")
if install == ("N"):
    os.system("git clone https://github.com/Und3rf10w/kali-anonsurf")
    os.system("cd kali-anonsurf")
    os.system("sudo bash installer.sh")
start = input("Gostaria de iniciar o kali anonsurf?(y/n): ")
if start == ("y"):
    os.system("sudo anonsurf start")
elif start == ("Y"):
    os.system("sudo anonsurf start")
if start == ("n"):
    print ("Certo, quando quiser iniciar o anonsurf, basta me rodar de novo!")
elif start == ("N"):
    print("Certo, quando quiser iniciar o anonsurf, basta me rodar de novo!")
os.system("anonsurf status")
print("Para desligar seu anonsurf dê o comando 'sudo anonsurf stop'")
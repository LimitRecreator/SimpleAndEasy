import socket
import os
os.system('pip install socket')
import keyboard

tip = input("Já sabe o IP alvo?(s/n)")
if tip == ("n"):
		turl = input("Digite aqui apenas o url principal do alvo. Ex: 'www.google.com/ | Ou 'www.suapesquisa.gov' Muito importante colocar SEM nada qeu vem depois da primeira barra invertida e não colocar também 'https' ou 'http' somente o url principal.-> ")
		print("ASSIM QUE O IP ALVO FOR EXIBIDO ENTRE PARÊNTESES, PRESSIONE 'CTRL+C' !!!")
		
		
		target_ip = os.system(f"ping {turl}")
		
		
		print("COPIE O ENDEREÇO DE IP QUE FOI EXIBIDO ENTRE PARÊNTESES")
if tip == ("N"):
		turl = input("Digite aqui apenas o url principal do alvo. Ex: 'www.google.com/ | Ou 'www.suapesquisa.gov' Muito importante colocar SEM nada qeu vem depois da primeira barra invertida e não colocar também 'https' ou 'http' somente o url principal.-> ")
		print("ASSIM QUE O IP ALVO FOR EXIBIDO ENTRE PARÊNTESES, PRESSIONE 'CTRL+C' !!!")
		target_ip = os.system(f"ping {turl}")
		print("COPIE O ENDEREÇO IP QUE FOI EXIBIDO ENTRE PARÊNTESES")
if tip == ("s"):
	pass
if tip == ("S"):
	pass

print("AGORA IREI EXECUTAR E/OU INSTALAR UMA PROTEÇÃO NO SEU ENDEREÇO DE IP")


install = input("Já possuí o Kali-Anonsurf instalado?(y/n): ")
if install == ("n"):
    os.system("git clone https://github.com/Und3rf10w/kali-anonsurf")
    os.system("cd kali-anonsurf && sudo bash installer.sh")
    os.system("sudo bash installer.sh")
if install == ("N"):
    os.system("git clone https://github.com/Und3rf10w/kali-anonsurf")
    os.system("cd kali-anonsurf && sudo bash installer.sh")
    os.system("sudo bash installer.sh")

os.system("sudo anonsurf start")

def scan_ports(target_host, target_ports):
    open_ports = []
    for port in target_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    target_host = input("Cole o endereço IP do alvo: ")
    target_ports = range(1, 1025)  # Varredura de portas de 1 a 1024

    open_ports = scan_ports(target_host, target_ports)

    if open_ports:
        print("Portas abertas encontradas:")
        for port in open_ports:
            print(f"Porta {port} aberta")
    else:
        print("Nenhuma porta aberta encontrada no alvo.")

if __name__ == "__main__":
    main()

print("Para desligar seu anonsurf dê o comando 'sudo anonsurf stop'")

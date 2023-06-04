import os
import subprocess
url = input(str("Digite ou cole o URL alvo: "))
os.system(f"sqlmap {url} --dbs random-agent --level 4 --risk 2 --tamper=space2comment --time-sec=2 --flush-session")
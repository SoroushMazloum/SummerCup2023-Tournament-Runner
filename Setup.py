from os import system as Command

Command("chmod +x *.sh")
Command("cd HoleAnalyzer/data && chmod +x *.sh")
Command("cd HoleAnalyzer && pip install -r requirements.txt")

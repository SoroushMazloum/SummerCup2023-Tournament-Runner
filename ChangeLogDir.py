from os import system as Command

Command("cp *.rcg.tar.gz Logs -v")
Command("cp *.rcl.tar.gz Logs -v")
Command("mv *.rcg.tar.gz ../SummerCup2023/Logs/ -v")
Command("mv *.rcl.tar.gz ../SummerCup2023/Logs/ -v")

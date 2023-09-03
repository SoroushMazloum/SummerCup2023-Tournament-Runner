import os

files = os.listdir()

for file in files:
    if file.endswith(".rcg"):
        Result = file.lstrip('0123456789')
        Result = Result.lstrip('-')
        Result = Result.replace('_', ' ', 10)
        Result = Result.replace('-vs-', '  vs  ', 1)
        
        # Remove the .rcg extension from the end of the file name
        Result = Result[:-4]
        
        # Rename the file
        os.system("rm Result.txt")
        os.system("touch Result.txt")
        file = open('Result.txt', 'w')
        file.write(Result)
        file.close()
        exit()
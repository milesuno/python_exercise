import utilis
from utilis import find_largest_num
from pathlib import  Path
num1 = [2, 6, 29, 49, 4, 28, 21, 10]

num2 = [80, 32, 19, 59, 26]

num3 = [6, 16, 66, 34, 28, 30]

num4 = [-69]

print(find_largest_num(num1))

print(utilis.find_largest_num(num2))

print(find_largest_num(num3))

print(utilis.find_largest_num(num4))

pathExist = Path("venv")
print(pathExist.exists())

pathMakeDir = Path("BBC")
# pathMakeDir.mkdir()
# pathMakeDir.rmdir()

pathInterateFiles = Path()

for file in pathInterateFiles.glob("*.*"):
    print(file)
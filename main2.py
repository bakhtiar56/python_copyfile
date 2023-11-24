from shutil import copyfile
import os

copyfile("source2.txt","dest2.txt")

os.system("cat dest2.txt")




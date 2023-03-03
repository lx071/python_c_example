# 命令行执行 python test.py
import os
import sys

os.system('rm -r build src/__pycache__')

os.system('mkdir build')
os.chdir('./build')
sys.path.append(os.path.abspath('..') + '/src')
# print("aaa:", sys.path)
#
os.system("cmake ..")
os.system("make")
# print("bbb:", sys.path)
# print(sys.argv[0])
# print(os.getcwd())
# print(os.path.abspath('..'))


os.system('./example')

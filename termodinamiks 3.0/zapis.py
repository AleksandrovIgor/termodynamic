# -*- coding: cp1251 -*-
import shutil
import os

def _print(argStr):
    """function out - print files"""
    print unicode(argStr, 'cp1251'),

shutil.copyfile("latex.tex", "doct1.tex")
# ���������� ������ ����� ������ )
myfile = open("doct1.tex", "r+")
data = myfile.read()

data +=" \\begin{tabular}"
 
data +=" ���� & zilonis & ������� & nilzirgs \\\ \n"
 
data +=" ������� & nilzirgs\\ \n\\"
data +=" ��� & lauva\\ \n\\"
 
data +="\end{tabular} \n\\"


data += "\end{document}\n"
myfile.seek(0, 0)
myfile.write(data)

#myfile.truncate(myfile.tell())
myfile.close()
[_print(line) for line in open("doct1.tex")]
#os.remove("doct1.tex")

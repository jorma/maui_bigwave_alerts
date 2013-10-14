import sys
import codecs

def encode():
  path = "C:\Users\user\Desktop"
  basename = "assgn2part1.txt"
  filename = path + "\\" + basename
  #file = open(filename, "rt")
  f = codecs.open(filename,encoding='utf-8')
  contents = f.read()


  print contents ,"\n"
  newcontents = contents.replace('a','e')
  newcontents = contents.replace('s', '3')

  print newcontents


  f.close()
# import filecmp
  
# f1 = "t2.txt"
# f2 = "t1.txt"
  
# # shallow comparison
# result = filecmp.cmp(f1, f2)
# print(result)
# with open('t1.txt', 'r') as fin, open('t2.txt', 'w') as fout:
#     while True:
#         line = fin.readline()
#         if not line:
#             break
#         fout.write(line)

import sys



 
a = '''def main(x): 
            print(x)'''


    # print(lines)
    # lines = lines[0]
    # print(lines)
with open('t1.txt') as f:
    lines = f.read()
    a = a+lines
# print(a)
exec(a)

     
 


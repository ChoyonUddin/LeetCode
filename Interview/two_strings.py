'''Given two arrays of strings, determine whether corresponding elements contain a common substring
 Ex:
 a = ['ab','cd','ef']
 b = ['af','ee','ef']
----------------------
yes 
no 
yes
'''
def commonsubstring(a,b):
    for i,j in zip(a,b):
        print("yes" if len(set(i).intersection(set(j)))>0 else "No")
print(commonsubstring(['ab','cd','ef'],['af','ee','ef']))
# coding: utf-8

# In[1]:


from os import walk
from os.path import join
import os

# 指定要列出所有檔案的目錄
mypath = "./"

# 遞迴列出所有檔案的絕對路徑
for root, dirs, files in walk(mypath):
    for f in files:
        fullpath = join(root, f)
        if fullpath.split('.')[-1] == 'py':
            os.system('2to3 -w %s'%fullpath)
            print(fullpath)


# In[ ]:
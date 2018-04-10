
# coding: utf-8

# In[1]:


from os import walk
from os.path import join

# 指定要列出所有檔案的目錄
mypath = "./"

# 遞迴列出所有檔案的絕對路徑
for root, dirs, files in walk(mypath):
    for f in files:
        fullpath = join(root, f)
        if fullpath.split('.')[-1] == 'py':
            get_ipython().system('2to3 -w $fullpath')
            print(fullpath)


# In[ ]:





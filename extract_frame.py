# coding: utf-8

# In[1]:


from os import walk
from os.path import join
import os
import sys, getopt


def main(argv):
    input_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <input file> -o <out file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':   # for help
            print('test.py -i <input file> -o <out file>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
            
    
    # 指定要列出所有檔案的目錄
    mypath = "./" + input_file
    video_format = ['avi', 'mp4', 'flv', 'mkv']
    # 遞迴列出所有檔案的絕對路徑
    for root, dirs, files in walk(mypath):
        for f in files:
            fullpath = join(root, f)
            if fullpath.split('.')[-1] in video_format:
                #os.system('2to3 -w %s'%fullpath)
                # -r img/s 
                msg = "ffmpeg -i {0}/{1} -an -r 2 -y {2}/{3}-%d.jpg".format(input_file, f, output_file, ''.join(f.split('.')[:-1]))
                print(msg)
                os.system(msg)

                
            
if __name__ == "__main__":
    main(sys.argv[1:])
            


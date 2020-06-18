import os
 
def search_file(search_dir,search_name):
    '''搜索特定文件'''
    search_files=[] #存储搜索到的文件
    for root,dirs,files in os.walk(search_dir):
        for file in files:
            path=os.path.join(root,file) #文件完整路径
            path=os.path.normcase(path) #标准化路径
            if file == search_name:
                search_files.append(path) #插入search_files列表中
    return search_files
 
if __name__=='__main__':
    search_name=input('搜索的文件名为：')     
    search_dir=('C:\\','D:\\','F:\\')
    for i in range(len(search_dir)):
        for item in search_file(search_dir[i],search_name):            
            print(item)
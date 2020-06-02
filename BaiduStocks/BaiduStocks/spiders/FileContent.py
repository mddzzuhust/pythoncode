import os

if __name__ == '__main__':
    path = "C:\\Users\\Administrator\\Desktop\\32个Java面试必考点"
    files = os.listdir(path)
    i=1
    for file in files:
        try:
            old_file_path = os.path.join(path, file)
            new_file_path = os.path.join(path,str(i)+'.png')
            i=i+1
            print(old_file_path)
            print(new_file_path)
            os.rename(old_file_path, new_file_path)
        except:
            continue
import os 
from __init__ import PROJECT_ROOT
import re
number_regex=re.compile('\d+')
def cut_last_n_file(column_num,file_path,target_file):
    """
    切割文件的后n列之后的数据
    """
    i=0 
    with open(file_path,'r',encoding='utf-8',errors='ignore') as in_file,open(target_file,'w',encoding='utf-8')as tf:
        line_data=in_file.readline()
        while line_data!='':
            cut_line=line_data[column_num:]
            #print(cut_line)
            line_data=in_file.readline()
            # if '/' in cut_line:
            #     print(cut_line)
            #     continue
            if number_regex.findall(cut_line):
                tf.write(cut_line)
                i+=1
            if i>5000:
                break


if __name__=='__main__':
    cut_last_n_file(31,
                    os.path.join(PROJECT_ROOT,'resource','tokendata','applogcat-1.log'),
                    os.path.join(PROJECT_ROOT,'resource','tokendata','applogcat-1-cut.log')
                    )
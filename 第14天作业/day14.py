import pandas as pd
import threading,multiprocessing,time,os
import xml.etree.ElementTree as ET

dic = {}
def recoder(dic):
    def timer(func):
        def wrapper(*args, **kwargs):
            st = time.time()
            func(*args, **kwargs)
            et = time.time()
            print(f"pid为{os.getpid()} 线程id为{threading.get_ident()}的函数读取文件{args[0]}，运行时长{round(et-st,5)}")
            return result
        return wrapper
    return timer

@recoder(dic)
def count_word(path):
    tree = ET.parse(path)
    root = tree.getroot()
    for e in root.iter():
        if e.text:
            for word in e.text.split():
                dic[word] = dic.get(word,0)+1

def read_files(path):
    thread_list = []
    global dic
    for file in os.listdir(path):
        newfile = path + '/' + file
        new_thread = threading.Thread(target=count_word, args=(newfile,))
        thread_list.append(new_thread)
        new_thread.start()
    for thread in thread_list:
        thread.join()
    return dic

def main(path):
    global dic
    pool = multiprocessing.Pool()
    result_list = []
    second_dir = []
    for file in os.listdir(path):
        newfile = path+'/'+file
        if os.path.isdir(newfile):
            second_dir.append(newfile)
        else:
            new_thread = threading.Thread(target=count_word,args=(newfile,))
            new_thread.start()

    for dir in second_dir:
        for file in os.listdir(dir):
            newfile = dir + '/' + file
            result_list.append(pool.apply_async(read_files, args=(newfile,)))
    pool.close()
    pool.join()
    for res in result_list:
        dic.update(res.get())
    return dic

if __name__ == '__main__':
    dic.clear()
    main('../../download')
    series =pd.Series(dic)
    series.to_csv('result.csv')
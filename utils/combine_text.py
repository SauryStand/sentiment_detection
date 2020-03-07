#coding:utf-8
import os
import logging

root_path = 'D:\source_codes\python\Sentiment\sentiment_detection\data\dict\zh\categories'


for i,j,k in os.walk(root_path):
    filenames = k

with open(root_path + '\\' + 'my_dict_zh.txt', 'w', encoding='utf-8') as output_file:
    for filename in filenames:
        with open(root_path + '\\' + filename, 'r', encoding='utf-8') as f:
            for text_num, line in enumerate(f):
                output_file.write(line)
                #line = line.strip('\n')
                if (text_num + 1) % 100000 == 0:
                    logging.info("finished %d rows for stop_words" % (text_num + 1))
        f.close()

print("finished combine txt files")
output_file.close()


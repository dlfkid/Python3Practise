# -*- coding:utf-8 -*

# 任一个英文的纯文本文件，统计其中的单词出现的个数。

import re

def count_words(path):
    with open(path) as text_file:
        text = text_file.read()
        words_array = re.findall(r"\w", text)
        words_count = len(words_array)
    return words_count


if __name__ == '__main__':
    file_name = "0004Text.md"
    words_num = count_words(file_name)
    print("There are {words_count} words in file {file_name}".format(words_count=words_num, file_name=file_name))
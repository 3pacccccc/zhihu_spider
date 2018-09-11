# -*- coding:utf-8 -*-
__author__ = 'maruimin'


def str_to_int(text):
    #将'12,545'字样的字符串转换为数字
    int_dict = text.split(',')    #将传进来的text split为一个dict
    a = 0
    b = len(int_dict)
    for x in int_dict:
            a = a + int(x)*1000**(b-1)
            b = b-1
    return a
if __name__ == '__main__':
    str_to_int('555')


    #print(12*1000**1)
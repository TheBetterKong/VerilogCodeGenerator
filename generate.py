"""
author：TheBetterKong
data:   2021/06/04

使用场景：
    在写 verilog 汇编代码时往往很多内容都是重复的，它们仅仅是 pin 编号不同
    例如：
        FullAdder	fir1fa1( pp0[2], pp1[1], pp2[0], Fir1_S[1], Fir1_C[1] );
        FullAdder	fir1fa2( pp0[3], pp1[2], pp2[1], Fir1_S[2], Fir1_C[2] );
        FullAdder	fir1fa3( pp0[4], pp1[3], pp2[2], Fir1_S[3], Fir1_C[3] );
        FullAdder	fir1fa4( pp0[5], pp1[4], pp2[3], Fir1_S[4], Fir1_C[4] );
        ...

    本脚本提供这种代码的一键生成

代码很简单，也可根据自己情况，利用正则表达式，修改成更加复杂的情况
"""

import re


def generate_terminal():
    s = input('> 输入文本模板（需要替换的地方用 {} 表示：')
    count = int(input('> 输入生成的数量：'))
    for n in range(0, count):
        print(s.replace(r'{}', str(n)))


def generate_txt():
    filename = 'moshi.txt'
    count = int(input('> 输入生成的数量：'))

    with open(filename, 'r') as f1:
        s = f1.read()

    with open('result.txt', 'w+') as f2:
        for n in range(0, count):
            snew = s.replace(r'{}', str(n))
            f2.write(snew)
            f2.write('\n')
            f2.write('\n')


if __name__ == '__main__':
    print('''
------------------ 重复代码自动生成脚本 ----------------
author：TheBetterKong
data:   2021/06/04

使用说明：
    moshi.txt   用来存放模板，需要自动生成的位置用'{}'表示
    result.txt  生成的结果
----------------------- welcome -----------------------
功能模式：
0： 命令行       适用于简单的单行代码生成
1： 文件         适用于复杂文本生成
    ''')

    tag = input("> 选择使用模式(0/1)：")
    if tag == '0':
        generate_terminal()
    elif tag == '1':
        generate_txt()

    print('''
----------------------- 生成完毕 -----------------------
    ''')

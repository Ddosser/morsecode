#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

__author__ = "Ddosser"
__version__  = 'v0.1'

morse_encode = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
    }
    
morse_decode = {
        '---':  'O', '--.':   'G', '-...':   'B', 
        '-..-': 'X', '.-.':   'R', '--.-':   'Q', 
        '--..': 'Z', '.--':   'W', '..---':  '2', 
        '.-':   'A', '..':    'I', '-.-.':   'C', 
        '..-.': 'F', '-.--':  'Y', '-':      'T', 
        '.':    'E', '.-..':  'L', '...':    'S', 
        '..-':  'U', '.----': '1', '-----':  '0', 
        '-.-':  'K', '-..':   'D', '----.':  '9', 
        '-....':'6', '.---':  'J', '.--.':   'P', 
        '....-':'4', '--':    'M', '-.':     'N', 
        '....': 'H', '---..': '8', '...-':   'V', 
        '--...':'7', '.....': '5', '...--':  '3'
    }

class MorseCode(object):
    """docstring for MorseCode"""
    def __init__(self):
        super(MorseCode, self).__init__()
        
    def encode(self, raw_str):
        morse = raw_str.strip().upper()
        return " ".join([morse_encode[m] for m in morse if m])

    def decode(self, en_str):
        p = [morse_decode[e.upper()] for e in en_str.split(" ") if e]
        return "".join(p)

def usage():
    print '*'*60
    print "Usage: python morsecode.py -[e|d] [-f <file>] [-o <file>]"
    print "-e       escape input string or file."
    print "-d       decode."
    print "-f       input from file."
    print "-o       output to file."
    print "-h       for help."
    print '*'*60
    exit(0)

def main():
    args = sys.argv
    ed = MorseCode()

    if len(args) < 2 or '-h' in args:
        usage()

    if '-e' in args:
        flag = False
    elif '-d' in args:
        flag = True
    else:
        usage()

    if '-f' in args:
        in_file = args[3]
        r = open(in_file, "r")
        raw_str = r.read()
        r.close()
    else:
        raw_str = raw_input("请输入：")

    if flag:
        result = ed.decode(raw_str)
    else:
        result = ed.encode(raw_str)

    if '-o' in args:
        out_file = args[5]
        w = open(out_file, "w")
        w.write(result.encode('utf-8'))
        w.close()
    else:
        print flag and "解密结果：" or "加密结果："
        print "\033[1;32m" + result + "\033[0m"

        
if __name__ == '__main__':
    main()

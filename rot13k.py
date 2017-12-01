import sys
import getopt
import copy
import argparse

LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];


def rot13k(string,key):
    result = ""
    i = 0
    letters_original = copy.copy(LETTERS)
    for char in key:
        if char.isupper():
            char = char.lower()
        LETTERS.insert(i,char)
        i = i + 1
    s = []
    for x in LETTERS:
        if x not in s:
            s.append(x)
    print(letters_original)
    print(s)
    result = ""
    for x in string:
        if x.isupper():
            x = x.lower()
        index1 = letters_original.index(x)
        index2 = index1+13
        result += s[index2 % len(s)] 
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--string', required=True,help="String to crypt")
    parser.add_argument('--key',required=True,help="Key")
    args = parser.parse_args()
    result = rot13k(args.string,args.key)
    print result

        

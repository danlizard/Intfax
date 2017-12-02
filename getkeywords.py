#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
charact = set('qwertyuiopasdfghjk lzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю1ё23456780')
def make_header(raw_text):
    #print(raw_text)
    raw_text = list(raw_text.lower())
    q = raw_text
    for i in range(len(raw_text)):
        if raw_text[i] not in charact:
            raw_text[i] = ''
    arr = ("".join(raw_text)).split()
    good = {"NOUN", "ADJS", "ADJF", "COMP", "VERB", "INFN", "PRTF", "PRTS", "GRND", "NUMR", "NUMB"}
    ans = []
    for el in arr:
        if morph.parse(el)[0].tag.POS in good:
            ans.append(el)
    #print(ans)
    return ans
if __name__ == "__main__":
    s = 'С космодрома Плесецк запущен "Союз" с военным спутником'
    print(" ".join(make_header(s)))
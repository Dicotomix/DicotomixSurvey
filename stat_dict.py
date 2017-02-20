#!/usr/bin/env python
# -*- coding: utf-8 -*-

from srv import *

def word_length():
    val = [0] * 26
    for i in range(len(myd.words_s)):
        val[len(myd.words_s[i])] += myd.words_x[i + 1] - myd.words_x[i]
    return val

print(word_length())

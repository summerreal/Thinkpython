"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def signature(s):
    """Returns the signature of this string.

    Signature is a string that contains all of the letters in order.

    s: string
    返回此字符串的签名。

签名是一个字符串，按顺序包含所有字母。

    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """Finds all anagrams in a list of words.

    filename: string filename of the word list

    Returns: a map from each word to a list of its anagrams.
    查找单词列表中的所有字谜。
    文件名：单词列表的字符串文件名
    返回：从每个单词到其字谜列表的映射。
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        # TODO: rewrite using defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    """Prints the anagram sets in d.

    d: map from words to list of their anagrams
    打印 d 中的字谜集。
     D：从单词映射到其字谜列表
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    """Prints the anagram sets in d in decreasing order of size.

    d: map from words to list of their anagrams
    以 d 为单位按大小降序打印字谜集。
    D：从单词映射到其字谜列表
    """
    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print(x)


def filter_length(d, n):
    """Select only the words in d that have n letters.

    d: map from word to list of anagrams
    n: integer number of letters

    returns: new map from word to list of anagrams
    仅选择 d 中包含 n 个字母的单词。

    D：从单词到字谜列表的映射
    n：整数个字母

    返回：从单词到字谜列表的新映射
    """
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


if __name__ == '__main__':
    anagram_map = all_anagrams('chap14\words.txt') #查找单词列表中的所有字谜。
    print_anagram_sets_in_order(anagram_map) #以 d 为单位按大小降序打印字谜集。

    eight_letters = filter_length(anagram_map, 26) #仅选择 d 中包含 n 个字母的单词
    print_anagram_sets_in_order(eight_letters) #以 d 为单位按大小降序打印字谜集。

    

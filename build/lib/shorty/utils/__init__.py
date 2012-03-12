from multiprocessing.dummy import list

__author__ = 'cingusoft'

ALPHABET = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

#Bijective methods for encode and decode id
def url_encode(i):
    if i == 0:
        return ALPHABET[0]
    s = ''
    base = len(ALPHABET)
    while i > 0:
        s += ALPHABET[i % base]
        i /= base
    return s[::-1]

def url_decode(s):
    i = 0
    base = len(ALPHABET)
    for char in s:
        i = i*base+ALPHABET.index(char)
    return i
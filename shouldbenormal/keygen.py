#!/usr/bin/env python3
"""Keygen for ALittlePatate's ShouldBeNormal."""

import itertools
import sys

MASK = 0xffffffff
H0 = 0xc001d00d
MUL = 0x045d9f3b
ROT = 7
ADD = 0x01234567
TARGET = 0x7c7652d1
LENGTH = 11
MULINV = pow(MUL, -1, 1 << 32)


def rol32(x, n):
    return ((x << n) | (x >> (32 - n))) & MASK


def ror32(x, n):
    return ((x >> n) | (x << (32 - n))) & MASK


def step(h, c):
    h ^= c
    h = (h * MUL) & MASK
    h = rol32(h, ROT)
    return (h + ADD) & MASK


def finv(y):
    x = ror32((y - ADD) & MASK, ROT)
    return (x * MULINV) & MASK


def digest(password):
    h = H0
    for c in password.encode():
        h = step(h, c)
    return h


def backward(h, suffix):
    for c in reversed(suffix.encode()):
        h = finv(h) ^ c
    return h


def generate(prefix, alphabet="abcdefghijklmnopqrstuvwxyz"):
    # prefix(4) + middle(3) + suffix(4) = 11 characters.
    if len(prefix) != 4:
        raise ValueError("prefix must contain exactly four characters")

    suffixes = {}
    for chars in itertools.product(alphabet, repeat=4):
        suffix = "".join(chars)
        suffixes.setdefault(backward(TARGET, suffix), suffix)

    h_prefix = H0
    for c in prefix.encode():
        h_prefix = step(h_prefix, c)

    for chars in itertools.product(alphabet, repeat=3):
        middle = "".join(chars)
        h = h_prefix
        for c in middle.encode():
            h = step(h, c)
        suffix = suffixes.get(h)
        if suffix is not None:
            candidate = prefix + middle + suffix
            if digest(candidate) == TARGET:
                yield candidate


def main():
    prefixes = sys.argv[1:] or ["wolf", "tree", "wish", "snow"]
    for prefix in prefixes:
        for candidate in generate(prefix):
            print(candidate)


if __name__ == "__main__":
    main()

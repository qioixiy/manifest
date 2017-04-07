#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import json
import codecs

class insertRecord():
    '''
    insert a Record
    '''
    def __init__(self):
        self.obj = {}
        infile=open("repos.json", 'rb')
        os.rename("repos.json", "repos.json.bk")
        with infile:
            try:
                self.root = json.load(infile)
            except ValueError, e:
                raise SystemExit(e)

    def make(self):
        self.input("url")
        self.input("desc")
        self.input("tag")
        self.input("star")

        self.insert(self.obj)
        outfile = codecs.open("repos.json", 'wb', 'utf-8')
        with outfile:
            json.dump(self.root, outfile, sort_keys=True, ensure_ascii=False,
                      indent=4, separators=(',', ': '))

    def insert(self, item):
        self.root["url"].append(item)

    def input(self, title):
        sys.stdout.write(title+": ")
        key=sys.stdin.readline()[:-1]
        if (len(key)==0):
            return
        self.obj[title]=key[:len(key)]

# main
if __name__ == '__main__':
    insertRecord().make()

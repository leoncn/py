#!/usr/bin/env python
import os
import os.path as path
import sys

def walk_dir(work_dir='.'):
    for it in os.listdir(work_dir):
        full_path = path.join(work_dir,it)
        if path.isfile(full_path):
            yield full_path
        else:
            for it in walk_dir(full_path):
                yield it


if __name__ == '__main__':
    _dir = '.'
    if(len(sys.argv) > 1):
        _dir = sys.argv[1]
        
    for it in walk_dir(_dir):
        print it
#!/usr/bin/env python
#
# verify_md5.py
# Author: Jim Sam

import os
import hashlib

# This function, md5_for_file was copied from StackOverflow. Please see:
# http://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python#1131238
def md5_for_file(f, block_size=2**20):
    m = hashlib.md5()
    with open(f, "rb" ) as f:
        while True:
            buf = f.read(block_size)
            if not buf:
                break
            m.update( buf )
    return m.hexdigest()

def get_hash(m):
    with open(m, 'r') as f:
        for line in f:
            if ' *' in line:
                a = line.split(' *')
                hashcode = a[0]
    return hashcode

def cycle_files(md5_list):
    did_verified = []
    not_verified = []
    for m in md5_list:
        verified = False
        filename = m[:-4]
        generated_hashcode = md5_for_file(filename)
        derived_hashcode = get_hash(m)
        if generated_hashcode == derived_hashcode:
            verified = True
            did_verified = did_verified + [filename]
        if not verified:
            not_verified = not_verified + [filename]
    return did_verified, not_verified

def make_file_list(dir1, ext):
    file_list = []
    for f in dir1:
        file_name=str(f)
        if file_name[-4:].lower() == ext:
            file_list.append(file_name)
    return file_list

def main():
    this_dir = os.listdir('.')
    md5_list = make_file_list(this_dir, '.md5')
    verified, not_verified = cycle_files(md5_list)
    print "The following verified: \n"
    for f in verified:
        print f
    print "\nThe following failed to verify: \n"
    for f in not_verified:
        print f


if __name__ == '__main__':
    main()
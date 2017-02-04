#!/usr/bin/env python
#
# create_tree.py
# This script generates an indexed md5 checksum for every file in the directory.
# It does not verify checksums. Please see verify_tree.py for verification.
#

import os
import hashlib

def md5_for_file(f, block_size=2**20):
    '''
    This function, md5_for_file was copied from StackOverflow, used under the
    Creative Commons license outlined at http://blog.stackoverflow.com/2009/06/attribution-required/

    SO User Yuval Adam. http://stackoverflow.com/users/24545/yuval-adam
    Code: http://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python#1131238
    '''
    m = hashlib.md5()
    with open(f, "rb" ) as f:
        while True:
            buf = f.read(block_size)
            if not buf:
                break
            m.update( buf )
    return m.hexdigest()

def main():
    folder = os.getcwd()
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.startswith('.'):
                continue
            full_file = os.path.join(root, f)
            new = os.path.join(full_file+'.md5')
            if os.path.isfile(new):
                continue
            elif '.md5.' in new:
                continue
            else:
                print("Making MD5 for %s now." % full_file)
                m = md5_for_file(full_file)
                with open(new, 'w') as n:
                    n.write(m+' *'+f)
                    n.close()

    print("\nDone!\n")


if __name__ == '__main__':
    main()

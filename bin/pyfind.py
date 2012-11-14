#!/usr/bin/python

import sys
import argparse
import os
from stat import *
import fnmatch

def matching(thing, args):
    if args.name:
        if not fnmatch.fnmatch(thing, args.name):
            return False
    return True

def search(dir, depth, args):
    if args.verbose:
        print "Now searching in directory {:}".format(dir)
    things = os.listdir(dir)
    for thing in things:
        if args.verbose:
            print "Checking {:}".format(thing)

        path = os.path.join(dir, thing)
        # TODO check the conditions in args
        if matching(thing, args):
            print "  " * depth + thing
        mode = os.stat(path).st_mode
        if S_ISDIR(mode):
            search(path, depth+1, args)
        
def main():
    dirs = []
    while len(sys.argv) > 1 and sys.argv[1][0] != '-':
        dirs.append( sys.argv.pop(1) )

#    if len(dirs) == 0:
#        print "At least a directory name is reqired. "
    #print dirs
    parser = argparse.ArgumentParser(description='Find things in the filesystem')
    parser.add_argument('--name', type=str, default=None, help='Wilde card to be matched')
    parser.add_argument('--verbose', '-v', help='Verbosity level', action='count')
    #parser.add_argument('--sum', dest='accumulate', action='store_const',
    #               const=sum, default=max,
    #               help='sum the integers (default: find the max)')

    args = parser.parse_args()

    if args.verbose:
        print "Search for {:} in directories {:}".format(args.name, dirs)

    for dir in dirs:
        search(dir, 0, args)
      
    
if __name__ == '__main__':
    main()

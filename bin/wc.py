#!/usr/bin/python

import argparse

def main():
    parser = argparse.ArgumentParser(description='Find things in the filesystem')
    parser.add_argument('file', type=str, nargs='*', help='One or more filenames')
    args = parser.parse_args()
    #print args.file
    total = {
        'lines' : 0,
        'words' : 0,
        'chars' : 0,
    }
    for filename in args.file:
        print filename,
        count = {
            'lines' : 0,
            'words' : 0,
            'chars' : 0,
        }
        fh = open(filename, 'r')
        for line in fh.readlines():
            count['lines'] += 1;
            #print line,
        print count['chars'], count['words'], count['lines']
        for f in count.keys():
            total[f] += count[f]
    print "\nTotal:", total['chars'], total['words'], total['lines']

if __name__ == '__main__':
    main()

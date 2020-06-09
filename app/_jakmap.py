import sys, argparse

from classes import *

# I am supposed to be a naive cli interface


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='jmap implementation')
    parser.add_argument('--list', action="count"
                        ,help='show all ')
    parser.add_argument('--search', nargs="+", required=False
                        ,help='search for something')
    
    args = parser.parse_args()
    
    if args.list:
        print("Listing stuff..")

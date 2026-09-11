import argparse
import configparser
from datetime import date
#Why grp,pwd? Git saves the owner/group ID
try: 
    import grp,pwd
except ModuleNotFoundError:
    pass    
#.gitignore
from fnmatch import fnmatch
#Git uses SHA-1, used as ID for trees,blobs and commits
import hashlib
from math import ceil
import os
import re
import sys
#Git compress using zlib
import zlib




argparser=argparse.ArgumentParser(description="NotGitShell :P")
argsubparsers= argparser.add_subparsers(title="Commands",dest="command")

def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "init":
            cmd_init(args)
        case "add":
            cmd_add(args)
        case "commit":
            cmd_commit(args)
        case "stauts":
            cmd_status(args)
        case _:
            print("Bad Command.")    


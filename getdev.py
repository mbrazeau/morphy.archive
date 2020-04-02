#!/usr/bin/env python

# This script will clone all of the relevant development branches of the
# Morphy project if you would like to build a bleeding-edge development
# version. It also simplifies the entire process of cloning and building,
# particularly for any users who do not have Google's repo tool installed.

import  sys, os, getopt, multiprocessing, platform, shutil
from subprocess import call

def pullAll():
    os.system("git -C ./mpl pull")
    os.system("git -C ./nui pull")

def cloneAllDev():
    os.system("git clone --branch development https://github.com/mbrazeau/mpl.git ./mpl/")
    os.system("git clone --branch dev https://github.com/mbrazeau/nui.git ./nui/")
    os.system("git clone --branch dev https://github.com/mbrazeau/buildMorphy.git ./build/")
    os.system("git clone https://github.com/cdesjardins/wineditline.git ./external/wineditline")
    os.system("git clone https://github.com/mtholder/ncl.git ./external/ncl/")

def main(argv):

    args = ["update"]

    print("Fetching all Morphy subprojects.")
    
    if (len(argv) > 0):
        if (argv[0] == "update"):
            pullAll()
        else:
            print("Unrecognised argument")
    else:
        cloneAllDev()

if __name__ == "__main__":
    main(sys.argv[1:])

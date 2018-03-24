#!/usr/bin/python3
#coding: utf8

import os
import sys


DST_PATH = "bin"


def build_coreutils(repo_path):
    if not os.path.exists(repo_path) or not os.path.isdir(repo_path):
        raise Exception("path not exists!")

    cwd = os.getcwd()
    os.chdir(repo_path)

    cmd = "cargo build --all --release"
    print(cmd)
    os.system(cmd)
    os.chdir(cwd)

    target_path = os.path.join(repo_path, "target", "release")

    for filename in os.listdir(target_path):
        filepath = os.path.join(target_path, filename)
        if os.path.isfile(filepath):
            if "." not in filename:
                dst_path = os.path.join(DST_PATH, filename)
                cmd = "cp %s %s" % (filepath, dst_path)
                print(cmd)
                os.system(cmd)

def main():
    if not os.path.exists(DST_PATH):
        raise Exception("DST_PATH not exists!")

    cwd = os.getcwd()

    build_coreutils(os.path.join(cwd, "..", "coreutils"))


if __name__ == '__main__':
    main()
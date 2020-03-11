# -*- coding: utf-8 -*-

import argparse
import threading as th;


parser = argparse.ArgumentParser()

parser.add_argument('--paramA', type=str, default='参数B')

arg=parser.parse_args()

#print(parser.get_default('paramA'))


def main():
    print(arg.paramA)

if __name__ == '__main__':
    main()

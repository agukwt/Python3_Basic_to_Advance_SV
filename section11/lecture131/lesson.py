#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import sys
from optparse import OptionParser
from optparse import OptionGroup


def main():
    usage = 'usage %prog [option] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string',
                      dest='filename', help='File name')
    parser.add_option('-n', '--num', action='store', type='int', dest='num')

    # optionが指定されれば、固定boolean設定 / defaultはoption指定に依らない。
    parser.add_option('-v', action='store_true', dest='verbose', default=True)
    parser.add_option('-q', action='store_false', dest='verbose', default=False)
    parser.set_defaults(verbose=True)

    # optionが指定されれば、固定値設定
    parser.add_option('-r', action='store_const', const='root', dest='user_name')

    # Call back
    parser.add_option('-e', dest='env')

    def is_release(option, opt_str, value, parser):
        if parser.values.env == 'prd':
            raise parser.error("Can't release")
        setattr(parser.values, option.dest, True)
    parser.add_option('--release', action='callback', callback=is_release, dest='release')

    # 通常と異なるOptionを指定する
    group = OptionGroup(parser, 'Dangerous Options')
    group.add_option('-g', action='store_true', help='Group option')
    parser.add_option_group(group)

    options, args = parser.parse_args()

    print(options)
    print(args)

    print(options.filename)
    print(options.num)
    print(options.verbose)


if __name__ == '__main__':
    main()

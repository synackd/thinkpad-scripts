#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2014 Martin Ueding <dev@martin-ueding.de>
# Licensed under The GNU Public License Version 2 (or later)

import configparser
import os.path

import termcolor

CONFIGFILE = os.path.expanduser('~/.config/thinkpad-scripts/config.ini')
'Path of global config file'

def get_config():
    config = configparser.ConfigParser()

    config.read('default.ini')
    if os.path.isfile(CONFIGFILE):
        config.read(CONFIGFILE)

    return config

def print_config(config):
    for section in sorted(config.sections()):
        termcolor.cprint(section, attrs=('bold',))

        for key in sorted(config[section]):
            print(termcolor.colored(key, 'yellow'), config[section][key])

def main():
    print_config(get_config())

if __name__ == '__main__':
    main()
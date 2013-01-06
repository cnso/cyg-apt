"""
  cyg-apt - a Cygwin package manager.

  (c) 2002--2009 Chris Cormie         Jan Nieuwenhuizen
                 <cjcormie@gmail.com> <janneke@gnu.org>
  (c) 2012       James Nylen
                 <jnylen@gmail.com>
  (c) 2012-2013  Alexandre Querci
                 <alquerci@email.com>

  License: GNU GPL
"""

import argparse

class CygAptArgParser():
    def __init__(self, usage=None, scriptname=None):
        self.usage = usage
        self.scriptname = scriptname

    def parse(self):
        commands = ['setup',
                    'update',
                    'ball',
                    'download',
                    'filelist',
                    'find',
                    'help',
                    'install',
                    'list',
                    'md5',
                    'missing',
                    'new',
                    'purge',
                    'remove',
                    'requires',
                    'search',
                    'show',
                    'source',
                    'upgrade',
                    'url',
                    'version',
                    ]

        parser = argparse.ArgumentParser(prog=self.scriptname,
                                         add_help=False,
                                         usage=self.usage)

        parser.add_argument('command',
                            nargs='?',
                            default='help',
                            choices=commands
                            )

        parser.add_argument('package',
                            nargs="*")

        parser.add_argument('-q', '--quiet',
                            action='store_false',
                            default=True,
                            help='Loggable output - no progress indicator',
                            dest="verbose")

        parser.add_argument('-d', '--download',
                            action='store_true',
                            dest='download_p',
                            help='download only')

        parser.add_argument('-m', '--mirror',
                            nargs=1,
                            help='use mirror')

        parser.add_argument('-t', '--dist',
                            nargs=1,
                            dest='distname',
                            default='curr',
                            choices=['curr', 'test', 'prev'],
                            help='set dist name')

        parser.add_argument('-a',
                            action='store_true',
                            dest='noupdate',
                            help='do not update')

        parser.add_argument('-x', '--no-deps',
                            action='store_true',
                            dest='nodeps_p',
                            help='ignore dependencies')

        parser.add_argument('-s', '--regexp',
                            action='store_true',
                            dest='regex_search',
                            help='search as regex pattern')

        parser.add_argument('-f', '--nobarred',
                            action='store_true',
                            help='add/remove packages cyg-apt depends on')

        parser.add_argument('-X', '--no-verify',
                            action='store_false',
                            dest='verify',
                            help='do not verify setup.ini signatures')

        parser.add_argument('-y', '--nopostinstall',
                            action='store_true',
                            help='do not run postinstall scripts')

        parser.add_argument('-z', '--nopostremove',
                            action='store_true',
                            help='do not run preremove/postremove scripts')

        parser.add_argument('-h', '--help',
                            action='store_true',
                            help='show brief usage')

        args = parser.parse_args()

        return args

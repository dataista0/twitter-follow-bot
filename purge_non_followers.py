#!/usr/bin/env python

import codecs
import sys

from twitter_follow_bot import auto_unfollow_nonfollowers


def main():
    auto_unfollow_nonfollowers()


if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    main()

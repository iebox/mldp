#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#--include-module=encodings.ascii
#--include-modules=encodings.ascii,encodings-utf_8

from lib.display import *

class Singleton(object):
    def __new__(cls):
      if not hasattr(cls, 'instance'):
        cls.instance = super(Singleton, cls).__new__(cls)
      return cls.instance


def try_singleton():
    # running
    s = Singleton()
    display_memary_address(s)
    s1 = Singleton()
    display_memary_address(s1)


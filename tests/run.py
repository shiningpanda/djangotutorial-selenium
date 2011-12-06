# -*- coding: utf-8 -*-
import os
import sys
import nose

testdir = os.path.dirname(os.path.abspath(__file__))
basedir = os.path.dirname(testdir)

sys.path.insert(0, basedir)
sys.path.insert(1, os.path.join(basedir, 'djangotutorial'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

os.chdir(testdir)

nose.main()
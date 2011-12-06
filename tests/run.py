# -*- coding: utf-8 -*-
import os
import sys
import nose

folder = os.path.dirname(os.path.abspath(__file__))
base = os.path.dirname(folder)

sys.path.insert(0, base)
sys.path.insert(1, os.path.join('djangotutorial'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

os.chdir(folder)

nose.main()
#!/usr/bin/env python2.7

import os
import sys
#import shutil
from shutil import copy2

home = '/home/thomas'

files = [
		('.Xresources','Xresources'),
		('.xbindkeysrc','xbindkeys'),
		('.Xmodmap','Xmodmap'),
		('.xinitrc','xinitrc')
		]

try: x = sys.argv[1]
except: exit()

if x == 'deploy':
	print 'deploying'
	for f in files:
		copy2(f[1],os.path.join(home,f[0]))


elif x == 'update':
	print 'updating'
	for f in files:
		print f[0]
		copy2(os.path.join(home,f[0]),f[1])



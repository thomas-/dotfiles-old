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
		('.xinitrc','xinitrc'),
		('.i3/config','i3/config'),
		('.i3/conkystatus','i3/conkystatus')
		]

try: x = sys.argv[1]
except: print "no argument specified"; exit()

if x == 'deploy':
	print 'deploying'
	for f in files:
		copy2(f[1],os.path.join(home,f[0]))


elif x == 'update':
	print 'updating'
	for f in files:
		if os.path.dirname(f[1]) is not '':
			if not os.path.isdir(os.path.dirname(f[1])):
				os.makedirs(os.path.dirname(f[1]))
		copy2(os.path.join(home,f[0]),f[1])



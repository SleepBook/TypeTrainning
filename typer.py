#this is a small tools for improving my typing
#written by oar, 23/07/2016
#I'am very sad today, lastnight i see my last close friend off
#I feel like a real lonely spirit now.
from provider import *

def typer():
	print 'welcome to this typing exercise program'
	while 1:
		print 'please select the exercise mode'
		print '\t1) continuous mode'
		print '\t2) discrete mode'

		mode = int(raw_input())
		while mode not in (1,2):
			print 'invalid input, select again'
			mode = int(raw_input())

		content = content_generator(mode)

		cmd = engine(content)
		if cmd == 1:
			break
	print 'bye'


if __name__ == '__main__':
	typer()

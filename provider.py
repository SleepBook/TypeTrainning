import datetime
import random
import getch
import pdb


def content_generator(mode):
	if mode == 1:
		print 'please specify the start character'
		start = ord(raw_input())
		print 'please specify the end character'
		end = ord(raw_input())
		content = [chr(i+start) for i in range(end-start + 1)]
		return content

	else:
		print 'please enter the character you want to exercise'
		print 'split by a space and hit enter when you finish'
		content = raw_input().split()
		return content
		

def engine(content):
	print 'start endless exercise, when you feel it\'s enough',
	print 'press \'2\'to exit the program, enter 1 to start new exercise'
	
	length = len(content)
	stat = []
	for i in range(length):
		stat.append([0,0,0])

	#warm up
	for char in content:
		show(char)
	for i in range(length)[::-1]:
		show(content[i])
	for i in range(length)[::-1]:
		show(content[i])

	#real exercise
	while 1:
		selector = random.randint(0,length-1)
		ans,delay = show(content[selector])
		#print 'the char is',content[selector],ans,delay
		if ans == 3 or ans == 4:
			break
		else:
			stat[selector][0] += 1
			stat[selector][1] += ans
			stat[selector][2] += delay
		#print 'the refresh result is',stat[selector][0],stat[selector][1]

	show_stat(content,stat)
	if ans == 4:
		return 1
	else:
		return 0



def show_stat(content, stat):
	print 'show statistic for this exercise'
	print '*'*60
	print '*'*60
	print 'character\terror time\terror rate\tavg. reponse time'
	print '*'*60
	for i,char in enumerate(content):
		#try:
		#	error_rate = stat[i][1]/stat[i][0]
		#	avg_time = stat[i][2]/stat[i][0]
		#except ZeroDivisionError:
		#	print 'the character is ',content[i]
		#	print stat[i][0],stat[i][1],stat[i][2]

		#pdb.set_trace()
		print '%c\t%d\t%2f\t%4f'%(char,stat[i][1],stat[i][1]/float(stat[i][0]),stat[i][2]/float(stat[i][0]))
		#print char,'\t',stat[i][1],'\t',stat[i][1]/float(stat[i][0])
		print '*'*60


def show(char):
	print char
	start = datetime.datetime.now()
	ans = getch.getch()
	end = datetime.datetime.now()
	duration = (end-start).total_seconds()*1000
	if ans == char:
		return (0,duration)
	elif ans == '2':
		return (4,duration)
	elif ans == '1':
		return (3,duration)
	else:
		return (1,duration)
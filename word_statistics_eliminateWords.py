# script by IJ 2017-12-01

##################################################################
# puts all words together in to 3 files
i = 1			# count ALL files

open("s_many0.txt", 'w')
many0 = open("s_many0.txt", 'a')
open("s_use0.txt", 'w')
use0 = open("s_use0.txt", 'a')
open("s_single0.txt", 'w')
single0 = open("s_single0.txt", 'a')

while i <= 10 :

	if i == 1 :
		n_up = 1327
		n_do = 15
	elif i == 2 :
		n_up = 416
		n_do = 9
	elif i == 3 :
		n_up = 490
		n_do = 9
	elif i == 4 :
		n_up = 524
		n_do = 9
	elif i == 5 :
		n_up = 584
		n_do = 7
	elif i == 6 :
		n_up = 637
		n_do = 7
	elif i == 7 :
		n_up = 1037
		n_do = 9
	elif i == 8 :
		n_up = 1442
		n_do = 13
	elif i == 9 :
		n_up = 908
		n_do = 8
	elif i == 10 :
		n_up = 1047
		n_do = 10
		
	r = open("stats_a%d_percent.txt" % (i), "r")
	for line in r :
		l = str(line)
		wo = l.split()[0]
		num = int(l.split()[1])
		
		if num > n_up : many0.write("%s\n" % (wo))
		elif num < n_do : single0.write("%s\n" % (wo))
		else : use0.write("%s\n" % (wo))			
		
	r.close()
	print("done with score %d file " % (i))
	i += 1

many0.close()
single0.close()
use0.close()

##################################################################
# make single word per repetition (in a not clever, but easy way)

from collections import Counter

#-------------
open("s_many1.txt", 'w')
many1 = open("s_many1.txt", 'a')

r_many0 = open("s_many0.txt", 'r')
wordcount_many = Counter(r_many0.read().split())
for item in wordcount_many.items():
	many1.write("{:30}{:7}\n".format(*item))
r_many0.close()
many1.close()

print ("many file generated")
#---------------

open("s_single1.txt", 'w')
sing1 = open("s_single1.txt", 'a')

r_sing0 = open("s_single0.txt", 'r')
wordcount_sing = Counter(r_sing0.read().split())
for item in wordcount_sing.items():
	sing1.write("{:30}{:7}\n".format(*item))
r_sing0.close()
sing1.close()
print ("single file generated")		
#---------------
open("s_use1.txt", 'w')
use1 = open("s_use1.txt", 'a')

r_use0 = open("s_use0.txt", 'r')
wordcount_use = Counter(r_use0.read().split())
for item in wordcount_use.items():
	use1.write("{:30}{:7}\n".format(*item))
r_use0.close()
use1.close()
print ("use file generated")		

##################################################################
# put words in one line

open("s_many2.txt", 'w')				# many file
m2 = open("s_many2.txt", 'a')
rm1 = open("s_many1.txt", 'r')
rm1.readline(0)
for line in rm1 :
	l = str(line)
	wo = l.split()[0]
	m2.write("%s\n" % (wo))
m2.close()
rm1.close()

open("s_use2.txt", 'w')					# use file
m2 = open("s_use2.txt", 'a')
rm1 = open("s_use1.txt", 'r')
rm1.readline(0)
for line in rm1 :
	l = str(line)
	wo = l.split()[0]
	m2.write("%s\n" % (wo))
m2.close()
rm1.close()

open("s_single2.txt", 'w')				# single file
m2 = open("s_single2.txt", 'a')
rm1 = open("s_single1.txt", 'r')
rm1.readline(0)
for line in rm1 :
	l = str(line)
	wo = l.split()[0]
	m2.write("%s\n" % (wo))
m2.close()
rm1.close()


################################################################## HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!........
# make a list from words and remove form rem*** files
#rem_a1.txt

with open("s_many2.txt") as f:
    myList = list(f.read().splitlines())	# makeslist without break lines :) happy hour!!
print (myList)



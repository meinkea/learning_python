'''
CONTENTS:

49     If LOOPS

68     FOR LOOPS

86     RANGE and WHILE

99     COMMENTS and BREAK

135    CONTINUE   <<<<<<<<<< <<<<<<<<<<

150    FUNCTION

180    RETURN VALUE

205    VARIABLE SCOPE

220    KEYWORD ARGUMENTS

235    FLEXIABLE NUMBER OF ARGUMENTS   <<<<<<<<<< <<<<<<<<<<

250    UNPACKING ARGUMENTS

265    SETS

280    DICTIONARY

    MODULES

    DOWNLOADING IMAGES FROM THE WEB  (OUT of ORDER)   <<<<<<<<<< <<<<<<<<<<

    READ AND WRITE FILES

    DOWNLOADING FILES FROM THE WEB  (OUT of ORDER)




'''







##########  IF LOOPS  ##########

name = "Lucy"

#if name is "Bucky":
#    print("hey there Bucky!")
#elif name is "Lucy":
#    print("What up Lucedawg?")
#elif name is "Sammy":
#    print("What up Slammy?")
#else:
#    print("Please sign up for the site!")

#print('\n')
#print('--'*20)
#print('\n')



##########  FOR LOOPS  ##########


#foods = ['bacon', 'tuna', 'ham', 'snausages', 'beef']

#for i in foods:
#    print(i)
#    print(len(i))

#print('\n')
#print('--'*20)
#print('\n')

#for i in foods[1:4]:
#    print(i)
#    print(len(i))


#########  RANGE and WHILE  ##########

#        range is like, 1..N in math notation (start, end number~optional, increment~optional)
#for x in range(3, 40, 7):
#    print(x)

#buttcrack = 5

#while buttcrack < 10:
#    print(buttcrack)
#    buttcrack += 1  # Same as buttcrack = buttcrack + 1


##########  COMMENTS and BREAKS  ##########

#magicNumber = 89

# ok this program find a magic number
# a # is for a single line

'''
three little single quotes
is to make several
comments for multiple lines
HURRRRRAY!!!
'''

#for n in range(101):
#    if n is magicNumber:
#        print(n, "is the " + "Magic number")
#        break
#    else:
#        print(n)



#Divide = 4
#MAX =  100
#remainder = 0

#for i in range(1, MAX):
#    remainder = i%4

#    if remainder is 0:
#        print(i)
#    else:
#        continue


##########  CONTINUE  ##########   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#numbersTaken = [2, 5, 12, 13, 17]

#for n in range (1, 20):
#    if n in numbersTaken:
#        continue
#    print(n)
'''
continue stops the current iteration and moves onto the next one
'''



##########  FUNCTION  ##########

#   def declares the function

def beef(x, btc):
    print("DAYAM, functions are cool!")
    print(x)
    amount = btc *527


x = 100
btc = 20

beef(x, btc)

print('\n')

beef(10, 10)


def S(n):
    for i in range(1,n):
        print('')

#beef(3, 2584)
#S(5)
#beef(2, 6)



##########  RETURN VALUE  ##########


def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

buckys_limit = allowed_dating_age(27)
creepy_joe_limit = allowed_dating_age(49)
#print("Bucky can date girls", buckys_limit, "or older")
#print("Creepy Joe can date girls", creepy_joe_limit, "or_older")

def get_gender(sex='Unkown'):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "female"
    print(sex)

#get_gender('m')
#get_gender('f')
#get_gender()



##########  VARIABLE SCOPE  ##########


#a = 10
def corn():
    print(a)

def fudge():
    print(a)

#corn()

#fudge()


##########  KEYWORD ARGUMENTS  ##########


def dumb_sentance(name='Bucky', action='ate', item='tuna'):
    print(name, action, item)


#dumb_sentance()
#dumb_sentance("Salty", "farts", "Gently")
# to pass in a different number of arguments, or in a different order
#dumb_sentance(item='ME!', name='Jason')
#dumb_sentance(action='is', item='AWESOME')



##########  FLEXIABLE NUMBER OF ARGUMENTS  ##########   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def add_numbers(*arrrg):
    total = 0
    for a in arrrg:
        total += a
    print(total)

#add_numbers(3)
#add_numbers(3, 4)
#add_numbers(3, 4, 3)
#add_numbers(3, 4, 200)


##########  UNPACKING ARGUMENTS  ##########

def health_calculator(age, apples_ate, chocolatechips):
    answer = (100-age) + (apples_ate) - (chocolatechips * 2)
    print(answer)

bucks_data = [27, 20, 0]

#  The Long Way (not unpacking)
#health_calculator(bucks_data[0], bucks_data[1], bucks_data[2])

# THE SUPER SPECIAL AWESOME WAY! (UNPACKING ARGUMENTS LIKE YOUR COOL!)
#health_calculator(*bucks_data)


##########  SETS  ##########


#groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duct tape', 'lotion', 'beer'}
#print(groceries)

#if 'milk' in groceries:
#    print("You already have milk hoss")
#else:
#    print("Oh yea, you need milk")





##########  DICTIONARY  ##########


classmates = {'Tony':'cool but smells', 'Emma':'She sits behind me', 'Lucy':'I like her because she ask lots of questions'}

#print(classmates)
#S(1)
#print(classmates['Emma'])
#S(2)

# for whenever we loop though, treat k as the keyword and v as the value
# classmates is the dictionary we are looping through, and it's going to loop through all of the items

#for k, v in classmates.items():
#    print(k + v)


##########  MODULES  ##########

# lets is load another file's functions
import tuna
import random

# many other file's function's could have the same name
# therefor you mus specify the file you want to use the function from
# use this format >>>  filename.function()

#tuna.fish()

#x = random.randrange(1, 1000)
#print(x)


##########  DOWNLOAD AN IMAGE FROM THE WEB  ##########   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>> THIS CODE IS IN FACT NOT WORKING <<<
# >>> IT IS BROKE BROKE <<<

#import random
import urllib3.request

# str( ) turns a number to a string
# to download code from the web go to File(tab) >> Settings >> (Search) Project Interpreter

#def download_web_image(url):
#    name = random.randrange(1, 1000)
#    full_name = str(name) + ".jpg"
#    urllib3.request.

#download_web_image("https://thenewboston.com/images/video_categories/294.png")



##########  Reading and Writing to Files ##########

# open( ) get the file ready
# the first argument is what you would like the file's name to be
# the second argument is writing 'w' or reading 'r'

#fw = open('sample', 'w')
#fw.write('Writing some stuff in my text file\n')
#fw.write('I like bacon\n')
#fw.close()


#fr = open('sample.txt', 'r')
#text = fr.read()
#print(text)
#fr.close()

##########  Downloading Files from the Web  ##########

#from urllib import request

#goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1498679768&period2=1501271768&interval=1d&events=history&crumb=HfKdmMlJarC'

#def download_stock_data(csv_url):
#    response = request.urlopen(csv_url)
#    csv = response.read()


# the following is formatting

# split breaks up a long string
#    lines = csv_str.split("\\n")

# r means raw so you don't need to escape any characters
#    dest_url = r'goog.csv'

#    FX = open(dest_url, "w")
#    for line in lines:
#        fx.write(line + "\n")
#    fx.close()

#download_stock_data(goog_url)
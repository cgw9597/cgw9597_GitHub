#-*-coding:utf8
#heep://learnpythonthehardway.org/book/ex38.html
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while(len(stuff)) !=10:
    next_one = more_stuff.pop()
    print "Addig: %s" % next_one
    stuff.append(next_one)
    print "There as %d times now." % len(stuff)

print "There we go :%s" % stuff[1]
print "Let's do some things with stuff"

print "stuff[1] = %s" % stuff[1]
print "stuff[-1] = %s" % stuff[-1]
print "stuff.pop() = %s" % stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
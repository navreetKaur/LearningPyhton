print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'
print "Arithemetics"
print 2+4
print 8/2
print 8%2
print 6>8
rate = 12
tax = 24
total = rate + tax /100
print tax
rate = 12
tax = 24
total = rate + tax /100
print "tax is", tax
print "tax is %.2f"%tax
print "tax is %d"%tax
print "tax is %s"%tax
print "double tax is %.2f"%(tax +tax)

x = "'%d' students." % 10
y = "hello %s and bye %s." % ("you", "me")

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

print "." * 10 

x = "h"
y = "mn"
print x +y,
print x +y

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
print """hello, I am in a bus 
jello bello vello"""
print 'Lol"'
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


print "Enter Your Name:"
name = raw_input()
print "so your name is %s" %name
print "Enter Your Age:"
age = raw_input("We won't tell don't worry")
print "so your age is %s" %age

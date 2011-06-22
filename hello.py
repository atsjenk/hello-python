import sys

print "Hello World!"
for i in range(5):
  print "\t" , i

print "Input your name"
name = sys.stdin.readline().strip()
print "Hello %s!" % name

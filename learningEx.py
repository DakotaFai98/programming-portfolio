# python learning exercises

# Functions
def echo(thing):
	return thing

def swap(x,y):
	return y , x
	


def main_function():
	print "testing echo('marco'):", echo("marco")
	print "testing echo('shut up'):", echo("no, you shut up")
	print "testing swap('fame', 'fortune'):", swap('fame', 'fortune')

# Arithmetic Function

def reverse(x):
	return -x

def plus(x,y):
	return x + y

def diff(x,y):
	return y - x

def abs_diff(x,y):
	return abs(x - y)

def divide(x,y):
	return x/y

def remainder(x,y):
	return x%y

def power(x,y):
	return x ** y

def calculate(a,b,c,d,e,f):
	return 
	
def pythagoras(x,y):
	return (x+y)*(x+y)



def main_arithmetic():
	print "testing reverse(3): ", reverse(3)
	print "test plus(2,5): ", plus(2,5)
	print "test diff(7,2): ", diff(7,2)
	print "test abs_diff(-5,13): ", abs_diff(-5,13)
	print "test divide(4,2):", divide(4,2)
	print "test remainder(8,3): ", remainder(8,3)
	print "test power(6,2): ", power(6,2)
	print "test calculate(1,2,3,4,5,6):", calculate(1,2,3,4,5,6)
	print "testing pythagoras(2,5): ", pythagoras(2,5)


def main():
	main_function()
	main_arithmetic()

main()
import sys

print("The file running is "+sys.argv[0])
if len(sys.argv) == 1:
	print("There are no additional commands")
elif len(sys.argv) == 2:
	print(sys.argv[1])
elif len(sys.argv) == 3:
	arg1, arg2 = sys.argv[1:]
	print(int(arg1)+int(arg2))
else:
	print("There are "+str(len(sys.argv)-1)+" arguments after the file name")
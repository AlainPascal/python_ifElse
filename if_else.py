# !/usr/bin/python

print("hello, welcome to the python if ... else statement.");
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+");
print("\n1. Option One");
print("\n2. Option Two");
print("\n3. Option Three");
print("\n4. Option Four");
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+");

optNum = input("\nkindly select any number between [1, 2, 3, 4]: ");
print("\n");

# ___ start if ... else statement ___
if (int(optNum) == 1):
	print("\nOption selected is One.");
elif (int(optNum) == 2):
	print("\nOption selected is Two.");
elif (int(optNum) == 3):
	print("\nOption selected is Three.");
elif (int(optNum) == 4):
	print("\nOption selected is Four.");
else:
	optNum = input("\nkindly select any number between [1, 2, 3, 4]: ");
# ___ end if ... else statement ___
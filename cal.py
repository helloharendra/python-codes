#calculator first program

def add(x,y):
	return x+y
def substract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	return x%y

print("select options")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.division")

while True:
	choice=input("please select your choice(1/2/3/4)")
	if choice in ('1','2','3','4'):
		num1=float(input('ENTER FIRST NUMBER'))
		num2=float(input('ENTER SECOND NUMBER'))

		if choice =='1':
			print(num1,"+",num2,"=",add(num1,num2))
		elif choice=='2':
			print(num1,"-",num2,"=",substract(num1,num2))
		elif choice=='3':
			print(num1,"*",num2,"=",multiply(num1,num2))
		elif choice=='4':
			print(num1,"/",num2,"=",divide(num1,num2))
		break
	else:
		print('invalid input')

	
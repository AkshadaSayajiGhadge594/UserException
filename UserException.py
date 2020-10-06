print("-----Demonstration of User Defined Exception-----------");

class AgeInvalid(Exception):
	def __init__(self,value):
		self.value=value;

def main():
	try:
		age=int(input("Enter Your Age"));
		if(age<18):
			raise(AgeInvalid("Age is Invalid"));
	
	except AgeInvalid as error:
		print("A new Exception occured:",error.value);

if __name__=="__main__":
	main();

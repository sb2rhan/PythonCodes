from pip._vendor.colorama import init, Fore

def displayMessage(message, isWarning=False):
	if isWarning == True:
		print(Fore.RED + message)
	else:
		print(Fore.BLUE + message)
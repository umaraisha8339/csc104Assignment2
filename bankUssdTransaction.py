
def return_to_menu():
	ussd_code = eval(input('please type in your bank ussd code:'))
	Mainmenu()
print('Here is Zenith Bank ussd code s\nZenith: *966#')
def Mainmenu():
	print('1.Open account\n2.Get a card\n3.Register\n4.Check balance\n5.Airtime\n6.Transfer\n7.Self service\n8.Next')
	option = eval(input("please select an option:"))
	if option == 1:
		print('eaZybanking please select an option below:')
		if option2 ==1:
			account=eval(input('1.Open acc for self\n2.Open acc for 3rd part\n3.reate mobile wallet\n4.Uprade ZWallet to acc\n3.Next')
			print('Wrong pin')
			print("ENTER 1 TO RETURN TO MENU\nENTYER 2 TO END")
			top = eval(input(':'))
			if top == 1:
				Mainmenu()
			elif top == 2:
				exit()
			else:
			print('Wrong input')
	elif option == 2:
		Transfer = input('Enter the Account Number you want to transfer mony to:')
		amount = eval(input('Enter amount'))
		Account_pin = eval(input('Enter pin'))
		print('Are you sure you want to send',amount,'Naira to',Transfer,'\n1. YES\n2. NO')
		Assure_massage = eval(input(":"))
		if Assure_massage == 1:
			print('Transaction successifull')
			exit()
			print("ENTER 1 TO RETURN TO MENU\nENTYER 2 TO END")
			top = eval(input(':'))
			if top == 1:
				return_to_menu()
			elif top == 2:
				exit()
			else:
				print('Wrong input')
	elif option == 3:
		transfer = eval(input('1. For self\n2. For other'))
		if transfer == 1:
			amount = eval(input('Enter amount'))
			print('Transaction successifull')
		elif transfer == 2:
			amount = eval(input('Enter amount'))
			Phone_number = eval(input('enter number you want to Buy card for '))
			print('are you sure you want to buy',amount,'Naira worth to this number',Phone_number,'\n1. yes\n2. No')
			Airtime_Assure_massage = eval(input(':'))
			if Airtime_Assure_massage == 1:
				print('Transaction successifull')
				print("ENTER 1 TO RETURN TO MENU\nENTYER 2 TO END")
				top = eval(input(':'))
				if top == 1:
					Mainmenu()
				elif top == 2:
					exit()
				else:
					print('Wrong input')
	elif option == 4:
		print('An SMS massage will be send to you shortly')
ussd_code = eval(input('please type in your bank ussd code:'))
if ussd_code == 901:
	bank = "access"
	Mainmenu()
else:
	Mainmenu()																									
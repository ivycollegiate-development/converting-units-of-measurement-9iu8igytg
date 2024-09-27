def print_menu():
	print('1. Kilometers to Miles')
	print('2. Miles to Kilometers')




def km_miles():
	km = float (input('Please enter a distance in km: '))
	miles = km / 1.60934
	print('Distance in miles {0}'.format(miles))




def miles_km():
	miles = float (input('Please enter a distance in Miles: '))
	km = miles * 1.60934
	print('Distance in miles {0}'.format(km))




def c_to_f():
	C = float (input('Please enter a temperature value in c '))
	F = C * (9 / 5) + 32
	print('Tempature in f : {0}'.format(F))




def f_to_c():
	F = float (input('Please enter a temperature value in f '))
	C = (F - 32) * (9 / 5)
	print('Tempature in c : {0}'.format(C))


if __name__ == '__main__':
	print_menu()
	choice = input('Which would you like to do today?: ')
	if choice == '1':
		km_miles()
	if choice == '2':
		miles_km()
	if choice == '3':
		C_to_F()
	if choice == '4':
		F_to_C()

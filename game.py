number = 27
running = True
while running:
	guess = input('Enter the number ')
	if guess == number:
		print 'congatulations you guessed it'
		running = False
	elif guess < number:
		print 'Entered number is slightly lesser'
	else:
		print 'Entered number is slightly larger'


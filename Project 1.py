# Project - Traffic lights
current_colour=input('choose from option-Red, Yellow, Green.')
current_colour=current_colour.upper()
if current_colour=='RED':
    print("Stop until green")
elif current_colour=='YELLOW':
    print('Slow down')
elif current_colour=="Green":
    print("Go")
else:
    print("Please enter a valid light colour. Choose from option")
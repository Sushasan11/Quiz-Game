print('\t \t \t Welcome to the Game')
print(' ')
while True:
    
    user = input('What is the name of the toy cowboy in Toy Story?: ').capitalize()
    if user == 'Woody':
        print('Correct')
    else:
        print('Incorrect')
            
    user = input('What is the color of an emerald?: ').capitalize()
    if user == 'Green':
        print('Correct')
    else:
        print('Incorrect')
                
    user = input('What do caterpillars turn into?: ').capitalize()
    if user == 'Butterfiles':
        print('Correct')
    else:
        print('Incorrect')
                    
    user = input('What do you use to write on a blackboard?: ').capitalize()
    if user == 'Chalk':
        print('Correct')
    else:
        print('Incorrect')
                        
    user = input('What do bees make?: ').capitalize()
    if user == 'Honey':
        print('Correct')
    else:
        print('Incorrect')
    
    play_again = input('Do you want to play again?(y/n): ').lower()
    if play_again != 'y':
        print('Thanks for playing')
        break
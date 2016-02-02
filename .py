def deck_contents(deckname):
    #This function makes MTG deck lists into Dictionaries
    
    deck_content = {}
   
    import csv
   
    with open(deckname, 'r') as f:
        reader = csv.reader(f)
        #this makes it so the file doesn't read commas or spaces

        next(reader)
        #this skips the header row in the file .csv file
     
        for row in reader:
            deck_content[row[1]] = int(row[0])
            #deckbox.org files contain columns: quantity, name, other stuff...
            #we want the keys to be the card name aka row 1, card quantity is in row 0.
            #Maybe in the future I'll figure out how to make use of the other columns.

            #The program crashes unless you delete the last few blank rows in the 
            #.deckbox file.  I don't know why this happens.
            #Go into each .csv file and delete the last few rows to fix this issue.
         
    return deck_content


def holiday_box():
    #This function prints a list of decks based off the user's choice

    deck_list = {}
    print('\n+-------------------------------------------+\n|       MTG Decks in the Holiday Box        |\n+-------------------------------------------+')

    import glob
    
    for files in glob.glob("*.csv"):
    #This finds all .csv files in the folder local to the holiday_box program.

        if 'Inventory' in files:
            invintory = deck_contents(files)
         
        elif 'Wishlist' in files:
            wishlist = deck_contents(files)
            #The wishlist is all cards that you need to complete your decks that you don't
            #currently own.  A deck won't work if all cards aren't in the invintory and for
            #some reason using the invintory + wishlist doesn't work in this program later on,
            #it currently has to be done manually by pasting the wishlist into the invintory.

        else:
            print(' - %s' % (files[:len(files)-4]))
            deck_list[files[:len(files)-4]] = deck_contents(files)
         
    while True != False:
        user_choice = input("""\nChose a deck, Or type 'decks in box','deck contents' or 'done': """)
        play_list = []
        
        for key in deck_list.keys():
            play_list.append(key)
           
        if user_choice in deck_list.keys():
            play_list.remove(user_choice)
            
            for deck in deck_list.keys():
                if deck != user_choice:
                    for card in deck_list[user_choice]:
                        if deck_list[deck].__contains__(card) and deck_list[user_choice][card] + deck_list[deck][card] >= invintory[card]:
                            play_list.remove(deck)
                            break
                            #If break is removed it will show all cards in that deck that make it non-playable.
                            #This is annoying if the only card that is similar between the two decks is the one wooded foothills
                            #that is in your invintory, when you could just swap it out for a scalding tarn.
                            #Maybe make an option that lets you input two deck names and it lists all cards that conflict?

                            #It's also annoying to have to type the full deck name out if its got a lot of "_"s and dates and such.
                
            print('\n+-------------------------------------------+\n|    Remaining decks that can be played:    |\n+-------------------------------------------+')
            
            for deck in play_list:
                print (' - %s' % (deck))

        elif user_choice.lower() == 'decks in box':
            print('\n+-------------------------------------------+\n|       MTG Decks in the Holiday Box        |\n+-------------------------------------------+')
            
            for deck in deck_list.keys():
                print (' - %s' % (deck))

        elif user_choice.lower() == 'deck contents':
            user_choice = input('Which deck would you like to see the contents of?: ')

            if user_choice in deck_list.keys():
                print('\n\nDeck: %s' %(user_choice))
                
                for card in deck_list[user_choice]:
                    print(' - %s : %i' % (card, deck_list[user_choice][card]))

            else:
                print("""\nThat's not a deck in the box.""")

        elif user_choice.lower() == 'done':
            break
        
        else:
            print("""\nThat's not a deck in the box. Type the full deck name: """)


holiday_box()

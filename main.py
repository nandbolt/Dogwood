# Alexander Wilson, 9-4

# Bookkeeping
ending_count = '9'

# Init message
print()
print('*Starting adventure*')
print()

# User
user_input = ''
dog_name = input('What is a good dog name?\n')

# Title
print()
print('*******')
print('Dogwood')
print('*******')
print()

# Forest
print('*Forest*')
print('You awaken in a dense, dimly lit forest. You do not know how you got here,')
print('or why you are a dog. The breeze is soft, carrying a faint, smokey smell.')
print('Your stomache groans.')

# Forest choices
first_choice = '- follow the smokey smell'
second_choice = '- bark'

# Forest prompt
print()
print(first_choice)
print(second_choice)
print()
user_input = input()
print()

# If first choice
if (('follow' in user_input) or ('smoke' in user_input) or ('smell' in user_input)):
    # Clearing
    print('*Clearing*')
    print('You decide to ',user_input,', leading you out of the forest and',sep='')
    print('into a wide, grassy field. A humming river flows steadily to your left,')
    print('but you notice the smoke trail leads further ahead.')

    # Clearing choices
    first_choice = '- follow the smoke trail'
    second_choice = '- head to the river'

    # Clearing prompt
    print()
    print(first_choice)
    print(second_choice)
    print()
    user_input = input()
    print()

    # If first choice
    if (('follow' in user_input) or ('smoke' in user_input) or ('trail' in user_input)):
        # Burning house
        print('*Burning house*')
        print('As you ',user_input,', you reach an isolated house set ablaze, hissing in the',sep='')
        print('gentle breeze. There seems to be noone around to put out the flames.')

        # Burning house choices
        first_choice = '- rush into the burning house'
        second_choice = '- go back to the river'

        # Burning house prompt
        print()
        print(first_choice)
        print(second_choice)
        print()
        user_input = input()
        print()

        # If first choice
        if (('rush' in user_input) or ('burning' in user_input) or ('house' in user_input)):
            # True ending
            print('The fire rumbles as you ',user_input,'. Running through dense smoke',sep='')
            print('and dodging falling embers, you encounter a human lying on the ground among')
            print('the chaos. Slowly, your vision starts to fade until it is completely black.')
            print()
            print('You slowly start to open your eyes, vision blurry. You feel a pull on your')
            print('collar, as if you are being dragged by the neck by something, someone. As')
            print('your lungs clear of smoke and vision clears, you see a burning house. The')
            print('pulling on your neck ceases as you lay on the grass. As you lay there, you feel')
            print('something cold and wet on the back of your neck.')
            print()
            print(dog_name,', your dog, is vivaciously licking you as you lay there.',sep='')
            print('You reach out and give him a big, strong hug as he licks you with joy.')
            print()
            print('(Ending 1 of ',ending_count,')',sep='')
            print('TRUE ENDING')
        # Else second choice
        else:
            # Fisherman ending
            print('The roaring flames wane as you ',user_input,'. You encounter a fisherman near',sep='')
            print('the shore and try to lead him back to the burning house, barking with all your might.')
            print('Once he sees the house, he immediately runs toward the nearby town.')
            print()
            print('The flames are resilient, but are no match for the dozens of townsfolk armed with')
            print('gallons of water. As the flames subside, the fisherman takes a liking to you, your wit')
            print('and spirit, and welcomes you into his family and names you Sal.')
            print()
            print('You spend your days on the riverside with your new family, occasionally going on')
            print('fishing trips and eating mostly fish. You feel at home.')
            print()
            print('(Ending 2 of ',ending_count,')',sep='')
    else:
        # River house
        print('*House on the River*')
        print('You ',user_input,', reaching a quiet, quaint house along the sandy shores.',sep='')
        print('The door is slightly open, eminating a savory smell. Several cats roam nearby,')
        print('staring you down. Besides the cats, noone seems to be home.')

        # River house choices
        first_choice = '- follow the savory smell into the house'
        second_choice = '- chase the cats'

        # River house prompt
        print()
        print(first_choice)
        print(second_choice)
        print()
        user_input = input()
        print()

        # If first choice
        if (('follow' in user_input) or ('smell' in user_input) or ('house' in user_input)):
            # Stray ending
            print('You ',user_input,', nose guiding the way. Up on the',sep='')
            print('dinner table lays a cooked, steaming duck, causing saliva to pour out of')
            print('your mouth. Driven by hunger, you chow down on the cooked duck, savoring each bite.')
            print('Suddenly, you here a loud shout behind you. The man orders you out of his house.')
            print('You stuff as much duck in your mouth as you can before you leave.')
            print()
            print('Stubbles is what they call you. You wander, searching for what can sustain you.')
            print('It can be sad at times, but you do all that you can to make it through each night.')
            print()
            print('(Ending 3 of ',ending_count,')',sep='')
        # Else second choice
        else:
            # Cat society ending
            print('As you ',user_input,', they lead you to an underground cave filled with',sep='')
            print('layers of cats, eyeing you with distaste. Knowing you are unwelcomed, you bow')
            print('your head. The cats are stunned, noting your respect for them. The queen cat,')
            print('laying on her throne, meows.')
            print()
            print('The cat society welcomes you as a member and makes you an honorary feline.')
            print('Life is much simpler as you work within the guild to help all the cats,')
            print('taking your slice of the pie whenever plenty.')
            print()
            print('(Ending 4 of ',ending_count,')',sep='')
else:
    # Knight event
    print('As you ',user_input,', a black knight appears before you in the woods.',sep='')
    print('They request that you stop barking, but recognize that you are lost and insist')
    print('that you follow them into town.')

    # Clearing choices
    first_choice = '- follow the knight'
    second_choice = '- bark'

    # Clearing prompt
    print()
    print(first_choice)
    print(second_choice)
    print()
    user_input = input()
    print()

    # If first choice
    if (('follow' in user_input) or ('knight' in user_input)):
        # Town
        print('*Town*')
        print('Choosing to ',user_input,', you reach a bustling town with hundreds',sep='')
        print('of humans flowing through the streets, rushing in and out of buildings. The knight')
        print('bids you farewell, insisting you not to cause any trouble.')
        print()
        print('To your right, there is a library that isn\'t all to busy. To your left, a sign')
        print('directs you to a nearby market. Many people seem to be heading there.')

        # Town choices
        first_choice = '- travel to the market'
        second_choice = '- enter the library'
        third_choice = '- cause trouble'

        # Town prompt
        print()
        print(first_choice)
        print(second_choice)
        print(third_choice)
        print()
        user_input = input()
        print()

        # Use AND and ELIF
        # If third choice and sure of it
        if ((('cause' in user_input) or ('trouble' in user_input)) and ('yes' in input('Are you sure?\n\n- yes\n- no\n\n'))):
            # Criminal dog ending
            print()
            print('Trouble brews as you cause much of it throughout the town. The knight hears of this and sends his')
            print('dissapointment. The townsfolk become annoyed of your troublemaking and tries to run you out of town,')
            print('but you end up escaping with a gleeful smirk on your snout.')
            print()
            print('Soon you are known as Diggs the Mischevous, stirring up trouble whereever you set your paws.')
            print('You run an underground operation that causes mischief, living forever in the shadows.')
            print()
            print('(Ending 7 of ',ending_count,')',sep='')
        # Elif first choice
        elif (('travel' in user_input) or ('market' in user_input)):
            # Merchant ending
            print('*Market*')
            print('The market breathes energy as people move to and from various stands. Noticing an empty stand,')
            print('you decide to set up shop and sell the only thing you have available: dog barks. At such a cheap')
            print('rate, people can\'t help but buy as many dog barks as they can afford.')
            print()
            print('You soon acquire enough money to upgrade your measly stand into a full-fledged business. People')
            print('come from all places to place orders on Atlas\'s barks. You earn enough to retire early, settling for')
            print('a place on the outskirts of town.')
            print()
            print('(Ending 5 of ',ending_count,')',sep='')
        # Else third choice
        else:
            # Academic ending
            print('*Library*')
            print('The library bleeds with information, books at the ready to be disected and dissolved into')
            print('the brain. A fellow respected scientist catches glimpse of your studious and persistent')
            print('efforts, adopting you into their research efforts.')
            print()
            print('As a scientific researcher, you, Dr. Bubbles, help the town advance their technologies and')
            print('become known for your intelligence and progress in water sciences.')
            print()
            print('(Ending 6 of ',ending_count,')',sep='')
    else:
        # Knight ultimatum
        print('You ',user_input,'. The knight recognizes your strength and resilience,',sep='')
        print('and respects your honesty and bravery. However, he insists that you accompany them.')
        print('They note that the town isn\'t too far away.')

        # Knight ultimatum choices
        first_choice = '- follow the insistent knight'
        second_choice = '- bark'

        # Knight ultimatum prompt
        print()
        print(first_choice)
        print(second_choice)
        print()
        user_input = input()
        print()

        # If first choice
        if (('follow' in user_input) or ('knight' in user_input)):
            # Knight ending
            print('You ',user_input,' to town. Along the journey the knight recognizes your',sep='')
            print('resilience and recommends you to the king to join the royal guard of knights.')
            print('The king is impressed with your demeanor, enlisting you into the guard immediately.')
            print()
            print('As Sir Beagleton, you spend your days protecting the town from foreign threats. The other knights')
            print('have accepted you as kin, and the townsfolk feel at peace under your watch.')
            print()
            print('(Ending 8 of ',ending_count,')',sep='')
        # Else second choice
        else:
            # Royalty ending
            print('As you ',user_input,' and ', user_input,', the knight can only stand and admire',sep='')
            print('your wit, bravery, persistence and tenacity to keep barking. They leave and bring')
            print('crowds of townsfolk to sit back and watch in amazement as you continue to bark.')
            print()
            print('The townsfolk idolize you, overthrowing the current monarch and crowning you the')
            print('new king. Going by King Barklogan, you live as the new ruler of this small town,')
            print('barking orders to your subordinates for all of your rule.')
            print()
            print('(Ending 9 of ',ending_count,')',sep='')

# Quit prompt
print()
print('********************')
print('Press enter to quit.')
print('********************')
input()

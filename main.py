def game():
    from game_data import data
    import random
    import os
    from art import logo
    score = 0
    running = True


    while running:
        print(logo)
        if score > 0:
            print(f"Your Current score is {score}.\n")
        else:
            # print("Welcome to insta quiz by Hritik Gehlot.\n")
            print("𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓲𝓷𝓼𝓽𝓪 𝓺𝓾𝓲𝔃 𝓫𝔂 𝓗𝓻𝓲𝓽𝓲𝓴 𝓖𝓮𝓱𝓵𝓸𝓽.\n")
    
        compare1 = data[random.randint(0, len(data)-1)]      #It will give dict whose keys are ['name', 'follower_count', 'description', 'country']
        # print(compare1.keys())
        compare2 = data[random.randint(0, len(data)-1)]
        if compare1 == compare2:
            continue
        print(f"Compare A: {compare1['name']}, {compare1['description']}, {compare1['country']}")
        print("\tVS")
        print(f"Compare B: {compare2['name']}, {compare2['description']}, {compare2['country']}\n")
        try:
            user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
            
            if user_input == "a":
                if compare1["follower_count"] > compare2["follower_count"]:
                    score += 1
                    os.system("cls")
                else:
                    running=False
                    print(f"\n\nYou loose. {compare1['name']} have {compare1['follower_count']}M followers and {compare2['name']} have {compare2['follower_count']}M followers")                   
    

            if user_input == "b":
                if compare1["follower_count"] < compare2["follower_count"]:
                    score += 1
                    os.system("cls")

                else:
                    running=False 
                    print(f"\n\nYou loose. {compare1['name']} have {compare1['follower_count']}M followers and {compare2['name']} have {compare2['follower_count']}M followers")                   
        except:
            print("Please enter either 'A' or 'B'")            
    

    if running == False:
        again = input("Do you want to play again? Type 'y' or hit enter : ").lower()
        if again == "y":
            game()

game()            



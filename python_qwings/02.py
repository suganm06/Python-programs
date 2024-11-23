# name = input("What is your name? ")
# print("Hello " + name + ", nice meeting you. I am Sugan!")

# time = input("Could you please tell me the time? ")
# print("thanks for letting me know")

# hobby = input("What are your hobbies? ")
# print(hobby + " sounds fun! I also enjoy these hobbies.")

# favorite_food = input("What's your favorite food? ")
# print("Yum! " + favorite_food + " sounds delicious. I could eat that any day!")

# favorite_sport = input("What's your favorite sport? ")
# print(favorite_sport + " is a great sport! I play it sometimes with my friends too.")

# music = input("What kind of music do you enjoy? ")
# print("Cool! I like listening to " + music + " music when I need to relax.")

# movie = input("What's your favorite movie or TV show? ")
# print("It is a great choice! I could watch " + movie +  " over and over.")

# book = input("Do you enjoy reading? What's your favorite book? ")
# print("Wow, " + book + " sounds interesting. I’ll add it to my reading list!")

# game = input("Do you play video games? What's your favorite game? ")
# print(game + " is a fantastic game! I love playing that too.")

# print("It was great chatting with you, " + name + "! Let's catch up again sometime.")

name = input("What is your name? ")
print("Hello " + name + ", nice meeting you. I am Sugan!")

hobby = input("What are your hobbies? ")
print(hobby + " sounds fun! I also enjoy these hobbies.")

favorite_sport = input("What's your favorite sport? ")
print(favorite_sport + " is a great sport! I play it sometimes with my friends too.")

if favorite_sport.lower() == "cricket":
    ipl = input("Do you like watching IPL? (yes/no) ")
    if ipl.lower() == "yes":
        print("Great! IPL is so much fun!")
    else:
        print("I understand, it's not for everyone.")
elif favorite_sport.lower() == "badminton":
    print("Badminton is such a fast and thrilling game!")
else:
    print(favorite_sport + " is fun to play!")

movie = input("What's your favorite movie or TV show? ")
print(movie + " is a great choice! I could watch " + movie + " over and over.")

if movie.lower() == "inception":
    print("Inception really makes you think!")
elif movie.lower() == "friends":
    print("Friends is such a fun show, I can watch it anytime!")
else:
    print(movie + " sounds interesting!")

game = input("Do you play video games? What's your favorite game? ")
print(game + " is a fantastic game! I love playing that too.")

if game.lower() == "minecraft":
    print("Minecraft is so creative!")
elif game.lower() == "valorant":
    print("valorant is full of action, especially with friends!")
else:
    print(game + " sounds exciting!")

print("It was great chatting with you, " + name + "! Let's catch up again sometime.")
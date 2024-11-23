# Q1)
print("Q1)")
print(
    "In Python, you can comment multiple lines using either [#] at the beginning of each line or by using a triple-quotes. Shortcut key in VS code [Ctrl + ?].\n"
)

# Q2)
print("Q2)")
a = 5
b = 13
c = 10

print("(a+b+c):", a + b + c)
print("(a*b*c):", a * b * c)
print("(a-4*b+c):", a - 4 * b + c)
print("\n")

# Q3)
print("Q3)")
p = int(input("Enter value for p: "))
q = int(input("Enter value for q: "))
r = int(input("Enter value for r: "))

result = 5 * p - 8 * q - 12 * r
print("Result of 5*p - 8*q - 12*r is:", result)
print("\n")

# Q4)
print("Q4)")
name = input("What is your name? ")
print("Hello " + name + ", nice to meet you!")
print("\n")

# Q5)
print("Q5)")
a = -12
if a % 2 == 0:
    print(a," is an even number.")
else:
    print(a," is an odd number.")
print("\n")

# Q6)
print("Q6)")
fever = input("Do you have a fever? (yes/no): ").strip().lower()
if fever == "yes":
    print("You should consult a doctor.")
else:
    print("Take some rest.")
print("\n")

# Q7)
print("Q7)")
for i in range(-25, 51):
    print(i)
print("\n")

# Q8)
print("Q8)")
i = 1
while i <= 10:
    print("0.25 * " , i , "=" , (0.25 * i))
    i += 1
print("\n")

# Q9)
print("Q9)")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    if age >= 65:
        print("You are also eligible for senior citizen benefits.")
    else:
        print("You are not eligible for senior citizen benefits yet.")
else:
    print("You are not eligible to vote.")
print("\n")

# Q10)
print("Q10)")
name = input("Hey there! I'm Sugan. What's your name? ")
print("Nice to meet you, " + name + "! I'm always up for a good chat. Let's dive in!\n")

hobby = input("What's something you enjoy doing when you have free time? ")
if "reading" in hobby.lower():
    print("Reading is fantastic!\n")
elif "travel" in hobby.lower():
    print("Traveling is amazing! gives peace of mind.\n")
else:
    print(hobby + " sounds really fun! I'd love to try it sometime.\n")

favorite_sport = input("What's your favorite sport? ")
if favorite_sport.lower() == "cricket":
    print("Ah, cricket! Nothing like a good match. Are you a fan of T20 or Test cricket?")
    cricket_type = input("T20 or Test? ")
    if "t20" in cricket_type.lower():
        print("T20s are so action-packed! Never a dull moment.\n")
    else:
        print("Test cricket has its own unique charm, like a long, strategic battle.\n")
elif favorite_sport.lower() == "badminton":
    print("Badminton is so fast-paced!\n")
elif favorite_sport.lower() == "soccer":
    print("Soccer is a worldwide favorite!\n")
else:
    print(favorite_sport + " sounds cool! I should learn more about it.\n")

movie = input("What's a movie or TV show that really resonates with you? ")
if "inception" in movie.lower():
    print("Inception is a brain-bender! It’s fun to think about what reality means after watching it.\n")
elif "friends" in movie.lower():
    print("Friends is timeless! It's like comfort food for the soul.\n")
elif "marvel" in movie.lower():
    print("The Marvel Universe! So many heroes, so many stories.\n")
else:
    print(movie + "? That’s a great pick! I’ll add it to my list of must-watch shows or movies.\n")

game = input("What's a game you love? ")
if "minecraft" in game.lower():
    print("Minecraft is so versatile!\n")
elif "valorant" in game.lower():
    print("Valorant is all about precision and tactics!\n")
elif "fifa" in game.lower():
    print("FIFA is a classic!\n")
else:
    print(game + " sounds interesting! I’ll definitely look into it.\n")

print("This was fun, " + name + "! I learned a lot about you. Let’s chat again sometime soon!")

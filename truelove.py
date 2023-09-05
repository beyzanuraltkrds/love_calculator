print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your date name? \n")

combined_names = (name1 + name2).lower()

true_count = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")
love_count = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

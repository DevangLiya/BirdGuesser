# actual game

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def plot_bird(bird_list):
	'''
	Clear the plot and display a single bird. Print the name of the bird after the plot is closed.
	'''
	plt.cla()
	plt.clf()

	current_bird = bird_list.sample()
	filepath = current_bird['filepath'].item()
	label = current_bird['label'].item()

	image = mpimg.imread(filepath)
	plt.imshow(image)
	plt.axis('off')
	plt.show()

	print(f"Correct ID: {label}")

	return 0

# cute welcome screen
plt.text(0.08, 0.55, "Welcome to BirdGuesser!", fontsize=30)
plt.text(0.35, 0.45, "(birbs for u bb)", fontsize=20)
plt.axis('off')
plt.tight_layout()
plt.show()

# clear the terminal window
os.system('clear')

# select game mode and load appropriate list
game_mode = int(input("Please select game mode: Easy - 0, Hard - 1 "))
if game_mode == 0:
	game_mode = 'easy'
	print(f"Playing on easy mode? We all need a bit of encouragement. All the best!")
	bird_list = pd.read_csv('easy.csv', names=['filepath', 'label'])
	bird_list['label'] = bird_list['label']
else:
	game_mode = 'hard'
	print(f"Woah, look at you feeling adventerous today, playing on hard mode. All the best!")
	bird_list = pd.read_csv('hard.csv', names=['filepath', 'label'])
	bird_list['label'] = bird_list['label']

# actual game
score = 0
n_round = 0
while True:
	print("==========")
	n_round = n_round + 1
	print(f"Get read for round {n_round}")

	plot_bird(bird_list)

	right = input("Did you get that right? [0/1] ")
	score = score + int(right)
	print(f"Your current score is {score}/{n_round}")
	another = input("Press any key to continue, 'Q' to quit ").lower()
	if another == 'q': break

# cute end screen
print("==================================")
print(f"Your final score is {score}/{n_round}")
print("Thanks for playing 🐦")
print("==================================")
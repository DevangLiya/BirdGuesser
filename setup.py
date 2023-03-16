#Setup for bird guesser. Run only once after downloading

import requests
from bs4 import BeautifulSoup
import os
from tqdm import tqdm

# Function to download image from URL
def download_image(url, fn):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			with open(fn, 'wb') as f:
				f.write(response.content)
	except Exception as e:
		print(f"Error downloading {url}: {str(e)}")

def download_list(bird_list, num_images, list_name):
	# paths to all the birds will be saved in a file
	# columns: path, bird name
	out_csv = open(f'{list_name}.csv', 'w') 

	for query in tqdm(bird_list):
		# Send GET request to Google search page
		url = f"https://www.google.com/search?q={query}&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwiOvNn48ZzzAhXEyDgGHUjMDZMQsAQIHg&biw=1920&bih=937"
		response = requests.get(url)

		# Parse HTML response using BeautifulSoup
		soup = BeautifulSoup(response.content, 'html.parser')

		# Extract image URLs using BeautifulSoup selectors
		image_tags = soup.find_all('img', {'class': 'yWs4tf'})
		image_urls = [tag['src'] for tag in image_tags]

		# Download images to local directory
		directory = f'{list_name}/{query}'

		# breakpoint()
		if not os.path.exists(directory):
			os.mkdir(directory)

		for i, url in enumerate(image_urls[:num_images]):
			download_image(url, f'{directory}/{query}{i}')
			# print(f"Downloaded image {i+1}/{num_images} for {query}")
			out_csv.write(f'{directory}/{query}{i},{query}\n')

	out_csv.close()

	return 0

num_images = 5 # number of images per bird

# download easy birds
with open('easybirds', 'r') as fh:
	easybirds = fh.read().splitlines()
if not os.path.exists('easy'):
	os.mkdir('easy')
print('Downloading easy birds')
download_list(easybirds, num_images, 'easy')

# download hard birds
with open('hardbirds', 'r') as fh:
	hardbirds = fh.read().splitlines()
if not os.path.exists('hard'):
	os.mkdir('hard')
print('Downloading hard birds')
download_list(hardbirds, num_images, 'hard')

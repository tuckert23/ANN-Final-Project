import requests as rq
import urllib.request

# Dictionaries and so the number of repositories you can pull from is expandable
# i.e. you could include raribles or decentraland
names = ["cryptopunks"]
names_lens = {"cryptopunks": 9999}

# URL for OpenSea API
url = "https://api.opensea.io/api/v1/assets"


def download_images(collection_name, start_at=0):
	
	# Receives the number of images from the dictionary
	num_images = names_lens[collection_name]
	print("Saving images from", collection_name)
	print("%i images to be collected" % num_images)
	
	"""
	This loop collects one image at a time. While it is possible (and faster) to collect in batches,
	it is often cumbersome and not as reusable as the cap for batch size is 30 images.
	"""
	for i in range(start_at, num_images):
		# Setting the parameters for the GET request
		params = {"collection": collection_name, "token_ids": [i],}
		
		# Requesting from API and receiving in JSON format
		response = rq.get(url, params=params).json()
		
		# Sometimes the response is bad, if so simply keep going
		if response['assets'] != []:
			
			# Extracting only the image urls for this request
			link = response['assets'][0]["image_url"]
			
			# Every 10 images downloaded, give a status update
			if i % 10 == 0:
				print("\tRequest %i:" % i, link)
			
			# Vaving each image from their urls by their token-ID
			urllib.request.urlretrieve(link, "./" + collection_name + "/" + str(i) + ".png")
			
		else:
			print("Response %i empty" % i)
			continue


if __name__ == '__main__':
	# Calling the function
	# start_at parameter is helpful if the code stops at some point so you
	# don't have to restart from the beginning
	download_images("cryptopunks")

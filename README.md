# Artificial Neural Networks and Deep Learning
## Final Project  
Artificial Neural Networks and Deep Learning  
DIS Copenhagen  
December 6, 2021  
Lucian Leahu and Daniel Svendsen  

## Contributors:
Dean Wahle, Ethan Sidelsky, and Taylor Tucker

## Research Question:
Can a computer generate a valuable NFT based on the designs of popular ones?

## [Link to Medium Blog Post](https://medium.com/@tuckert23/ai-crypto-art-generating-nft-style-images-with-neural-networks-68b0930ec1bd)


## Description of Notebooks
- __download_data.py__  
`download_data.py` is a simple script used to download images from any collection on the OpenSea API. All the user needs is to know the collection name, which is easily found via the collections URL on OpenSea, and the number of images the collection holds, which is also easily found on the home screen of the collection page. This script assumes the token IDs for each image to be `[0, num_images-]`.

- __CryptoPunk GAN.ipynb__  
The CryptoPunk GAN is a notebook containing all of the code required to run a GAN on the CryptoPunk dataset. This dataset can either be pulled using `download_data.py`, or throught the included `cryptopunks.zip` folder, which contains all of the needed CryptoPunk assest. When running this notebook, be sure the `num_epochs` parameter is closer to 50, which equates to 30-45 minutes of runtime on modern laptops. At the end, you will be left with a GIF of the model's progression from noise to CryptoPunk-style images. 

- __ANNCycleGAN.ipynb__  
This notebook contains all the code required to run a CycleGAN for style-transfer so long as you have the CryptoPunks dataset, which can either be pulled using `download_data.py`, or throught the included `cryptopunks.zip` folder, which contains all of the needed CryptoPunk assests. This code does take a long time to run, so be sure that the `epochs` parameter in the training code block is less than 10. The CycleGAN uses the CryptoPunk Dataset as a style guide, while learning to morph the faces from the facial dataset into that style. While the results aren't perfect, see if you can notice any odd similarities between the people and the generated CryptoPunks (i.e. hair color, facial shape, facial features, etc.). 


## Package requirements
- numpy
- pandas
- matplotlib.pyplot
- os
- tensorflow
- keras
- time
- IPython.display
- tensorflow_docs.vis.embed
- glob
- imageio
- tensorflow_addons
- tensorflow_datasets

# Bot Ross
by [Andrew Barlow](https://github.com/dandrewbarlow)

## Description
A project to create a neural network that creates Bob Ross paintings

## Implementation
I'm going to use a generative adversarial network to create this. This is my first foray into deep learning, and this is an educational exercise for me, so take everything you see with a grain of salt. I'm going to use Keras + Tensorflow due to their respective reputation and status in the deep learning field.

* `download.py` - Downloads all the Bob Ross paintings to use
* `train.py` - Train the model
* `generate.py` - Use the model to generate new images
* `Makefile` - shortcuts for running, downloading dependencies, etc.
* `requirements.txt` - contains dependencies
## GoScanner

# Purpose:
When playing Go on a physical board, it can be a pain to record the game to learn from later. 
Particularly, the .sgf tree format provides an easy way to view, send and make hypothetical changes to a 
completed game. This project converts webcam pictures of a game into a digital reprentation of each turn, 
then convertes those states into a .sgf file.


# Technical Summary:
This project takes an image of a Go board as input and outputs a matrix representation of the game's state.


The edges of the Go board are detected in the inputted image, which is then transformed to a square, top-down perspective.
The image is then segmented by each square, then fed into a Convolutional Neural Network (CNN) trained to classify each 
sub-image as containing a white piece, black piece or no piece. The classification for each position is stored in an array, 
and the array representation is converted to a .sgf representation. This is then written and can be viewed by most types of Go 
software.

# Planned additions
Taking multiple game states and ordering them into a tree structure.

Cleaning up the pipeline into a user-friendly api that can be accessed by a frontend 

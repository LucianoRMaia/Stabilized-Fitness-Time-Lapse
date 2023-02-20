# Stabilized-Fitness-Time-Lapse
This repo contains the python code for taking pictures of a person in the same position everytime. 
This solves the problem of fitness progress recording, where each photo is taken in slightly different positions, thus generating a shaky time-lapse. Here we're using Google's Mediapipe in order to get the pose of the person, and then assuring that every picture is taken using the same pose, producing a much smoother final result. 
This code may also be used for aging time-lapse, hair growth time-lapse, or virtually any kind of time-lapse where the main subject is a human.

##TODO:
- Save result images in a separate directory with unique names, considering the date and time they were taken, maybe add the weight of the person in the name of the file, so that we can create a graph of weight gain/loss with the time lapse.
- Plot the original image with an alpha over the current image, so that it's easier to align the body, specially for cases where mediapipe doesn't make clear distinctions (like orientation of hands).
- Before saving the current image, show original image and current image blinking in the same window, so that the user can confirm they are indeed stabilized.
- Create a compiler for the time lapse photos.


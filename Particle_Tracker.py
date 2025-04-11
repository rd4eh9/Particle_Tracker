#Steps:
#import images into array --> parse from video
#identify particles
#find center of particle
#track change in xyz for each particle over time

import cv2

#import images into array
# Load the image
image = cv2.imread('path/to/image.jpg')
# Display the image (optional)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image_array = np.array(image)
 # how to access elements BGR blue = image[50, 100, 0]


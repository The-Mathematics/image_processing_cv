import cv2

image1 = cv2.imread("image1.jpeg")
#This code line creates a variable image1 and assigns the value "image.jpeg" to it

cv2.imshow("Normal Image1", image1)
#This code line displays the image with a new name "Normal Image"

cv2.imshow("image1.jpeg", image1)
#This code line displays the original image

image1Gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image1", image1Gray)
#This code line converts the image1 to grayscale and assigns it to a new variable image1Gray
#This code line displays the greyed image with the name "Gray Image1"

image1Blur = cv2.GaussianBlur(image1, (13,13), 0)
cv2.imshow("Blurred Image1", image1Blur)
#This code line blurs the image using the gaussian blur technique,it requires that you provide the ksize and sigmaX and sigmaY - if sigmaY is not provided,it will assume the same value as sigmaX - if both values are 0,they will be calculated from the kernel size
#This line displays the blurred image with the name "Blurred Image1"

image1Canny = cv2.Canny(image1, 150, 200)
cv2.imshow("Edges Image1", image1Canny)
#This code line converts the image1 to a tresh image to reveal its edges and assigns it to a new variable image1Canny
#This code line displays the treshed image with the name "Edges Image1"

print("Original Dimension:", image1.shape)
image1Resize = cv2.resize(image1, [200,200])
cv2.imshow("Resized Image1", image1Resize)
print("Resized Dimension:", image1Resize.shape)
#This code line prints out the dimensions for the original image stored in the variable image1
#This code line resizes the image1 to a dsize [200,200] and assigns it to a new variable image1Resize
#This code line displays the resized image with the name "Resized Image1"
#This code line prints out the dimensions for the resized image stored in image1Resize


cv2.imwrite("Gray Image1.jpeg", image1Gray)
cv2.imwrite("Edges Image1.jpeg", image1Canny)
cv2.imwrite("Resized Image1.jpeg", image1Resize)
cv2.imwrite("Blurred Image1.jpeg", image1Blur)
cv2.waitKey(0)
#This code line saves the greyed image as "Gray Image1"
#This code line saves the Treshed image as "Edges Image1"
#This code line saves the Resized image as "Resized Image1"
#This code line saves the Blurred image as "Blurred Image1"
#This code line sets the delay for the code to run


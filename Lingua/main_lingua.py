import cv2
import pytesseract
from speaker import speak

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # Remember to check that this is your tesseract path!

# Capturing camera feed and when q is pressed the feed at that moment is used 
cap = cv2.VideoCapture(0)
text_shown = False

while True:
    _, img = cap.read()

    # Show what the camera is capturing
    cv2.imshow("Lingua", img)
    
    k = cv2.waitKey(5) & 0xFF  # We are just using the least signficant byte
    if k == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()

# Function to process the image (from BGR to a gray scale)
def process_img(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    _, res = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return res

# Process the captured image
img = process_img(img)

# Extract text data from our image
data = pytesseract.image_to_data(img, lang='eng', config='--psm 6')
sentence = []
for x, y in enumerate(data.splitlines()):  # Divide the detected text in lines (our words)
    if x != 0:
        y = y.split()
        if len(y) == 12: # If its len it's 12, Tesseract it's detecting it as a word
            word = y[11] # Tesseract saves the string word in the 11th column
            sentence.append(word)


# Function to convert a list to a string
def l_to_s(list):
    str = ""
    for c in list:
        str += c + " "
    return str

# Convert the list of words to a single string and read it
text_to_speak = l_to_s(sentence)
speak(text_to_speak)

print(text_to_speak) # Print it in the terminal (you can comment this line if you won't use it)

# Clean up
cv2.waitKey(0)
cv2.destroyAllWindows()


                
    
        
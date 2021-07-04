import cv2

def choosefile(location):
        global file
        file = cv2.imread(location,1)
        
def convert(width,height):
        global resized_file
        resized_file = cv2.resize(file,(width,height))
        
def save(name):
    cv2.imwrite(name, resized_file )

def dimention():
    return 'dimention of selected image is '+ str(file.shape[1])+'x'+str(file.shape[0])

        


"""
gray_file = cv2.cvtColor(file,cv2.COLOR_BGR2GRAY)
resized_file = cv2.resize(gray_file,(int(file.shape[1]/2),int(file.shape[0]/2)))
cv2.imshow('galaxy',resized_file)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
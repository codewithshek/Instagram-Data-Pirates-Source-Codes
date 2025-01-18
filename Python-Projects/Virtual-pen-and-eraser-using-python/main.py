import cv2
import numpy as np
class drawingCanvas():
    def __init__(self):
      self.penrange = np.load('penrange.npy') 
# load HSV range
      self.cap = cv2.VideoCapture(0)         
 #0 means primary camera .
      self.canvas = None                      
#initialize blank canvas
        #initial position on pen 
      self.x1,self.y1=0,0
        # val is used to toggle between pen and eraser mode
      self.val=1
      self.draw()                            
#Finally call the draw function

    def draw(self):
        while True:
          _, self.frame = self.cap.read()       
#read new frame
          self.frame = cv2.flip( self.frame, 1 ) 
#flip horizontally
    
          if self.canvas is None:
            self.canvas = np.zeros_like(self.frame) 
#initialize a black canvas
            
          mask=self.CreateMask()             
#createmask
          contours=self.ContourDetect(mask)  
#detect Contours
          self.drawLine(contours)            
#draw lines
          self.display()                     
#display results
          k = cv2.waitKey(1) & 0xFF          
#wait for keyboard input
          self.takeAction(k)                 
#take action based on k value
        
          if k == 27:                        
#if esc key is pressed exit
            break       

    def CreateMask(self):
      hsv = cv2.cvtColor(self.frame,
cv2.COLOR_BGR2HSV) #convert from BGR to HSV color range
      lower_range = self.penrange[0]                   
 #load  HSV lower range
      upper_range = self.penrange[1]                   
 #load  HSV upper range
      mask = cv2.inRange(hsv, lower_range, 
upper_range) 
#Create binary mask
      return mask

    def ContourDetect(self,mask):
        # Find Contours based on the mask created.
      contours, hierarchy = cv2.findContours(mask, 
cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      return contours

    def drawLine(self,contours):
        #if contour area is not none and is greater than 100 draw the line
      if contours and cv2.contourArea(max(contours, 
key = cv2.contourArea)) > 100:  #100 is required min contour area              
          c = max(contours, key = cv2.contourArea)    
          x2,y2,w,h = cv2.boundingRect(c)
    
      if self.x1 == 0 and self.y1 == 0:  
  #this will we true only for the first time marker is detected
          self.x1,self.y1= x2,y2
       else:
                # Draw the line on the canvas
          self.canvas = cv2.line(self.canvas,
 (self.x1,self.y1),(x2,y2), [255*self.val,0,0], 10)
            #New point becomes the previous point 
            self.x1,self.y1= x2,y2
       else:
            # If there were no contours detected then make x1,y1 = 0 (reset)
          self.x1,self.y1 =0,0   

    def display(self):
        # Merge the canvas and the frame.
        self.frame = cv2.add(self.frame,
self.canvas)    
        cv2.imshow('frame',self.frame)
        cv2.imshow('canvas',self.canvas)

    def takeAction(self,k):
        # When c is pressed clear the entire canvas
        if k == ord('c'):
            self.canvas = None
        #press e to change between eraser mode and writing mode
        if k==ord('e'):
            self.val= int(not self.val) # toggle
 val value between 0 and 1 to change marker color.
                    
if __name__ == '__main__':
    drawingCanvas()
     
cv2.destroyAllWindows()
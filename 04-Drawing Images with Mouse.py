####
# We can un/comment all the lines with ctrl+/(forward slash)
####



import cv2
import numpy as np



def draw_circle(event, x, y, flags, params):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        cv2.circle(img, (x,y), 50, color=(0,255,0), thickness=-1)
        
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        
        cv2.circle(img, (x,y), 50, color=(0,0,255), thickness=-1)
    
    
    
cv2.namedWindow(winname='my_drawing')


# Connects the mouse button to our callback function

cv2.setMouseCallback('my_drawing', draw_circle)




img = np.zeros((512,512,3), dtype=np.int8)      #int8 makes them little gray or else black

while True:
    
    cv2.imshow('my_drawing', img)
    
    
    if cv2.waitKey(10) & 0xFF == 27:
        
        break
        
        
cv2.destroyAllWindows()        





###############
# Script: Dragging with Mouse
###############


# import cv2
# import numpy as np


# # declaring global variables so that we can grab these inside of a function coz global variables will be used in or outside of a function:

# drawing = False

# ix,iy = -1,-1



# # mouse callback function:

# def draw_rectangle(event, x, y, flags, params):
    
#     global ix, iy, drawing
    
    
#     if event == cv2.EVENT_LBUTTONDOWN:
        
#         drawing = True             # When you click DOWN with left mouse button drawing is set to True 
#         ix, iy = x, y              # Then we take note of where that mouse was located
        
     
#     elif event == cv2.EVENT_MOUSEMOVE:
        
#         if drawing:                                                      
            
#             # If drawing is True, it means you've already clicked on the left mouse button 
#             # We draw a rectangle from the previous position to the x,y where the mouse is
                        
#             cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), thickness=-1)
            
       
#     elif event == cv2.EVENT_LBUTTONUP:
        
#         drawing = False
        
#         # we complete the rectangle
        
#         cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), thickness=-1)
        
        
        
# cv2.namedWindow('my_drawing')     

# cv2.setMouseCallback('my_drawing', draw_rectangle)




# img = np.zeros((512,512,3))

# while True:
    
#     cv2.imshow('my_drawing', img)
    
    
#     if cv2.waitKey(10) & 0xFF == 27:
        
#         break
        
        
# cv2.destroyAllWindows()        


"""
If we take the mouse back then the rectangle does not make any sense

Try it out with mouse moving backwards 

coz rectangle is a rectangle of rectangles

"""

















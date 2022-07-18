import cv2


videoName = 'video.mp4'
videoName2 = 'video2.mp4'
vidstate = 1

#create a videoCapture Object (this allow to read frames one by one)
video = cv2.VideoCapture(videoName)
video2 = cv2.VideoCapture(videoName2)
#check it's ok
if video.isOpened():
    print('Video Succefully opened')
else:
    print('Something went wrong check if the video name and path is correct')


#define a scale lvl for visualization
scaleLevel = 2 #it means reduce the size to 2**(scaleLevel-1)


windowName = 'Video Reproducer'
cv2.namedWindow(windowName )
#let's reproduce the video
while True:
    ret,frame = video.read()
    ret,frame2 = video2.read() #read a single frame 
    if not ret: #this mean it could not read the frame 
         print("Could not read the frame")   
         cv2.destroyWindow(windowName)
         break

    reescaled_frame  = frame
    reescaled_frame2  = frame2
    for i in range(scaleLevel-1):
        reescaled_frame = cv2.pyrDown(reescaled_frame)
        reescaled_frame2 = cv2.pyrDown(reescaled_frame2)

    
    waitKey = (cv2.waitKey(1) & 0xFF)
    if  waitKey == ord('q'): #if Q pressed you could do something else with other keypress
         vidstate = 2
         print("closing video and exiting")
    if  waitKey == ord('d'): #if Q pressed you could do something else with other keypress
         vidstate = 1
         print("d was presse")


    
    if  vidstate == 1:
        cv2.imshow(windowName, reescaled_frame )
    if  vidstate == 2:
        cv2.imshow(windowName, reescaled_frame2 )
        
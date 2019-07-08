#This is an app that deletes parts from the a video to edit it based on colors

from moviepy.editor import *
import os
import cv2
import numpy as np
import math as math
# from ImageWriter import  *
# import read_frames_fast as fs
from imutils.video import FileVideoStream
from imutils.video import FPS
import imutils
import time




def detect_green():
    pass


def detect_red():
    pass

def detect_color():
    pass

def detect_silence():
    pass


def make_list():
    pass


def update_list():
    pass

def final_cut():
    pass
#######################################


#returns the percentage of the green color in a photo
def detect_green(pathin):
   
    img = pathin
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    dimensions = img.shape 
     
    #Red color rangle  169, 100, 100 , 189, 255, 255
     
    BW = cv2.inRange(hsv,  (36, 25, 25), (70, 255,255))
    BW = cv2.cvtColor(BW, cv2.COLOR_BGR2RGB)
    BW =  cv2.cvtColor(BW, cv2.COLOR_BGR2GRAY)
    numTotalPixel = BW.size    
    numWhitePixel = cv2.countNonZero(BW)
    percentWhitePixel = numWhitePixel / numTotalPixel * 100;
   
    cv2.destroyAllWindows()
    return int(percentWhitePixel)



# print(detect_green("red and green circles.png"))


#returns the percentage of the red color in a photo
def detect_red(pathin):
    # img = cv2.imread(pathin)
    img = pathin
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    dimensions = img.shape 
     
    #Red color rangle  169, 100, 100 , 189, 255, 255
     
    mask1 = cv2.inRange(hsv, np.array([0,70,50]), np.array([10,255,255]))
    mask2 = cv2.inRange(hsv, np.array([170,70,50]), np.array([180,255,255]))
    BW = mask1 | mask2
    BW = cv2.cvtColor(BW, cv2.COLOR_BGR2RGB)
    BW =  cv2.cvtColor(BW, cv2.COLOR_BGR2GRAY)
    numTotalPixel = BW.size    
    numWhitePixel = cv2.countNonZero(BW)
    percentWhitePixel = numWhitePixel / numTotalPixel * 100;
   
    cv2.destroyAllWindows()
    return int(percentWhitePixel)



def detect_color(pathin):
    # construct the argument parse and parse the arguments

    # start the file video stream thread and allow the buffer to
    # start to fill
    fvs = FileVideoStream(pathin).start()
    time.sleep(1.0)

    # start the FPS timer
    fps = FPS().start()
    when = []
    count = 0
    cap = cv2.VideoCapture(pathin)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_rate = cap.get(cv2.CAP_PROP_FPS )
        
    # loop over frames from the video file stream
    while fvs.more() and count < length:
        # grab the frame from the threaded video file stream, resize
        # it, and convert it to grayscale (while still retaining 3
        # channels)
        frame = fvs.read()
        count += 1
        frame = imutils.resize(frame, width=450)
        r=  detect_red(frame)
        g = detect_green(frame)
        t = count/frames_rate
        if r >= 15 and g >= 15:

            when.append("-")

        elif g >= 15:

            when.append(["g",t])

        elif r >= 15:

            when.append(["r",t]) 

        else:

            when.append("-")

        frame = np.dstack([frame, frame, frame]) 
        # show the frame and update the FPS counter
        fps.update()

    # stop the timer and display FPS information
    fps.stop()
    # do a bit of cleanup
    cv2.destroyAllWindows()
    fvs.stop()
    return when




def detect_silence(pathin):
    pass



def make_list(pathin, thelist):

    bgr = []
    bggrr = []
    flag1 = 0

    #flag1 == 0  we are in a middle region
    # flag1 == 1  we are in a red region
    #flag1 == 2  we are in a green region
    for i in range(len(thelist)):

        if thelist[i] == "-" and flag1 == 0:
            
            flag1 == 0


        if type(thelist[i]) is list and thelist[i][0] == "r" and flag1 == 0:

            bgr.append(thelist[i])
            bggrr.append(thelist[i])
            flag1 = 1

        elif type(thelist[i]) is list and thelist[i][0] == "r" and flag1 == 1:
           
            flag1 = 1

        elif thelist[i] == "-" and flag1 == 1:

            bggrr.append(thelist[i-1])
            flag1 = 0

        elif type(thelist[i]) is list and thelist[i][0] == "g" and flag1 == 0:

            bggrr.append(thelist[i])
            flag1 = 2 

        elif type(thelist[i]) is list and thelist[i][0] == "g" and flag1 == 2:
           
            flag1 = 2 

        elif thelist[i] == "-" and flag1 == 2:
           
            bgr.append(thelist[i-1])
            bggrr.append(thelist[i-1])
            flag1 = 0


    cap = cv2.VideoCapture(pathin)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_rate = cap.get(cv2.CAP_PROP_FPS )
    bgr.append(["r",length / frames_rate])
    #bgr contains the sections between colors
    #ggrr contains the frames region 
    return bgr , bggrr





def update_list(thelist, ta, tb):

    
    for i in range(len(thelist)):
        if thelist[i][1] < ta:
            thelist[i][1] = thelist[i][1]
        # elif thelist[i][1] >= ta and thelist[i][1] < tb:
        #     del thelist[i]
        elif thelist[i][1] >= tb:
            thelist[i][1] = thelist[i][1] - (tb - ta)            
        else:
            thelist[i][1] = thelist[i][1]

    return thelist


def final_cut(pathin,pathout):
    
    cap = VideoFileClip(pathin)
    thelist = detect_color(pathin)
    bgr , bggrr = make_list(pathin,thelist)


    #cutout the periods before red
    for i in range(len(bgr)):
        
        if i == 0 and bgr[i][0] == "r":
            cap = cap.cutout(0,bgr[i][1])
            bgr = update_list(bgr,0,bgr[i][1])
            bggrr = update_list(bgr,0,bgr[i][1])

        elif bgr[i][0] == "r" and i != 0:
            cap = cap.cutout(bgr[i-1][1],bgr[i][1])
            bgr = update_list(bgr,bgr[i-1][1],bgr[i][1])
            bggrr = update_list(bgr,bgr[i-1][1],bgr[i][1])

        else:
            pass

    #cutout the colored periods
    for i in range(1,len(bggrr)):
    
        if bggrr[i][0] == bggrr[i-1][0]:
            cap = cap.cutout(bggrr[i-1][1],bggrr[i][1])
            bggrr = update_list(bggrr,bggrr[i-1][1],bggrr[i][1])

        elif bggrr[i][0] != bggrr[i-1][0]:
            pass

        else:
            print("error")


    #cutout the silence periods   




    #return the video and save in pathout
    cap.write_videofile(pathout)
    return cap

































# thelist = ["-","-","-","-","-","-","-","-","-",["r",10],["r",11],["r",12],["r",13]
# ,"-","-","-","-","-","-","-","-","-",["g",23],["g",24],["g",25],["g",26],"-","-",
# "-","-","-","-","-","-","-",["r",35],["r",36],["r",37],["r",38],"-","-","-","-",
# "-","-","-","-","-",["g",47],["g",48],["g",49],["g",50],"-","-"]


# h, hh = final_cut("wow.mp4",thelist )

# print(h)
# print("\n")
# print(hh)
# print(edit_time(h,2,5))



# print(detect("wow.mp4"))
# print("\n")
# print(detect("wow.mp4", "red"))
# cap = cv2.VideoCapture("wow.mp4")
# length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# print(length)











# def record():
#     cap = cv2.VideoCapture(0)
#     fourcc = cv2.VideoWriter_fourcc(*"XVID")
#     out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))
#     while(True):
#         ret, frame = cap.read()
#         out.write(frame)
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     out.release()
#     cv2.destroyAllWindows()
        

# def upload_video():
#     cap = cv2.VideoCapture('rihno.mp4')

#     while(cap.isOpened()):
#         ret, frame = cap.read()
#         cv2.imshow('frame',frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
    
# #######################################
# upload_video()
# messing around


# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     out.write(frame)
#     # Our operations on the frame come here
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Display the resulting frame
#     cv2.imshow('frame', frame)
#     cv2.imshow('gray', gray)
#     cv2.imshow('hsv', hsv)



#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# out.release()
# cv2.destroyAllWindows()



# #convert the video to phrames 1 fps
# def detect(file_name,color):#, pathOut):
#     cap = cv2.VideoCapture(file_name)
#     frameRate = cap.get(5) #frame rate
#     success,image = cap.read()
#     count = 0
#     success = True
#     when = []
#     while success:
#         frameId = cap.get(1)   #current frame number
#         if (frameId % math.floor(frameRate) == 0):
#             if color == "red":
#                 when.append(detect_red(image))
#             if color =="green":
#                 when.append(detect_green(image))
#         print(when)
#         success,image = cap.read()
#     cap.release()
#     cv2.destroyAllWindows()
#     return when


# def detect_red(pathin):
   
#     # img = cv2.imread(pathin)
#     img = pathin
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     dimensions = img.shape 
     
#     #Red color rangle  169, 100, 100 , 189, 255, 255
     
#     mask1 = cv2.inRange(hsv, np.array([0,70,50]), np.array([10,255,255]))
#     mask2 = cv2.inRange(hsv, np.array([170,70,50]), np.array([180,255,255]))
#     BW = mask1 | mask2
#     BW = cv2.cvtColor(BW, cv2.COLOR_BGR2RGB)
#     red=0
#     All=0
#     for x in range (BW.shape[1]):
#         for y in range (BW.shape[0]):

#             color = BW[y,x]
#             if np.array_equal(color ,np.array([255, 255, 255])):

#                 red += 1
#             All += 1 

#     return int((red / All)*100)



#cut the video
# def cut(video_name,vid1,vid2,output,t1,t2):



#     # from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#     # ffmpeg_extract_subclip(video_name, 0, t1, targetname="clip1.mp4")
#     # ffmpeg_extract_subclip(video_name, t2 + 1 ,VideoFileClip(video_name).duration , targetname="clip2.mp4")

    
#     clip1 = VideoFileClip(video_name).subclip(0,t1)
#     clip1.write_videofile(vid1)
#     clip2 =VideoFileClip(video_name).subclip(t2 + 1,VideoFileClip(video_name).duration)
#     clip2.write_videofile(vid2)
#     result = concatenate_videoclips([VideoFileClip(vid1), VideoFileClip(vid2)])
#     result.write_videofile(output)
#     os.remove(vid1)
#     os.remove(vid2)
#     return result

# clip1 = VideoFileClip("wow.mp4").cutout(2,4)
# clip1.write_videofile("wow2.mp4")
# cut("wow.mp4", "clip1.mp4","clip2.mp4", 2,5)
# result = concatenate_videoclips([VideoFileClip("clip1.mp4"), VideoFileClip("clip2.mp4")])
# result.write_videofile("final.mp4")

# def concatenate(clip1,clip2,output):
#     result = concatenate_videoclips([VideoFileClip(clip1), VideoFileClip(clip2)])
#     result.write_videofile(output)
#     os.remove(clip1)
#     os.remove(clip2)
#     return result
# 

# concatenate("clip1.mp4","clip2.mp4","wow2.mp4")
# 
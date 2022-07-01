import base_lib
from robot.api.deco import keyword
import time
from locators import camera_locators as loc
import sys
import os

ROBOT_AUTO_KEYWORDS = False

@keyword
def LAUNCH_CAMERA():
    try:
        base_lib.launch_app(loc.appname)
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False


@keyword
def CAPTURE_IMAGE():
    try:
        #Clicking on capture button
        base_lib.click_on_id(loc.camera_click_resourceID,loc.camera_click_classname)
        #base_lib.click_on('Shutter','GLButton')
        #d(text='Shutter', className='GLButton').click()
        time.sleep(5)
        return True
    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def Verify_and_Delete_IMAGE():
    try:
        time.sleep(5)
        #Clicking on capture button
        base_lib.click_on_id(loc.round_thumbnail_ID,loc.round_thumbnail_class)
        time.sleep(5)
        base_lib.click_on_id(loc.delete_picture_ID,loc.delete_picture_class)


        time.sleep(5)
        return True
    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def Set_Timer(t):
    try:
        base_lib.click_on_id(loc.Three_dots_ID,loc.Three_dots_class)
        time.sleep(3)
        if t==3:
            base_lib.click_on_id(loc.Timer_ID,loc.Timer_class)
        elif t==10:
            base_lib.click_on_id(loc.Timer_ID, loc.Timer_class)
            base_lib.click_on_id(loc.Timer_ID, loc.Timer_class)

    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def Front_Camera():
    try:
        base_lib.click_on_id(loc.Front_camera_ID,loc.Front_camera_class)
        time.sleep(5)
        base_lib.click_on_id(loc.Front_camera_click_ID,loc.Front_camera_click_class)
        time.sleep(5)
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def Launch_Video():
    try:
        base_lib.click_on('Video','android.widget.TextView')
        time.sleep(5)
        base_lib.click_on_id(loc.video_record_click_ID,loc.video_record_click_class)
        time.sleep(10)
        base_lib.click_on_id(loc.video_record_click_ID,loc.video_record_click_class)

        return True

    except Exception as e:
       print("Exception Occured:", str(e))
    return False




'''
LAUNCH_CAMERA()
time.sleep(5)
CAPTURE_IMAGE()

time.sleep(5)
Verify_and_Delete_IMAGE()
'''
#base_lib.close_app()
LAUNCH_CAMERA()
Set_Timer(t=10)
time.sleep(3)
CAPTURE_IMAGE()
Front_Camera()
Launch_Video()




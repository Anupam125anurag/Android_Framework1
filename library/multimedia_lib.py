import base_lib
from robot.api.deco import keyword
from locators import multimedia_locators
import time


ROBOT_AUTO_KEYWORDS = False

@keyword
def LAUNCH_MUSIC():
    try:
        base_lib.launch_app(multimedia_locators.music_appname)
        return True
    except Exception as e:
        print("Exception occured: ", str(e))
        return False

@keyword
def PLAY_MUSIC():
    try:
        #Clicking on play button
        base_lib.click_on_id(multimedia_locators.open_audio_resourceID, multimedia_locators.open_audio_classname)
        time.sleep(3)
        base_lib.click_on_id(multimedia_locators.open_audio_folder_resourceID, multimedia_locators.open_audio_folder_classname)
        time.sleep(3)
        base_lib.click_on_id(multimedia_locators.play_audio_file_resourceID, multimedia_locators.play_audio_file_classname)
        time.sleep(5)
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def PAUSE_MUSIC():
    try:
        #Clicking on pause button
        base_lib.click_on_id(multimedia_locators.to_fetch_play_pause_buttons_resourceID, multimedia_locators.to_fetch_play_pause_buttons_classname)
        time.sleep(3)
        base_lib.click_on_id(multimedia_locators.audio_play_pause_button_resourceID, multimedia_locators.audio_play_pause_button_classname)
        time.sleep(5)
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def NEXT_MUSIC():
    try:
        #Clicking on next button
        base_lib.click_on_id(multimedia_locators.audio_next_button_resourceID, multimedia_locators.audio_next_button_classname)
        time.sleep(5)
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False


@keyword
def PREVIOUS_MUSIC():
    try:
        #Clicking on pause button
        base_lib.click_on_id(multimedia_locators.audio_previous_button_resourceID, multimedia_locators.audio_previous_button_classname)
        time.sleep(5)
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def LAUNCH_VIDEO():
    try:
        base_lib.launch_app(multimedia_locators.video_appname)
        return True
    except Exception as e:
        print("Exception occured: ", str(e))
        return False

@keyword
def PLAY_VIDEO():
    try:
        #Clicking on play button
        base_lib.click_on_id(multimedia_locators.open_video_resourceID, multimedia_locators.open_video_className)
        time.sleep(3)
        base_lib.click_on_id(multimedia_locators.open_video_folder_resourceID, multimedia_locators.open_video_folder_className)
        time.sleep(3)
        base_lib.click_on_id(multimedia_locators.play_video_file_resourceID, multimedia_locators.play_video_file_className)
        time.sleep(5)
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def PAUSE_VIDEO():
    try:
        #Clicking on pause button
        base_lib.click_on_id(multimedia_locators.play_video_playlist_resourceID, multimedia_locators.play_video_playlist_className)
        time.sleep(3)
        base_lib.click_on_id(multimedia_locators.video_play_pause_button_resourceID, multimedia_locators.video_play_pause_button_className)
        time.sleep(3)
        base_lib.click_on_id(multimedia_locators.video_play_pause_button_resourceID, multimedia_locators.video_play_pause_button_className)
        time.sleep(5)
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def NEXT_VIDEO():
    try:
        #Clicking on next button
        base_lib.click_on_id(multimedia_locators.play_video_playlist_resourceID, multimedia_locators.play_video_playlist_className)
        time.sleep(3)
        base_lib.click_on_id(multimedia_locators.video_play_pause_button_resourceID, multimedia_locators.video_play_pause_button_className)
        time.sleep(3)
        base_lib.click_on_id(multimedia_locators.video_next_button_resourceID, multimedia_locators.video_next_button_classname)
        time.sleep(5)
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def PREVIOUS_VIDEO():
    try:
        #Clicking on previous button
        base_lib.click_on_id(multimedia_locators.play_video_playlist_resourceID, multimedia_locators.play_video_playlist_className)
        time.sleep(3)
        base_lib.click_on_id(multimedia_locators.video_play_pause_button_resourceID, multimedia_locators.video_play_pause_button_className)
        time.sleep(3)
        base_lib.click_on_id(multimedia_locators.video_previous_button_resourceID, multimedia_locators.video_previous_button_classname)
        time.sleep(5)
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def GOTO_HOME():
    try:
        base_lib.go_to_home()
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False

@keyword
def LAUNCH_BROWSER():
    try:
        base_lib.launch_app(multimedia_locators.browser_appname)
        return True

    except Exception as e:
        print("Exception Occured:", str(e))
        return False

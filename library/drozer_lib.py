import base_lib
from robot.api.deco import keyword
from locators import settings_locators
import time
import os





@keyword
def LAUNCH_DROZER():
    try:
        base_lib.launch_app("drozer Agent")
        return True

    except Exception as e:
        print("Exception occured: ",str(e))
        return False



@keyword
def CHECK_STATUS():
    time.sleep(2)
    if base_lib.check_existence_by_name("OFF","android.widget.ToggleButton"):
        base_lib.click_on("OFF","android.widget.ToggleButton")
    else:
        pass

*** Settings ***
Documentation    Sanity test
Suite Setup    Initialize Metadata

Library     ../library/base_lib.py
Library     ../library/settings_lib.py

Test Setup   START_TEST
Test Teardown  END_TEST

*** Keyword ***
Initialize Metadata
        #${devicename}       GET_DEVICE_NAME
        #Set suite metadata    Device Name    ${devicename}
        ${devicemodel}       GET_DEVICE_MODEL
        Set suite metadata    Device Model    ${devicemodel}
        ${Android_ver}       GET_ANDROID_VERSION
        Set suite metadata    OS Version    ${Android_ver}
        ${build_id}       GET_BUILD_ID
        Set suite metadata    Build ID    ${build_id}

*** Test Cases ***
Test 001 - Enable Adaptive Brightness
    [tags]    Sanity
    #launch settings
    ${result}     LAUNCH_SETTINGS
    ${result}     ENABLE_ADAPTIVE_BRIGHTNESS
    run keyword if  ${result}==False    Fail    Enabling_Adaptive_Brightness_failed   ELSE    LOG    PASS

Test 002 - Disable Adaptive Brightness
    [tags]    Sanity
    #launch settings
    ${result}     LAUNCH_SETTINGS
    ${result}     DISABLE_ADAPTIVE_BRIGHTNESS
    run keyword if  ${result}==False    Fail    Disabling_Adaptive_Brightness_failed   ELSE    LOG    PASS


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
Test 001 - Enable Wifi
    [tags]    Sanity
    #launch settings
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_SETTINGS
    ${result}     ENABLE_WIFI
    run keyword if  ${result}==False    Fail   Enabling_Wifi_Failed    ELSE    LOG    PASS

Test 002 - Enable Bluetooth
    [tags]    Sanity
    #launch settings
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_SETTINGS
    ${result}     ENABLE_BLUETOOTH
    run keyword if  ${result}==False    Fail   Enabling_Bluetooth_Failed     ELSE    LOG    PASS

Test 003 - Disable Wifi
    [tags]    Sanity
    #launch settings
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_SETTINGS
    ${result}     DISABLE_WIFI
    run keyword if  ${result}==False    Fail    Disabling_Wifi_Failed    ELSE    LOG    PASS

Test 004 - Disable Bluetooth
    [tags]    Sanity
    #launch settings
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_SETTINGS
    ${result}     DISABLE_BLUETOOTH
    run keyword if  ${result}==False    Fail    Disabling_Bluetooth_Failed    ELSE    LOG    PASS

Test 005 - Launch Quick Settings
    [tags]    Sanity
    #launch settings
    ${result}     OPEN_QUICK_SETTINGS
    run keyword if  ${result}==False    Fail    launch_quicksettings_failed   ELSE    LOG    PASS


Test 006 - Check for Battery Saver option in Quick Settings and Click on it
    [tags]    Sanity
    #launch settings
    ${result}     OPEN_QUICK_SETTINGS
    ${result}     VERIFY_BATTERY_SAVER_OPTION_AND_CLICK
    run keyword if  ${result}==False    Fail    Verifying_Battery_Saver_Failed    ELSE    LOG    PASS

#Test 007 - Verify Build ID
    #[tags]    Sanity
    #launch settings
    #${result}     VERIFY_BUILD_ID
    #run keyword if  ${result}==False    Fail    Verifying_Build_ID_Failed    ELSE    LOG    PASS

Test 008 - Enable Adaptive Brightness
    [tags]    Sanity
    #launch settings
    ${result}     LAUNCH_SETTINGS
    ${result}     ENABLE_ADAPTIVE_BRIGHTNESS
    run keyword if  ${result}==False    Fail    Enabling_Adaptive_Brightness_failed   ELSE    LOG    PASS

Test 009 - Disable Adaptive Brightness
    [tags]    Sanity
    #launch settings
    ${result}     LAUNCH_SETTINGS
    ${result}     DISABLE_ADAPTIVE_BRIGHTNESS
    run keyword if  ${result}==False    Fail    Disabling_Adaptive_Brightness_failed   ELSE    LOG    PASS


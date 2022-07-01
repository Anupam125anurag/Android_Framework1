*** Settings ***
Documentation    Sanity test
Suite Setup    Initialize Metadata

Library     ../library/base_lib.py
Library     ../library/drozer_lib.py

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
Test 001 - Launch Drozer
    [tags]    Drozer app
    #launch Drozer app
    ${result}     LAUNCH_DROZER
    ${result}     CHECK_STATUS
    run keyword if  ${result}==False    Fail   Enabling_Wifi_Failed    ELSE    LOG    PASS


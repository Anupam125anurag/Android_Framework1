import os
import time

build_id=os.popen("adb shell getprop ro.build.id").read()
build_fingerprint=os.popen("adb shell getprop ro.product.build.fingerprint").read()
build_date=os.popen("adb shell getprop ro.product.build.date").read()
build_type=os.popen("adb shell getprop ro.product.build.type").read()
mydir = "/home/idm/Desktop/MytcsApp1"

build_id=os.popen("adb shell getprop ro.build.id").read()

for subdir,dirs,files in os.walk(mydir):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".txt"):
            if filename=="Monkeylogs.txt":
                file=open(filepath,'r').read().splitlines()
                for elements in range(0,len(file)):
                    if "Caused by" in file[elements]:
                        f=open("/home/idm/Desktop/MytcsApp1/Parser_Result.txt" , "w")

			
			
			f.write("Specified Kernel Exception is coming from the below lines:") 
		        f.write("Log parser found the Exception..") 
                        f.write(file[elements])
			
                        f.write(file[elements+1])
                        f.write("Exception is coming from the below specified file and line:")
                        f.write(file[elements+2])







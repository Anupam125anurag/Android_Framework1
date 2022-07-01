import os
import tabulate
#import colorama
#from colorama import Fore, Back, Style
#import prettytable 
  
build_id=os.popen("adb shell getprop ro.build.id").read()
build_fingerprint=os.popen("adb shell getprop ro.product.build.fingerprint").read()
build_date=os.popen("adb shell getprop ro.product.build.date").read()
build_type=os.popen("adb shell getprop ro.product.build.type").read()

	
 
with open('Parser_Result.txt','r') as file:
    Str = file.read()

with open('drozerlog.txt','r') as file:
    Dz = file.read()

from tabulate import tabulate
 
# assign data

#from prettytable import PrettyTable

mydata = [
   
["ANDROID VERSION", "10"],
["BUILD ID", build_id],
["BUILD FINGERPRINT",build_fingerprint],
["BUILD DATE", build_date],
["BUILD TYPE",build_type],

["SANITY TEST REPORT","Please find it in the report.html file"],

["CTS TEST REPORT","Please find it in cts_results.zip folder"],

["MONKEY STABILITY TEST",Str],

["DROZER PENTESTING RESULT",Dz] ]
 
# create header
head = ["BUILD", "DETAILS"]


# display table
f=open("Android_Framework_Pixel_git/Report_all.txt" , "w")
f.write("BELOW IS THE REPORT OF DEVICE : PIXEL 4XL" )
f.write(tabulate(mydata,tablefmt="grid"))



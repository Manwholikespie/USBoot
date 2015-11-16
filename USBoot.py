import os
import time
os.system("clear")
# convert .iso to .img
print('If you have already inserted your USB device, remove it now.\n')

targetImg = raw_input(
'Please input the filepath to the .img file\n Ex: ~/Downloads/file/file.img\n\n > '
)

resultImg = raw_input(

'\nPlease input the filepath to the directory you want the .iso file in\n Ex: ~/Documents/DiskImages/\n\n > '
)
os.system("clear")
hdiutilCmd = "hdiutil convert -format UDRW -o " + targetImg + " " + resultImg
os.system(hdiutilCmd)
os.system("clear")

print('List of current devices:\n')
os.system("diskutil list")

print("""
\n***************************\n
PLEASE INSERT YOUR USB NOW.\n
***************************\n
""")
forget1 = raw_input('Press ENTER when ready.\n')
del forget1

os.system("diskutil list")
print('Locate the device node assigned to your flash media.\n')
disk = raw_input('What is the name of the disk? Ex: /dev/disk3\n > ')
print('Unmounting Disk' + disk)
diskCmd = "diskutil unmountDisk " + disk
os.system(diskCmd)
print('Disk unmounted')
time.sleep(3)
os.system('clear')

print('Copying image to disk...')
ddCmd = "sudo dd if=" + resultImg + " of=" + disk + " bs=1m"
os.system(ddCmd)
print('Information copied successfully.')
time.sleep(3)
os.system('clear')

ejectCmd = "diskutil eject " + disk
print('Disk ejected.')
time.sleep(3)
os.system('clear')
print(
"""
 _____ _                 _
|_   _| |__   __ _ _ __ | | __  _   _  ___  _   _
  | | | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | |
  | | | | | | (_| | | | |   <  | |_| | (_) | |_| |_
  |_| |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_(_)
                                |___/
"""
)

exit()

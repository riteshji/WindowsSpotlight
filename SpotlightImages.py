import struct
import ctypes
import os
import glob
#import requests
import json 
from tkinter import filedialog
from PIL import Image
import imghdr
import tkinter
import shutil 
import pathlib
from pathlib import Path, PurePath


HORIZONTAL = (1920, 1080)
VERTICAL = (1080, 1920)
#
#  STEP  1: Get the source folders of Spotlight images. 
#

#Windows keeps spotlight files in this folder, this is our source: 
STANDARD_SPOTLIGHT_FOLDER = '\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\' 

def getUserHome():
#Get user Home folder
      path = os.path.expanduser('~')
      return path
def getSpotLightPath():
#Get user's spotlight folder
      path =getUserHome() + STANDARD_SPOTLIGHT_FOLDER
      return path

#
# STEP 2: 
def getDestinationFolder():
# Get the destination folder where the spotlight files will be copied. 
# this is the standard Pictures folder under a users home directory. 
      path =getUserHome() + "\\Pictures\\Spotlight\\"
# USE this to select a folder and  copy there:  
      #tkinter.Tk().withdraw() 
      #path = filedialog.askdirectory(initialdir="/",  title='Select a directory to Copy Spotlight Images:')
      return path
#Spotlight  folder , for the current user is here: 
SPOTLIGHT_PATH =  getSpotLightPath()
#this is the destination folder for Spotlight images
DESTINATION_DIRNAME = getDestinationFolder() 
#within the destination folder, desktop size images will be copied here. 
DesktopFolder = DESTINATION_DIRNAME + "\\Desktop\\"
#within the destination folder, Mobile size images will be copied here. 
MobileFolder = DESTINATION_DIRNAME + "\\Mobile\\"
# 
# STEP 3: #     Now process the files in the users spotlight folder.
#
def getSpotlightfileslist():
      file_list = (sorted(glob.glob(SPOTLIGHT_PATH  + "\\*"), key=os.path.getmtime, reverse=True))
      return(file_list)
spotlight_images = getSpotlightfileslist()

def isImage(spotlightfile): 
      image_types = ("jpeg", "jpg", "png", "gif")
      file_type = imghdr.what(spotlightfile)
      if image_types.count(file_type) == 1:
            return True
      else: 
            return False 
 
def ImageType(img): 
      im = Image.open(img)
      if im.size == HORIZONTAL :
            return 1
      elif im.size == VERTICAL :
            return 2
      else : 
            return 0
i=0
def CopyImages () : 
      for img in spotlight_images :
            if isImage(img) : 
                  if ImageType(img) == 1 :
                        print("DesktopImage")
                        os.makedirs(os.path.dirname(DesktopFolder), exist_ok=True)
                        destpath =pathlib.Path(DesktopFolder + Path(img).stem + ".jpg" ) 
                        shutil.copy2(img,destpath)
                  elif ImageType(img) == 2 :
                        print("MobileImage")
                        os.makedirs(os.path.dirname(MobileFolder), exist_ok=True)
                        destpath =pathlib.Path(MobileFolder + Path(img).stem + ".jpg" ) 
                        shutil.copy2(img,destpath)
                  else: 
                        print("Not a Wallpaper")      
            else: 
                  print(f"File IS NOT AN IMAGE - ", img )            

CopyImages()
#---------------------------
# Name: Lauren McMullen
# Program: qr-code-generator.py
#---------------------------
# Purpose: This script uses the python qrcode library to 
#          generate a simple QR Code for user inputted 
#          data with a simply UI from the PySimpleGUI library
#---------------------------
# Credit:
# https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/
#    
#   and
#  
# https://pypi.org/project/qrcode/
#
# for documentiation on the libraries used in this script
#---------------------------

# import libraries
from os import link
import qrcode
import PySimpleGUI as sg

# --------------------------
# functions:

# def QRAction
# signature String String -> Image
# Produce and save final QR Image
def QRAction(LINK, FOLDER, FILENAME):
    img = makeQRBase(LINK)
    img.save(FOLDER + '\\' + FILENAME + '.png')
    return

# def make-qr-base
# signature String -> Image 
# produce the basic image of the qr code with given link and filename 
def makeQRBase(LINK):
    qr = qrcode.QRCode(version = 10, box_size = 10, border = 3) # make QR class
    qr.add_data(LINK) # add link as data
    qr.make(fit = True)
    img = qr.make_image(fill_color = (0,0,0), back_color = (255,255,255)) # QR colors
    return img


#def setup
# signature -> sg.window
# Configure the theme and layout of the GUI
def setup():
    sg.theme("DarkGreen6")

    layout = [[ sg.Text("Paste your link here:"), sg.In(size=(25,1), enable_events=True ,key='-LINK-')],
        [ sg.Text("Select save location:"), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse()],
        [  sg.Text("Save as:"), sg.In(size=(25,1), enable_events=True,key='-NAME-')],
         [ sg.Button("Create"), sg.Button("Close")]]

    window = sg.Window("QR Code Generator", layout, margins=(100,50))
    return window


# def main
# signature -> Image
# call all helpers and create the QR code with user input in GUI
def main():
    window = setup()
    while True:
        event, values = window.read()
        if event == "Create":
            QRAction(values['-LINK-'], values['-FOLDER-'], values['-NAME-'])
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    window.close()
    return

main()






















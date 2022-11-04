import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFrame
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import pyqtSlot
from PIL.ImageQt import ImageQt
from pdfloader import images_from_pdf_file
import pdf2image


def sampletext(widget, text = "Application content here", offset =(110, 55)):
    textLabel = QLabel(widget)
    textLabel.setText(text)
    textLabel.move(*offset)
    return textLabel

def normalwindow(widget, title = "PyQt5 Example", rect = (50, 50, 1620, 900)):
    widget.setGeometry(*rect)
    widget.setWindowTitle(title)
    return widget
t = []
def imagelabelautoresize(imageLabel):
    imageLabel.resize(imageLabel.pixmap().size())

def imagelabel(widget, pix = None, label_image = None, offset = (10, 70)):
    if not pix:
        pix = QPixmap()
    if not label_image:
        label_image = QLabel(widget)
    label_image.setText("test text")
    label_image.setPixmap(pix)
    print("pix {}".format((pix.width(), pix.height())))
    imagelabelautoresize(label_image)
    label_image.move(*offset)
    label_image.setScaledContents(True)
    return label_image

def pdfviewer(widget, pages):
    img = ImageQt(pages[0])
    imagelabel(widget, QPixmap.fromImage(img) )
    img1 = ImageQt(pages[1])
    imagelabel(widget, QPixmap.fromImage(img1), offset = (10, 670) )
    return img,img1

def pdfviewer1(widget, pages):
    print(len(pages), ' pages in total')
    imgs = map(ImageQt, pages)
    l, t = 10, 70
    for img in imgs:
        imagelabel(widget, QPixmap.fromImage(img), offset = (l, t))
        t += 600
    return tuple(imgs)
    pdffield = Text(pdf_frame, yscrollcommand=scrol_y.set, bg="grey")

    # Empty list for storing images
    photos = []
    # Storing the converted images into list
    for i in range(len(pages)):
        photos.append(ImageTk.PhotoImage(pages[i]))
    # Adding all the images to the text widget
    for photo in photos:
        pdffield.image_create(END, image=photo)

        # For Seperating the pages
        pdffield.insert(END, '\n\n')

def mainwindow():
    return QFrame()

def window():

    app = QApplication(sys.argv)
    widget = mainwindow()

    normalwindow(widget)
    sampletext(widget)
    imgs = pdfviewer(widget, images_from_pdf_file(size=(800, 900)))

    widget.show()
    sys.exit(app.exec_())
    del imgs

def windowtk():
    # Creating Tk container
    from pdf2image import convert_from_path
    from tkinter import Tk, Frame, Scrollbar, Text, mainloop, BOTH, RIGHT, END
    from PIL import Image, ImageTk

    root = Tk()
    # Creating the frame for PDF Viewer
    pdf_frame = Frame(root).pack(fill=BOTH, expand=1)
    # Adding Scrollbar to the PDF frame
    scrol_y = Scrollbar(pdf_frame, orient=VERTICAL)
    # Adding text widget for inserting images
    pdf = Text(pdf_frame, yscrollcommand=scrol_y.set, bg="grey")
    # Setting the scrollbar to the right side
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=pdf.yview)
    # Finally packing the text widget
    pdf.pack(fill=BOTH, expand=1)
    # Here the PDF is converted to list of images
    pages = images_from_pdf_file('mypdf.pdf', size=(800, 900))
    # Empty list for storing images
    photos = []
    # Storing the converted images into list
    for i in range(len(pages)):
        photos.append(ImageTk.PhotoImage(pages[i]))
    # Adding all the images to the text widget
    for photo in photos:
        pdf.image_create(END, image=photo)

        # For Seperating the pages
        pdf.insert(END, '\n\n')
    # Ending of mainloop
    mainloop()

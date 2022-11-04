from tkinter import * #Scrollbar, Frame, Tk, VERTICAL, BOTH, END, RIGHT, Text, Y, X, mainloop
from PIL import Image, ImageTk
from pdf2image import convert_from_path

from pdfloader import images_from_pdf_file

def mainwindow():
    return Tk()

def pdfwidget1(root):

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
    return pdf

def pdfwidget(root):
    frame = Frame(root).pack(fill=BOTH, expand = 1)
    # Adding Scrollbar to the PDF frame
    scrol_y = Scrollbar(frame, orient=VERTICAL)

    # Adding text widget for inserting images
    pdf = Text(frame, yscrollcommand=scrol_y.set, bg="grey")
    # Setting the scrollbar to the right side
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=pdf.yview)
    # Finally packing the text widget
    pdf.pack(fill=BOTH, expand=1)
    class pdfframe:
        def __init__(self, frame, pdf):
            self.frame = frame
            self.pdf = pdf
            self.photos = None
        def load(self, pages):
            pdf = self.pdf
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
            pdf.pack(fill=BOTH, expand=1)
            # hold a reference for the photos! important!
            self.photos = photos
            return photos
    return pdfframe(frame, pdf)

def windowtk():
    # Creating Tk container
    from pdf2image import convert_from_path

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

def loadpdf(pdf, images):
    pages = images
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
    return photos
def windoworg():
    # Creating Tk container
    root = mainwindow()

    # Creating the frame for PDF Viewer
    pdf = pdfwidget(root)

    # Here the PDF is converted to list of images
    pdf.load(images_from_pdf_file('mypdf.pdf', size=(800, 900)))


    # Ending of mainloop
    mainloop()
def window():
    windoworg()

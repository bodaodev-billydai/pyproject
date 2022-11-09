import os
from pdf2image import convert_from_path
#https://blog.alivate.com.au/poppler-windows/
#https://pypi.org/project/pdf2image/

poppler_path='D:/poppler-0.68.0_x86/poppler-0.68.0/bin'
#poppler_path='D:/poppler-22.04.0/Library/bin'
#poppler_path='D:\pyproject\hello\venv\Lib\site-packages\poppler-0.39.0-win32\lib'
# download poppler from following website
# source need build.  https://github.com/oschwartz10612/poppler-windows/releases/
#You will then have to add the bin/ foldertoPATH or use poppler_path = r"C:\path\to\poppler-xx\bin" as an argument in convert_from_path.

def images_from_pdf_file(file_name = 'D:/PYPROJECT/HELLO/mypdf.pdf', **kws):
    return convert_from_path(file_name, poppler_path =poppler_path,  **kws)




__all__ = {"images_from_pdf_file"}

# %%
from docx import Document
import os
from win32com import client as wc

# %%
def doc2docx(oldpath, newpath):
    word = wc.Dispatch('Word.Application')
    doc = word.Document.Open(oldpath)
    doc.SaveAs(newpath, 12)
    doc.Close()
    word.quit()

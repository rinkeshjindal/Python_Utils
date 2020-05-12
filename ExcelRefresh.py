'''
Created on May 4, 2020

@author: Rinkesh_Jindal
'''
import os, os.path
import win32com.client

if os.path.exists("C:\\Users\\rinkesh_jindal\\Downloads\\savings_Planning_4May2020.xlsm"):
    print("Testing")
    xl=win32com.client.Dispatch("Excel.Application")
    book = xl.Workbooks.Open(os.path.abspath("C:\\Users\\rinkesh_jindal\\Downloads\\savings_Planning_4May2020.xlsm"))
    xl.Application.Run("savings_Planning_4May2020.xlsm!PivotRefreshMod.PivotRefreshMod")
    book.Save()
    #xl.Application.Save()
    print("After Saving")
    xl.Application.Quit() # Comment this out if your excel script closes
    print("After Quit")
    del xl
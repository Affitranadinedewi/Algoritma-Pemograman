# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 23:45:31 2021

@author: ID20072
"""
NAMA :Affitra Nadine Dewi
NIM : o64002100025

hitung = 0
jawab = "iyah"


while(jawab == "iyah"):
    inputbulan = int(input("Enter in the month: "))
    inputtahun = int(input("Enter in the year: "))
    jawab = str(input("ingin lanjut atau tidak: "))




    def hitung_bulan():

      if(inputbulan >= 13 or inputbulan <= 0):
          print("invalid value entered")

      elif(inputbulan == 1 or inputbulan == 3 or inputbulan == 5 or inputbulan == 7 or inputbulan == 8 or inputbulan == 10 or inputbulan == 12):
    	     print(" The are 31 days in the month ")



      elif (inputbulan == 2):

        if(inputtahun % 4 == 0 and inputbulan == 2):
          print("The are 29 days in the month")
          return

        else :
            print("The are 28 days in the month ")

      else:
          print("The are 30 days in the month")


    hitung_bulan()

# !/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Author: Dwarika 
# @Env: python 3.6 
# @Github: https://github.com/Dwarkeshsahu/InfluenceCoding 


import phonenumbers 
from phonenumbers import geocoder as GC
from phonenumbers import carrier as CR
from phonenumbers import timezone as TZ

def PHONE_NO_DETAILS() :

    usernumber = input("Enter Your Number :")
    
    phone_no = phonenumbers.parse(usernumber)
    
    DETAILS_1 = GC.description_for_number(phone_no , "en")
    
    DETAILS_2 = CR.name_for_number(phone_no , "en")
    
    DETAILS_3 = TZ.time_zones_for_number(phone_no)
    
    # Number Details 
    print(DETAILS_1)
    
    # Number Informatiom 
    print(DETAILS_2)

    # Number Time Zone 
    print(DETAILS_3)
    

PHONE_NO_DETAILS()


"""
    User Mobile Number Details 
    
    How To Use 
    Example : 
    If You From India Enter Your Number 
    This Formate 
    
    Enter : +91****
    
    This Code Not Run In SL 
    Run Your PC 
    You will get better parformace 
    
    Thank You 


"""






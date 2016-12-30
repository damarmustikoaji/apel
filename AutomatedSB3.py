# Author : damar mustiko aji / ID @damarresin
# damar.mustikoaji@gmail.com

from Testcase.Authentication.Authentication import Login
from Testcase.Authentication.Authentication import Logout

from Testcase.UserSettings.UserSettings import ChangeLanguage
from Testcase.UserSettings.UserSettings import ChangePassword

from Testcase.SendReport.SendMail import SendViaMail

import unittest
import time
import random
import string
import sys
import getpass
import logging
import openpyxl
from openpyxl.styles import Font
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
from openpyxl.styles import colors
from openpyxl.styles import Font, Color
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

class IniTestku(unittest.TestCase):

    wb = Workbook()
    sheet = wb.active
    now = time.strftime("%c")
    waktunya = "%s"  % now

    col_1 = sheet['B3']
    col_2 = sheet['C3']
    col_3 = sheet['D3']
    col_4 = sheet['E3']
    col_1.font = Font(color=colors.BLACK, bold=True, size=12)
    col_2.font = Font(color=colors.BLACK, bold=True, size=12)
    col_3.font = Font(color=colors.BLACK, bold=True, size=12)
    col_4.font = Font(color=colors.BLACK, bold=True, size=12)

    ModeTest = None
    TitleTest = None
    EmailReport = "damar@mailinator.com"
    pathReport = "Report/" #Buatlah FOLDER : Report/ diluar folder AutomatedTest untuk menyimpan file Report.xlsx
    #Account
    UserA = ""
    UserB = ""
    Password = ""
    NewPasswordB = ""

    MailA = ""
    MailB = ""

    JanganPanik = "janganpanik"#password default
    UserC = JanganPanik

    #Sebangsa Web Apps
    Browser = ""
    LIVE = "https://sebangsa.com/"

    URL = LIVE #Change URL to Using DEVEl or LIVE

    print ("Sebangsa Version "+URL)

    #Change Language
    Bahasa = "English" #jika kondisi awal Indonesia (default)
    BahasaDefault = "Bahasa Indonesia"

    #Colom Name Excel
    sheet['B3'] = 'NO.'
    sheet['C3'] = 'TEST'
    sheet['D3'] = 'STATUS'
    sheet['E3'] = 'LOGGING'
    sheet['F3'] = 'Login'
    sheet['G3'] = 'Password'

    sheet['D1'] = URL
    sheet['C2'] = waktunya

    def setUp(self):
        if "Chrome" in self.Browser:
            self.driver = webdriver.Chrome()
        elif "Firefox" in self.Browser:
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        self.driver.set_window_size(1280,800)
        self.driver.maximize_window()

    def test_6_h_Change_DEFAULT(self):#3
        print ('\n')
        print ("Change Default Settings")
        driver = self.driver
        driver.get(self.URL)
        driver, logging, status = Login(driver, self.UserA, self.Password)
        self.sheet['C68'] = 'Change Language Settings Default'
        driver, logging, status = ChangeLanguage(driver, self.BahasaDefault)
        self.sheet['B68'] = '59'
        self.sheet['D68'] = status
        self.sheet['E68'] = logging
        self.sheet['F68'] = self.UserA
        self.sheet['G68'] = self.Password
        print ("Status: "+status)
        print ("Log: "+logging)
        driver, logging, status = Logout(driver)
        driver, logging, status = Login(driver, self.UserB, self.NewPasswordB)
        self.sheet['C69'] = 'Password Settings Default'
        driver, logging, status = ChangePassword(driver, self.Password, self.NewPasswordB)#password disamakan Username = Password
        self.sheet['B69'] = '60'
        self.sheet['D69'] = status
        self.sheet['E69'] = logging
        self.sheet['F69'] = self.UserB
        self.sheet['G69'] = self.NewPasswordB
        print ("Status: "+status)
        print ("Log: "+logging)
        driver, logging, status = Logout(driver)

    def test_6_i_send_report(self):
        print ("\n")
        laporan = SendViaMail(self.TitleTest, self.URL, self.waktunya, self.EmailReport)
        print (laporan)

    def tearDown(self):
        self.driver.close()
        self.sheet['C1'] = self.TitleTest
        self.wb.save(self.pathReport+self.TitleTest+".xlsx"))

if __name__ == "__main__":
    command = len(sys.argv)
    try:
        if command == 4:
            print ("++Mode Automated Testing Full Testcase++")
            IniTestku.ModeTest = 1
            IniTestku.TitleTest = "Full-Testing"
            IniTestku.Browser = sys.argv.pop()
            if "Chrome" in IniTestku.Browser or "Firefox" in IniTestku.Browser:
                print ("Browser: "+IniTestku.Browser)
            else:
                sys.exit("ERROR : Please check again your argument\n")
            IniTestku.Password = sys.argv.pop()
            IniTestku.UserA = sys.argv.pop()
            IniTestku.UserB = "bot_"+IniTestku.UserA
            IniTestku.NewPasswordB = IniTestku.UserB
            IniTestku.MailA = IniTestku.UserA+"@mailinator.com"
            IniTestku.MailB = IniTestku.UserB+"@mailinator.com"
            print ("New Password: "+IniTestku.Password)
            print ("New Account Name (UserA): "+IniTestku.UserA)
            print ("New Account Name (UserB): "+IniTestku.UserB)
            print ("New Password (UserB): "+IniTestku.NewPasswordB)
            print ("Email 1 (UserA): "+IniTestku.MailA)
            print ("Email 2 (UserB): "+IniTestku.MailB)
        else:
            sys.exit("==================================|||===================================== \nHelp Command Argument: \nFull test $python CommandAutomated.py <UsernameNew> <Password> <Browser> \nCont test $python CommandAutomated.py <Browser> \nConttest2 $python CommandAutomated.py \n==========================================================================\n")
    except Exception as e:
        raise

    unittest.main()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import shutil
from ftplib import FTP
from datetime import date
from dotenv import load_dotenv

load_dotenv()

emaillogin = os.environ.get("semrush-email")
passwordlogin = os.environ.get("semrush-pass")


def getreports():

    driver = webdriver.Chrome()
    driver.get("https://semrush.com")

    time.sleep(2)

    driver.find_element_by_xpath(
        "/html/body/div[3]/div[2]/header/div/div/div[2]/a[1]/span[1]").click()

    time.sleep(2)

    email = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/label[1]/div[2]/div/input')

    email.send_keys(emaillogin)

    password = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/label[2]/div[2]/div/input')

    password.send_keys(passwordlogin, Keys.RETURN)

    time.sleep(2)

    reports = driver.find_element_by_xpath(
        "/html/body/main/div/div[1]/div/div[1]/nav/div[2]/div[1]/a[1]").click()

    time.sleep(2)

    pdfbuttons = driver.find_elements_by_class_name(
        "my-reports-report-list-table__td__download-icon")

    for buttons in pdfbuttons:
        buttons.click()
        time.sleep(1)
        download = buttons.find_element_by_xpath(
            "/html/body/div[8]/div/div[1]/div/div[1]")
        download.click()
        time.sleep(1)


source_folder = "/Users/jacob/Downloads"
dest_folder = "/Users/jacob/Documents/Reports"
string_to_match = "Monthly_Report"


def copyCertainFiles(source_folder, dest_folder, string_to_match, file_type=None):
    # Check all files in source_folder
    for filename in os.listdir(source_folder):
        # Move the file if the filename contains the string to match
        if file_type == None:
            if string_to_match in filename:
                shutil.move(os.path.join(source_folder, filename), dest_folder)

        # Check if the keyword and the file type both match
        elif isinstance(file_type, str):
            if string_to_match in filename and file_type in filename:
                shutil.move(os.path.join(source_folder, filename), dest_folder)


url = os.environ.get("ftpurl")
user = os.environ.get("ftpuser")
ftppass = os.environ.get("ftppass")


ftp = FTP(url)

ftp.login(user=user, passwd=ftppass)

clientIDS = {
    'creosalus': 100,
    'charlottecourt': 101,
    'commonwealthtreatment': 103,
    'anneshealinghands': 11,
    'hrassistance': 106,
    'jtdavis': 107,
    'abesauto': 113,
    'bestchoicesupply': 119,
    'tonichapman': 124,
    'yourpowerfullegacy': 127,
    'reliableresidentialroofing': 128,
    'portofinolexington': 14,
    'thecraftsman': 143,
    'chorogrip': 19,
    'ridecitycustoms': 31,
    'compliancemate': 35,
    'bluegrassangels': 39,
    'kodiakconstructionky': 47,
    'lexingtoncomputerrecycling': 49

}


def uploadreports():

    local_folder = "/Users/jacob/Documents/Reports"

    for k, v in clientIDS.items():
        print('key: ', k, 'value: ', v)
        ftp.cwd(
            f"/public_html/clients.btwebgroup.com/modules/addons/btwg/uploads/{v}")
        for filename in os.listdir(local_folder):
            if k in filename:
                with open(f"{local_folder}/{filename}", 'rb') as f:
                    ftp.storbinary(
                        'STOR %s' % f"{time.time()}, ___ Monthly Report ___ ,{filename}", f)


getreports()
#copyCertainFiles(source_folder, dest_folder, string_to_match, file_type=".pdf")

# uploadreports()

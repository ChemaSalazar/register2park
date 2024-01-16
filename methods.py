import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

def readProfile(profile):
    prof_file = open(profile + ".txt", "r")
    profile_data = prof_file.readlines()
    prof_file.close()
    return profile_data

def setData(profile_data):
    global propertyname
    global propertyvalue
    global apartment
    global vehiclemake
    global vehiclemodel
    global vehicleplates
    global email 

    propertyname = os.getenv("PROPERTY_NAME").strip()
    propertyvalue = os.getenv("PROPERTY_VALUE").strip()
    apartment = os.getenv("APT_NUMBER").strip()
    vehiclemake = profile_data[0].strip()
    vehiclemodel = profile_data[1].strip()
    vehicleplates = profile_data[2].strip()
    email = os.getenv("EMAIL").strip()


def usageMsg(profile_data):
    print(f"Your profile file has an incorrect number of entries. We found {len(profile_data)} when we expected 3.")
    print(f"We found the following fields {profile_data}.\n")
    print('Your file should have the following fields: ')
    print('Vehicle Make')
    print('Vehicle Number')
    print('Vehicle Plates\n')
    print('Please enter the required number of fields and re-run the script. :)\n')
    
def showData():
    print("++++++Summary of variables++++++")
    print("propertyname => " + propertyname)
    print("propertyvalue => " + propertyvalue)
    print("apartment => " + apartment)
    print("vehiclemake => " + vehiclemake)
    print("vehiclemodel => " + vehiclemodel)
    print("vehicleplates => " + vehicleplates)
    print("email => " + email)
    print("++++++++++++++++++++++++++++++++")


def setUpWebDriver():
    options = webdriver.ChromeOptions()
    # Prevent window from closing once instantiated.
    options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=options)

def populatePropertyForm(driver):
    element = driver.find_element(By.ID, "propertyName")
    element.send_keys(propertyname)
    confirmBtn = driver.find_element(By.ID, "confirmProperty")
    confirmBtn.click()
    time.sleep(1)

def selectPropertyForm(driver):
    radioOption = driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][value="' + propertyvalue + '"]')
    radioOption.click()
    # Now click the submit the 'Next' button
    confirmPropBtn = driver.find_element(By.ID, "confirmPropertySelection")
    confirmPropBtn.click()

def clickVisitorParkingBtn(driver):
    visitorParkingBtn = driver.find_element(By.ID, "registrationTypeVisitor")
    visitorParkingBtn.click()
    time.sleep(1)

def fillDetailsForm(driver):
    apartmentNum_field = driver.find_element(By.ID, "vehicleApt")
    apartmentNum_field.send_keys(apartment)
    vehicleMake_field = driver.find_element(By.ID, "vehicleMake")
    vehicleMake_field.send_keys(vehiclemake)
    vehicleModel_field = driver.find_element(By.ID, "vehicleModel")
    vehicleModel_field.send_keys(vehiclemodel)
    licensePlate_field = driver.find_element(By.ID, "vehicleLicensePlate")
    licensePlate_field.send_keys(vehicleplates)
    licensePlateCon_field = driver.find_element(By.ID, "vehicleLicensePlateConfirm")
    licensePlateCon_field.send_keys(vehicleplates)

def submitForm(driver):
    time.sleep(2)
    submissionBtn = driver.find_element(By.ID, "vehicleInformation")
    submissionBtn.click()
    time.sleep(10)
    emailConfirmModalBtn = driver.find_element(By.ID, "email-confirmation")
    emailConfirmModalBtn.click()
    time.sleep(2)
    email_field = driver.find_element(By.ID, "emailConfirmationEmailView")
    email_field.send_keys(email)
    emailSubmitBtn = driver.find_element(By.ID, "email-confirmation-send-view")
    emailSubmitBtn.click()
    time.sleep(4)
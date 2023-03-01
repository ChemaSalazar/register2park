import click
# selenium
import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

global profile_name
global propName
global propRadioVal
global aptNum
global vehMake
global vehModl
global vehPlts
global profEmail

global PREVENT_SUBMIT
PREVENT_SUBMIT = True


@click.command()
@click.option('--profile', prompt='Which profile would you like to use?', default='default',
              help='select file inside of profile dir')
# @click.option('--test', prompt='Prevent submit?', default=True,
#               help='This flag is created for testing before submitting the form to their server')
def runProfile(profile):
    click.echo(f"your are loading profile: {profile}")
    file1 = open("profiles/" + profile + ".txt", "r")
    profile_data = file1.readlines()
    file1.close()
    print(len(profile_data))
    if len(profile_data) != 7:
        exit()
    else:

        propName = profile_data[0].strip()
        propRadioVal = profile_data[1].strip()
        aptNum = profile_data[2].strip()
        vehMake = profile_data[3].strip()
        vehModl = profile_data[4].strip()
        vehPlts = profile_data[5].strip()
        profEmail = profile_data[6].strip()

        print("++++++Summary of variables++++++")
        print("propName => " + propName)
        print("propRadioVal => " + propRadioVal)
        print("aptNum => " + aptNum)
        print("vehMake => " + vehMake)
        print("vehModl => " + vehModl)
        print("vehPlts => " + vehPlts)
        print("profEmail => " + profEmail)
        print("++++++++++++++++++++++++++++++++")

        # Setup webdriver on Chrome
        options = webdriver.ChromeOptions()
        # Prevent window from closing once instantiated.
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        # Open driver on base register URL
        driver.get("https://www.register2park.com/register")

        # Auto enter property based on the profile you loaded, then submits to next page.
        element = driver.find_element(By.ID, "propertyName")
        element.send_keys(propName)
        confirmBtn = driver.find_element(By.ID, "confirmProperty")
        confirmBtn.click()

        time.sleep(1)

        # Auto select the property from list of options
        radioOption = driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][value="' + propRadioVal + '"]')
        radioOption.click()

        # Now click the submit the 'Next' button
        confirmPropBtn = driver.find_element(By.ID, "confirmPropertySelection")
        confirmPropBtn.click()

        # Now click the Visitor Parking Button to continue
        visitorParkingBtn = driver.find_element(By.ID, "registrationTypeVisitor")
        visitorParkingBtn.click()

        time.sleep(1)

        # Now declare all form fields and send keys
        apartmentNum_field = driver.find_element(By.ID, "vehicleApt")
        apartmentNum_field.send_keys(aptNum)

        vehicleMake_field = driver.find_element(By.ID, "vehicleMake")
        vehicleMake_field.send_keys(vehMake)

        vehicleModel_field = driver.find_element(By.ID, "vehicleModel")
        vehicleModel_field.send_keys(vehModl)

        licensePlate_field = driver.find_element(By.ID, "vehicleLicensePlate")
        licensePlate_field.send_keys(vehPlts)

        licensePlateCon_field = driver.find_element(By.ID, "vehicleLicensePlateConfirm")
        licensePlateCon_field.send_keys(vehPlts)

        # This section will not run by default, this is to prevent accidental submission when testing.
        # Reassign PREVENT_SUBMIT's value to False in order to submit the form.
        if not PREVENT_SUBMIT:
            time.sleep(2)

            submissionBtn = driver.find_element(By.ID, "vehicleInformation")
            submissionBtn.click()

            time.sleep(3)

            emailConfirmModalBtn = driver.find_element(By.ID, "email-confirmation")
            emailConfirmModalBtn.click()

            time.sleep(2)

            email_field = driver.find_element(By.ID, "emailConfirmationEmailView")
            email_field.send_keys(profEmail)

            emailSubmitBtn = driver.find_element(By.ID, "email-confirmation-send-view")
            emailSubmitBtn.click()

            time.sleep(4)


runProfile()

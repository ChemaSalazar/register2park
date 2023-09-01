import click
from methods import readProfile, setData, showData ,usageMsg, setUpWebDriver, populatePropertyForm, selectPropertyForm, clickVisitorParkingBtn, fillDetailsForm, submitForm

global PREVENT_SUBMIT
PREVENT_SUBMIT = True

global REG2PARK_URL
REG2PARK_URL = "https://www.register2park.com/register"



@click.command()
@click.option('--profile', prompt='Which profile would you like to use?', default='default',
              help='select file inside of profile dir')
# @click.option('--test', prompt='Prevent submit?', default=True,
#               help='This flag is created for testing before submitting the form to their server')

def runProfile(profile):
    click.echo(f"you are loading profile: {profile} \n")
    profile_data = readProfile(profile)

    if len(profile_data) != 3:
        usageMsg(profile_data)
        exit()
    else:
        #Set Profile data and display
        setData(profile_data)
        showData()

        # Setup webdriver on Chrome
        driver = setUpWebDriver()

        # Open driver on base register URL
        driver.get(REG2PARK_URL)
        # Auto enter property based on the profile you loaded, then submits to next page.
        populatePropertyForm(driver)

        # Auto select the property from list of options
        selectPropertyForm(driver)

        # Now click the Visitor Parking Button to continue
        clickVisitorParkingBtn(driver)


        # Now declare all form fields and send keys
        fillDetailsForm(driver)

        # This section will not run by default, this is to prevent accidental submission when testing.
        # Reassign PREVENT_SUBMIT's value to False in order to submit the form.
        if not PREVENT_SUBMIT:
            submitForm(driver)


runProfile()
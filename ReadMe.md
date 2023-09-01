# Register2Park Selenium-Python Automation Script

I created this script to make it convenient for me to submit
visitor parking requests, it's not a big deal to have to do it manually,
however I have many visitors, and it is more convenient to use
a profile-based submission rather than hunting for their info all the time.

That being said, please use it responsibly.

## Requirements

### Software
- Chromium WebDriver
- Latest version of Chrome
- Selenium
- `import click`
- `import time`
- `import os`
- dotenv
- Python 3+

### Files/Directories
- `main.py` script that executes automated processes.
- `methods.py` contains most functions necessary to run the script.
-  Required `.env` file. Holds property name, property id, apartment number, and email.
    - This file should NEVER be publically available, for this reason it will not be included. However it should contain the following Key-values (substitute `[YOUR_CUSTOM_VALUE]` with your information ):
      - ```
        PROPERTY_NAME=[YOUR_CUSTOM_VALUE]
        PROPERTY_VALUE=[YOUR_CUSTOM_VALUE]
        APT_NUMBER=[YOUR_CUSTOM_VALUE]
        EMAIL=[YOUR_CUSTOM_VALUE]
         ```
      - Note: PROPERTY_VALUE (This can be found on the https://www.register2park.com site by inspecting the value of the option after submitting the property name)  
      
- Required `profiles/` directory (this folder is excluded to prevent sensitive information to be published.)
  - this folder will hold your profiles in order for the script to run.
- At least one profile file inside profiles/
  - file must be in `.txt` format
  - The structure **MUST** be as follows (separated by newlines):

    - vehicle make
    - vehicle model
    - vehicle license plates


  -  Sample profile:
        ```
        Tesla
        Y
        ELONG8
        ```


**Please Note: If you are missing 3 entries in your profile, your program will terminate with the number of entries your profile file has.**
  
## Usage


#### Before running

Install all required software and libraries.

I highly recommend that you find the values you need prior to running this script.

For example, Make sure your propery name and property's radio button values are correct.

An easy way to find the value is by using inspect element on the input option after successfully submitting your property's name.

Make sure that you have your .env created and configured. See "Files/Directories" for examples.


#### Running the script

make sure you have at least one profile text file in your `profiles/`
then simply run 
`Python main.py`

follow the prompts:

`Which profile would you like to use? [default]:` 
you may specify your file (without .txt) or leave empty for the script to look for "default.txt"

After this the script will open a chrome browser and perform its tasks.


The program will run in non-submit mode, which means its prevents you from accidentally submitting data to the servers 
while testing. Once you are ready to submit, reassign `PREVENT_SUBMIT` to `False`.


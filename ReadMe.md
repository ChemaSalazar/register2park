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
- Python 3+

### Files/Directories
- `main.py` script that executes automated processes.
- `methods.py` contains most functions necessary to run the script.
- Required `profiles/` directory (this folder is excluded to prevent sensitive information to be published.)
  - this folder will hold your profiles in order for the script to run.
- At least one profile file inside profiles/
  - file must be in `.txt` format
  - The structure **MUST** be as follows (separated by newlines):
    - propery name
    - property radio button value (This can be found by inspecting the value of the option after submitting the property name)
    - apartment number
    - vehicle make
    - vehicle model
    - vehicle license plates
    - email address (used for confirmation email)


  -  Sample profile:
        ```
        Some Property Name
        12345
        123
        Tesla
        Y
        ELONG8
        example@company.com
        ```


**Please Note: If you are missing 7 entires on your profile, your program will terminate with the number of entries your profile file has.**
  
## Usage


#### Before running
I highly recommend that you find the values you need prior to running this script.

For example, Make sure your propery name and property's radio button values are correct.

An easy way to find the value is by using inspect element on the input option after successfully submitting your property's name.



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


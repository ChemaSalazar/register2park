# Register2Park Selenium-Python Automation Script

I created this script to make it convenient for me to submit
visitor parking requests, it's not a big deal to have to do it manually,
however I have many visitors, and it is more convenient to use
a profile-based submission rather than hunting for their info all the time.

That being said, please use it responsibly.

## Requirements

### Software
- Chromium WebDriver
- Selenium
- `import click`
- `import time`
- Python 3+

### Files/Directories
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
  
## Usage
make sure you have at least one profile text file in your `profiles/`
then simply run 
`Python main.py`

follow the prompts, that's it!

The program will run in non-submit mode, which means its prevents you from accidentally submitting data to the servers 
while testing. Once you are ready to submit, reassign `PREVENT_SUBMIT` to `False`.


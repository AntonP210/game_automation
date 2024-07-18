import time
import pytest
import os

# Import the functions from the automation script
from helpers import wait_for_element, open_program , wait_and_click 
from constants import MEMU_DIR, MEMU_LOGO , STORE_ICON , SIGN_IN , EMAIL_PHONE , EMAIL_PHONE,  FORGOT_EMAIL, CREATE_ACCOUNT , NEXT_BTN


    
def test_open_program():
    program_command = MEMU_DIR

    # Open the program
    open_program(program_command)

    # Wait for the element to appear
    memu_logo = wait_for_element(MEMU_LOGO)
    
    # Assert that the element was found
    assert memu_logo is not None, "Program was not found on the screen, automation is stopped."
    
def test_open_play_store():

    wait_and_click(STORE_ICON)
    
    time.sleep(2)
    wait_and_click(SIGN_IN)
    
def test_login_screen():
    time.sleep(4)
    email = wait_for_element(EMAIL_PHONE)
    assert email is not None, "Email_phone was not found."
    
    forgot_email = wait_for_element(FORGOT_EMAIL)
    assert forgot_email is not None, "forgot_email was not found."
    
    create_account = wait_for_element(CREATE_ACCOUNT)
    assert create_account is not None, "create_account was not found."
    
    next_btn = wait_for_element(NEXT_BTN)
    assert next_btn is not None, "next_btn was not found."
    


if __name__ == "__main__":
    pytest.main()
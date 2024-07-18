import time
import pytest
import os

# Import the functions from the automation script
from automation_helpers import wait_for_element, open_program , wait_and_click 
from constants import PROGRAM_DIR
script_dir = os.path.dirname(__file__)  # Directory of the current script


    
def test_open_program():
    program_command = PROGRAM_DIR

    # Open the program
    open_program(program_command)

    # Construct the path to the element image dynamically
    element_path = os.path.join(script_dir, 'images', 'memu_logo.png')  

    # Wait for the element to appear
    element_location = wait_for_element(element_path)
    
    # Assert that the element was found
    assert element_location is not None, "Program was not found on the screen, automation is stopped."
    
def test_open_play_store():

    store_icon = os.path.join(script_dir, 'images', 'store.png')  
    wait_and_click(store_icon)
    
    sign_in_btn = os.path.join(script_dir, 'images', 'signin.png') 
    time.sleep(2)
    wait_and_click(sign_in_btn)
    
def test_login_screen():
    time.sleep(2)
    email_phone = os.path.join(script_dir, 'images', 'email_phone.png')  
    assert email_phone is not None, "Email_phone was not found."
    
    forgot_email = os.path.join(script_dir, 'images', 'forgot_email.png') 
    assert forgot_email is not None, "forgot_email was not found."
    
    create_account = os.path.join(script_dir, 'images', 'create_account.png') 
    assert create_account is not None, "create_account was not found."
    
    next_btn = os.path.join(script_dir, 'images', 'next_btn.png') 
    assert next_btn is not None, "next_btn was not found."
    


if __name__ == "__main__":
    pytest.main()
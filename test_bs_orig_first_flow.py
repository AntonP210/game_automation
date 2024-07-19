import time
import pytest
import os
# import constants as con

# Import the functions from the automation script
from helpers import wait_for_element, open_memu , wait_and_click 
from constants import *

# Disabled for quicker debugging for now - later should be enabled.
# def test_open_memu_program():

#     # Open the program
#     open_memu(MEMU_DIR)

#     # Wait for the element to appear
#     memu_logo = wait_for_element(MEMU_LOGO)
    
#     # Assert that the element was found
#     assert memu_logo is not None, "MEMU was not found on the screen, automation is stopped."
    
def test_run_bs_orig_and_exit_to_map():
    wait_and_click(ORIG_APP_ICON)
    time.sleep(15)
    wait_and_click(ORIG_LEVEL_MENU_BTN)
    time.sleep(5)
    wait_and_click(ORIG_BLUE_EXIT)
    time.sleep(5)
    wait_and_click(ORIG_RED_EXIT)
    time.sleep(5)
    wait_and_click(ORIG_LEVEL_ONE_BTN)
    

if __name__ == "__main__":
    pytest.main()
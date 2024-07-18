import time
import pyautogui


def wait_for_element(image_path, timeout=30):
    """
    Wait until the specified element appears on the screen.

    :param image_path: The path to the image of the element.
    :param timeout: Maximum time to wait for the element (in seconds).
    :return: The location of the element if found, otherwise None.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        location = pyautogui.locateOnScreen(image_path)
        if location is not None:
            return location
        time.sleep(1)  # Wait for a short period before checking again
    return None

def open_program(program_command):
    """
    Open a program using the Win + R command.

    :param program_command: The command to run the program.
    """
    pyautogui.hotkey('win', 'r')  # Open the Run dialog
    time.sleep(1)
    pyautogui.write(program_command)
    pyautogui.press('enter')
    time.sleep(2)  # Wait for the program to open
    
def wait_and_click(image_path, ):
    element = wait_for_element(image_path)
    assert element is not None, "Element is missing"
    pyautogui.click(element)
    
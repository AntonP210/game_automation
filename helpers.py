import time
import pyautogui


def wait_for_element(image_path, timeout=30, region=None, grayscale=True, confidence=0.8):
    """
    Wait until the specified element appears on the screen.

    :param image_path: The path to the image of the element.
    :param timeout: Maximum time to wait for the element (in seconds).
    :param region: A tuple of (left, top, width, height) to limit the search region.
    :param grayscale: Whether to perform the search in grayscale.
    :param confidence: The confidence threshold for the image match (0 to 1).
    :return: The location of the element if found, otherwise None.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        # Pre-capture the screen
        screenshot = pyautogui.screenshot(region=region)
        
        # Perform the search on the captured image
        location = pyautogui.locate(image_path, screenshot, grayscale=grayscale, confidence=confidence)
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
    time.sleep(60)  # Wait for the program to open
    
def wait_and_click(image_path, ):
    element = wait_for_element(image_path)
    assert element is not None, "Element is missing"
    pyautogui.click(element)
    
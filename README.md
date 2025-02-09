# UI Automator2 Test Suite

## Overview
This project contains a set of automated UI tests using `uiautomator2` for an Android application. The tests verify various functionalities such as login, navigation, form input, scrolling, swiping, gestures, and more.

## Requirements
- Python 3.x
- `uiautomator2` library
- Android device (physical or emulator) with `adb` enabled
- Target application installed on the device

## Installation
1. Install Python dependencies:
   ```sh
   pip install uiautomator2 unittest
   ```
2. Ensure `adb` is installed and added to the system path.
3. Connect the Android device via USB or ensure an emulator is running.
4. Start the `uiautomator2` server on the device:
   ```sh
   python -m uiautomator2 init
   ```

## Test Cases
### 1. `test_login`
   - Inputs username and password
   - Clicks the login button
   - Verifies that the welcome message appears

### 2. `test_navigation`
   - Navigates through the menu and settings
   - Verifies that the settings and profile pages exist

### 3. `test_form_input`
   - Fills out and submits a form
   - Verifies submission confirmation

### 4. `test_scroll_and_click`
   - Scrolls to a target item and clicks it
   - Verifies item details page

### 5. `test_swipe`
   - Performs swipe gestures
   - Verifies new content loads

### 6. `test_image_match`
   - Matches an image with a reference image

### 7. `test_toast`
   - Clicks a button to show a toast message
   - Verifies the toast message content

### 8. `test_permission_dialog`
   - Requests a permission
   - Clicks "Allow" if prompted

### 9. `test_wait_and_click`
   - Waits for data to load before clicking

### 10. `test_multiple_elements`
   - Checks multiple buttons exist

### 11. `test_custom_selector`
   - Uses XPath to find and click a button

### 12. `test_gesture`
   - Performs a custom gesture

### 13. `test_press_key`
   - Presses Home, Back, and Recent keys

### 14. `test_screenshot`
   - Takes a screenshot

### 15. `test_device_info`
   - Retrieves device information

### 16. `test_app_info`
   - Retrieves application version

### 17. `test_coordinates`
   - Clicks on an element based on coordinates

## Running the Tests
To execute all test cases, run:
```sh
python -m unittest test_script.py
```

## Cleanup
Each test:
- Starts the app in `setUp`
- Stops and clears the app in `tearDown`

After all tests:
- Turns off the screen

## Notes
- Ensure the correct `resourceId` and text values match your app.
- Some tests may require UI adjustments depending on screen resolution and element positioning.
- If running on multiple devices, use `uiautomator2.connect('<device_serial>')` to specify the target device.

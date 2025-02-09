import unittest
import uiautomator2 as u2
import time

class TestAppUI(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
       cls.d = u2.connect()
       cls.d.implicitly_wait(10)
       cls.package_name = "com.example.app"
       
   def setUp(self):
       self.d.screen_on()
       self.d.unlock()
       self.d.app_start(self.package_name)
       time.sleep(2)
   
   def test_login(self):
       self.d(resourceId="username").send_keys("test_user")
       self.d(resourceId="password").send_keys("test_pass")
       self.d(resourceId="login_button").click()
       
       self.assertTrue(self.d(text="Welcome").exists(timeout=5))
   
   def test_navigation(self):
       self.d(text="Menu").click()
       self.d(text="Settings").click()
       self.assertTrue(self.d(text="Settings Page").exists)
       
       self.d(text="Profile").click() 
       self.assertTrue(self.d(text="Profile Page").exists)
   
   def test_form_input(self):
       self.d(text="Form").click()
       
       self.d(resourceId="name").send_keys("Test Name")
       self.d(resourceId="email").send_keys("test@email.com")
       self.d(resourceId="submit").click()
       
       self.assertTrue(self.d(text="Form Submitted").exists)
   
   def test_scroll_and_click(self):
       self.d(scrollable=True).scroll.to(text="Target Item")
       self.d(text="Target Item").click()
       self.assertTrue(self.d(text="Item Details").exists)
   
   def test_swipe(self):
       self.d.swipe(300, 800, 300, 200)
       self.assertTrue(self.d(text="New Content").exists)
       
       self.d.swipe_ext("left")
       self.assertTrue(self.d(text="Next Page").exists)
   
   def test_image_match(self):
       image_path = "test_image.png"
       self.assertTrue(self.d.image.match(image_path))
   
   def test_toast(self):
       self.d(resourceId="show_toast").click()
       toast = self.d.toast.get_message()
       self.assertEqual(toast, "Expected Toast Message")
   
   def test_permission_dialog(self):
       self.d(text="Request Permission").click()
       if self.d(text="Allow").exists(timeout=3):
           self.d(text="Allow").click()
       self.assertTrue(self.d(text="Permission Granted").exists)
   
   def test_wait_and_click(self):
       self.d(text="Load Data").click()
       self.d.xpath('//*[@text="Data Ready"]').wait(timeout=10.0)
       self.d(text="Process").click()
       self.assertTrue(self.d(text="Processing Complete").exists)
   
   def test_multiple_elements(self):
       elements = self.d(className="android.widget.Button")
       self.assertEqual(len(elements), 3)
       
       for element in elements:
           self.assertTrue(element.exists)
           
   def test_custom_selector(self):
       elem = self.d.xpath('//android.widget.Button[@content-desc="Custom Button"]')
       self.assertTrue(elem.exists)
       elem.click()

   def test_gesture(self):
    self.d.gesture((100, 200), (300, 200), (300, 400))
    self.assertTrue(self.d(text="Gesture Detected").exists)

   def test_press_key(self):
        self.d.press("home")
        self.d.press("back")
        self.d.press("recent")

   def test_screenshot(self):
        self.d.screenshot("test.jpg")

   def test_device_info(self):
        info = self.d.info
        self.assertIsNotNone(info['displayWidth'])
        self.assertIsNotNone(info['displayHeight'])

   def test_app_info(self):
        info = self.d.app_info(self.package_name)
        self.assertIsNotNone(info['versionName'])
       
   def test_coordinates(self):
       x, y = self.d(text="Target").center()
       self.d.click(x, y)
       self.assertTrue(self.d(text="Clicked").exists)
   
   def tearDown(self):
       self.d.app_stop(self.package_name)
       self.d.app_clear(self.package_name)
   
   @classmethod
   def tearDownClass(cls):
       cls.d.screen_off()

if __name__ == '__main__':
   unittest.main()
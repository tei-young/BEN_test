from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# troubleshotting-Initialize Chrome driver with webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://13.209.85.69/")

# Test 1: Username less than 5 characters
def test_short_username():
   username = driver.find_element(By.ID, "username")
   password = driver.find_element(By.ID, "password")
   email = driver.find_element(By.ID, "email")
   submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
   
   # Input test data
   username.send_keys("test")  # 4 characters
   password.send_keys("test12345")
   email.send_keys("test@test.com")
   # Submit button
   submit.click()
   
   # Check alert text (wait 2 seconds)
   sleep(2)
   alert = driver.switch_to.alert
   assert "Username must be at least 5 characters." in alert.text
   alert.accept()

# Test 2: Valid registration form
def test_valid_registration():
   username = driver.find_element(By.ID, "username")
   password = driver.find_element(By.ID, "password")
   email = driver.find_element(By.ID, "email")
   submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
   
   # Input test data
   username.send_keys("tester123")  # 8 characters
   password.send_keys("test12345")  # 9 characters
   email.send_keys("test@test.com")
   # Submit button
   submit.click()
   sleep(2)  # Wait to check result

# Test 3: Email format validation
def test_invalid_email():
   username = driver.find_element(By.ID, "username")
   password = driver.find_element(By.ID, "password")
   email = driver.find_element(By.ID, "email")
   submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
   
   # Input test data
   username.send_keys("tester123")
   password.send_keys("test12345")
   email.send_keys("testtest.com")  # Email without @
   # Submit button
   submit.click()
   
   # Check alert text
   sleep(2)
   alert = driver.switch_to.alert
   assert "Please enter a valid email." in alert.text
   alert.accept()

try:
   # Run tests
   print("Running Test 1: Username length validation [PASS]")
   test_short_username()
   
   print("Running Test 2: Valid case validation [PASS]")
   test_valid_registration()
   
   print("Running Test 3: Email format validation [PASS]")
   test_invalid_email()
   
   print("Tests completed")

except Exception as e:
   print(f"Error occurred during test: {str(e)}")

finally:
   # Close browser
   driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pathlib import Path

# 1. Update this path to match your exact HTML file location!
PROJECT_DIR = Path(__file__).resolve().parent
HTML_FILE_PATH = (PROJECT_DIR / "registration.html").as_uri()

# This dictionary will store the final results of our tests
test_results = {}

def check_field_validity(driver, element_id):
    """Helper function to ask the browser if a specific field is valid."""
    element = driver.find_element(By.ID, element_id)
    is_valid = driver.execute_script("return arguments[0].checkValidity();", element)
    error_message = driver.execute_script("return arguments[0].validationMessage;", element)
    return is_valid, error_message

def run_tests():
    # Start the Chrome Browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # =========================================================================
        # TEST CASE 1: Check Empty Mandatory Fields
        # =========================================================================
        print("Running Test 1: Checking empty mandatory fields...")
        driver.get(HTML_FILE_PATH)
        
        # Click submit on an empty form to trigger mandatory errors
        driver.find_element(By.CSS_SELECTOR, ".submit-btn").click()
        
        # Track errors on mandatory fields
        fn_valid, fn_msg = check_field_validity(driver, "firstName")
        email_valid, email_msg = check_field_validity(driver, "email")
        gender_valid, gender_msg = check_field_validity(driver, "gender")
        
        if not fn_valid and not email_valid and not gender_valid:
            test_results["Test 1: Empty Mandatory Fields Blocked"] = f"PASSED (Tracked Message: '{fn_msg}')"
        else:
            test_results["Test 1: Empty Mandatory Fields Blocked"] = "FAILED (Browser allowed blank fields)"

        time.sleep(1)

        # =========================================================================
        # TEST CASE 2: Check Wrong Email Format
        # =========================================================================
        print("Running Test 2: Checking bad email validation...")
        driver.get(HTML_FILE_PATH)
        
        driver.find_element(By.ID, "firstName").send_keys("Alex")
        driver.find_element(By.ID, "email").send_keys("not-an-email") # Bad format
        Select(driver.find_element(By.ID, "gender")).select_by_visible_text("Male")
        driver.find_element(By.CSS_SELECTOR, ".submit-btn").click()
        
        email_valid, email_msg = check_field_validity(driver, "email")
        if not email_valid:
            test_results["Test 2: Bad Email Format Blocked"] = f"PASSED (Tracked Message: '{email_msg}')"
        else:
            test_results["Test 2: Bad Email Format Blocked"] = "FAILED (Browser accepted bad email)"

        time.sleep(1)

        # =========================================================================
        # TEST CASE 3: Check Invalid Mobile Number Pattern
        # =========================================================================
        print("Running Test 3: Checking bad mobile phone format...")
        driver.get(HTML_FILE_PATH)
        
        driver.find_element(By.ID, "firstName").send_keys("Alex")
        driver.find_element(By.ID, "email").send_keys("alex@example.com")
        Select(driver.find_element(By.ID, "gender")).select_by_visible_text("Male")
        
        # Typing letters and short numbers which breaks the 10-15 digit pattern rule
        driver.find_element(By.ID, "mobile").send_keys("abc1234") 
        driver.find_element(By.CSS_SELECTOR, ".submit-btn").click()
        
        mobile_valid, mobile_msg = check_field_validity(driver, "mobile")
        if not mobile_valid:
            test_results["Test 3: Bad Mobile Pattern Blocked"] = f"PASSED (Tracked Message: '{mobile_msg}')"
        else:
            test_results["Test 3: Bad Mobile Pattern Blocked"] = "FAILED (Browser accepted bad mobile structure)"

        time.sleep(1)

        # =========================================================================
        # TEST CASE 4: Clean Success Submission
        # =========================================================================
        print("Running Test 4: Checking valid perfect data submission...")
        driver.get(HTML_FILE_PATH)
        
        driver.find_element(By.ID, "firstName").send_keys("Bob")
        driver.find_element(By.ID, "lastName").send_keys("Smith")
        driver.find_element(By.ID, "email").send_keys("bob.smith@example.com")
        driver.find_element(By.ID, "mobile").send_keys("98765432101")
        Select(driver.find_element(By.ID, "gender")).select_by_visible_text("Female")
        driver.find_element(By.ID, "dob").send_keys("1990-12-25")
        
        # Verify all elements are happy before clicking submit
        fn_v, _ = check_field_validity(driver, "firstName")
        em_v, _ = check_field_validity(driver, "email")
        gn_v, _ = check_field_validity(driver, "gender")
        mb_v, _ = check_field_validity(driver, "mobile")
        
        if fn_v and em_v and gn_v and mb_v:
            driver.find_element(By.CSS_SELECTOR, ".submit-btn").click()
            test_results["Test 4: Clean Data Form Submission"] = "PASSED (All form data verified valid)"
        else:
            test_results["Test 4: Clean Data Form Submission"] = "FAILED (Valid data was flagged as wrong)"

        time.sleep(2)

    except Exception as e:
        print(f"An unexpected error interrupted the suite: {e}")
        
    finally:
        # Close the testing browser window
        driver.quit()

# 4. Execution entry point to run and print results
if __name__ == "__main__":
    run_tests()
    
    # Print out the final tracking report to the console
    print("\n" + "="*60)
    print("             FINAL REGISTRATION TEST TRACKING REPORT             ")
    print("="*60)
    for test_name, result in test_results.items():
        print(f"-> {test_name}: \n   {result}\n")
    print("="*60)
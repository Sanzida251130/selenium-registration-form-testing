import csv
import os
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


PROJECT_DIR = Path(__file__).resolve().parent

HTML_FILE_PATH = (PROJECT_DIR / "registration.html").as_uri()
CSV_INPUT_FILE = PROJECT_DIR / "registration_test_data.csv"
CSV_OUTPUT_FILE = PROJECT_DIR / "registration_test_results.csv"

def generate_csv_if_not_exists():
    """Generates 20 complete test cases covering equivalence classes and boundary values."""
    headers = [
        "TestID", "TestDescription", "FirstName", "LastName",
        "Email", "Mobile", "Gender", "DOB", "ExpectedResult"
    ]
    
    data = [ 
        # Mandatory Field Checks (TC01 - TC04)
        ["TC01", "All Fields Empty", "", "", "", "", "", "", "INVALID_MANDATORY"], 
        ["TC02", "Missing Mandatory First Name", "", "Doe", "john@example.com", "01712345678", "Male", "1995-01-01", "INVALID_MANDATORY"], 
        ["TC03", "Missing Mandatory Email", "John", "Doe", "", "01712345678", "Male", "1995-01-01", "INVALID_MANDATORY"], 
        ["TC04", "Missing Mandatory Gender", "John", "Doe", "john@example.com", "01712345678", "", "1995-01-01", "INVALID_MANDATORY"], 
        
        # Email Validation Checks (TC05 - TC08)
        ["TC05", "Email Missing @ Symbol", "Alex", "Doe", "not-an-email", "01712345678", "Male", "1995-01-01", "INVALID_EMAIL"], 
        ["TC06", "Email Missing Domain", "Alex", "Doe", "alex@", "01712345678", "Male", "1995-01-01", "INVALID_EMAIL"], 
        ["TC07", "Email Missing Username", "Alex", "Doe", "@example.com", "01712345678", "Male", "1995-01-01", "INVALID_EMAIL"], 
        ["TC08", "Email Double @ Symbol", "Alex", "Doe", "alex@@example.com", "01712345678", "Male", "1995-01-01", "INVALID_EMAIL"], 

        # Mobile Pattern & Boundary Checks (TC09 - TC14)
        ["TC09", "Mobile Contain Alphabets", "Alex", "Doe", "alex@example.com", "abc12345678", "Male", "1995-01-01", "INVALID_MOBILE"], 
        ["TC10", "Mobile Too Short (9 Digits)", "Alex", "Doe", "alex@example.com", "123456789", "Male", "1995-01-01", "INVALID_MOBILE"], 
        ["TC11", "Mobile Too Long (16 Digits)", "Alex", "Doe", "alex@example.com", "1234567890123456", "Male", "1995-01-01", "INVALID_MOBILE"], 
        ["TC12", "Mobile Lower Boundary (10 Digits)", "Alex", "Doe", "alex@example.com", "1234567890", "Male", "1995-01-01", "VALID"], 
        ["TC13", "Mobile Upper Boundary (15 Digits)", "Alex", "Doe", "alex@example.com", "123456789012345", "Male", "1995-01-01", "VALID"], 
        ["TC14", "Mobile Special Characters", "Alex", "Doe", "alex@example.com", "017123+4567", "Male", "1995-01-01", "INVALID_MOBILE"], 

        # Optional Field Variations & Edge Cases (TC15 - TC17)
        ["TC15", "Valid Without Optional Last Name", "Sarah", "", "sarah@example.com", "01812345678", "Female", "1998-05-20", "VALID"], 
        ["TC16", "Valid Without Optional DOB", "Michael", "Scott", "mscott@example.com", "01912345678", "Male", "", "VALID"], 
        ["TC17", "Valid Minimum Required Only", "Jim", "", "jim@example.com", "", "Male", "", "VALID"], 

        # Clean Success Cases (TC18 - TC20)
        ["TC18", "Clean Valid Submission Male", "Bob", "Smith", "bob.smith@example.com", "98765432101", "Male", "1990-12-25", "VALID"], 
        ["TC19", "Clean Valid Submission Female", "Jane", "Doe", "jane.doe@example.com", "01711112222", "Female", "2000-01-01", "VALID"], 
        ["TC20", "Valid Complex Subdomain Email", "Alice", "Wonder", "alice@mail.co.uk", "01512345678", "Female", "1992-08-14", "VALID"] 
    ] 
 
    # Always overwrite or recreate with the new 20 test cases
    with open(CSV_INPUT_FILE, mode="w", newline="", encoding="utf-8") as f: 
        writer = csv.writer(f) 
        writer.writerow(headers) 
        writer.writerows(data) 
    print(f"Dataset generated with 20 test cases at: {CSV_INPUT_FILE}") 

def check_field_validity(driver, element_id):
    """Helper function to evaluate HTML5 constraint validation using JavaScript."""
    element = driver.find_element(By.ID, element_id)
    is_valid = driver.execute_script("return arguments[0].checkValidity();", element)
    error_message = driver.execute_script("return arguments[0].validationMessage;", element)
    return is_valid, error_message

def run_csv_driven_tests():
    generate_csv_if_not_exists()

    test_rows = [] 
    with open(CSV_INPUT_FILE, mode="r", encoding="utf-8") as f: 
        reader = csv.DictReader(f) 
        for row in reader: 
            test_rows.append(row) 
            
    results_data = [] 
    driver = webdriver.Chrome() 
    driver.maximize_window() 
 
    try: 
        for row in test_rows: 
            test_id = row.get("TestID", "") 
            desc = row.get("TestDescription", "") 
            first_name = row.get("FirstName", "") 
            last_name = row.get("LastName", "") 
            email = row.get("Email", "") 
            mobile = row.get("Mobile", "") 
            gender = row.get("Gender", "") 
            dob = row.get("DOB", "") 
            expected_result = row.get("ExpectedResult", "") 
            
            print(f"Running {test_id}: {desc}...") 
            driver.get(HTML_FILE_PATH) 
            time.sleep(0.5) 
            
            # Input data fields
            if first_name: 
                driver.find_element(By.ID, "firstName").send_keys(first_name) 
            if last_name: 
                driver.find_element(By.ID, "lastName").send_keys(last_name) 
            if email: 
                driver.find_element(By.ID, "email").send_keys(email) 
            if mobile: 
                driver.find_element(By.ID, "mobile").send_keys(mobile) 
            if gender: 
                gender_select = Select(driver.find_element(By.ID, "gender")) 
                gender_select.select_by_visible_text(gender) 
            if dob: 
                driver.find_element(By.ID, "dob").send_keys(dob) 
                
            # Verify field-level validations
            fn_v, fn_msg = check_field_validity(driver, "firstName") 
            em_v, em_msg = check_field_validity(driver, "email") 
            gn_v, gn_msg = check_field_validity(driver, "gender") 
            mb_v, mb_msg = check_field_validity(driver, "mobile") 
            
            # Click submit button
            driver.find_element(By.CSS_SELECTOR, ".submit-btn").click() 
            time.sleep(0.5) 
            
            actual_status = "" 
            val_msg = "" 
            test_result = "FAILED" 
            
            # Evaluate test logic
            if expected_result == "INVALID_MANDATORY": 
                if not fn_v or not em_v or not gn_v: 
                    actual_status = "BLOCKED_MANDATORY_MISSING" 
                    val_msg = fn_msg or em_msg or gn_msg 
                    test_result = "PASSED" 
                else: 
                    actual_status = "ALLOWED_EMPTY_SUBMISSION" 
                    val_msg = "No validation error triggered" 
                    test_result = "FAILED" 
                    
            elif expected_result == "INVALID_EMAIL": 
                if not em_v: 
                    actual_status = "BLOCKED_INVALID_EMAIL" 
                    val_msg = em_msg 
                    test_result = "PASSED" 
                else: 
                    actual_status = "ACCEPTED_INVALID_EMAIL" 
                    val_msg = "Email validation failed to trigger" 
                    test_result = "FAILED" 
                    
            elif expected_result == "INVALID_MOBILE": 
                if not mb_v: 
                    actual_status = "BLOCKED_INVALID_MOBILE" 
                    val_msg = mb_msg 
                    test_result = "PASSED" 
                else: 
                    actual_status = "ACCEPTED_INVALID_MOBILE" 
                    val_msg = "Mobile pattern validation failed to trigger" 
                    test_result = "FAILED" 
                    
            elif expected_result == "VALID": 
                if fn_v and em_v and gn_v and mb_v: 
                    actual_status = "FORM_SUBMITTED_SUCCESSFULLY" 
                    val_msg = "All fields valid" 
                    test_result = "PASSED" 
                else: 
                    actual_status = "VALID_DATA_BLOCKED" 
                    val_msg = fn_msg or em_msg or gn_msg or mb_msg 
                    test_result = "FAILED" 
            
            row_output = dict(row) 
            row_output["ActualStatus"] = actual_status 
            row_output["ValidationMessage"] = val_msg 
            row_output["TestResult"] = test_result 
            results_data.append(row_output) 
            
            print(f" -> Result: {test_result} | Status: {actual_status}") 

    except Exception as e: 
        print(f"Error during execution: {e}") 
        
    finally: 
        driver.quit() 
        
    # Write output to CSV file
    if results_data: 
        output_headers = list(test_rows[0].keys()) + ["ActualStatus", "ValidationMessage", "TestResult"] 
        with open(CSV_OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as f: 
            writer = csv.DictWriter(f, fieldnames=output_headers) 
            writer.writeheader() 
            writer.writerows(results_data) 
            
        print("\n" + "="*70) 
        print(f"Test Execution Completed! Results saved to CSV: {CSV_OUTPUT_FILE}") 
        print("="*70) 

if __name__ == "__main__":
    run_csv_driven_tests()
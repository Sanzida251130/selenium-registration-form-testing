from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pathlib import Path

# ============================================================
# REGISTRATION HTML FILE
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent
HTML_FILE_PATH = (PROJECT_DIR / "registration.html").as_uri()

# ============================================================
# START CHROME
# ============================================================

driver = webdriver.Chrome()

try:

    # Open registration form
    driver.get(HTML_FILE_PATH)

    driver.maximize_window()


    # ========================================================
    # LOCATE FORM ELEMENTS
    # ========================================================

    print("Locating form elements...")

    first_name_input = driver.find_element(
        By.ID, "firstName"
    )

    last_name_input = driver.find_element(
        By.ID, "lastName"
    )

    email_input = driver.find_element(
        By.ID, "email"
    )

    mobile_input = driver.find_element(
        By.ID, "mobile"
    )

    gender_dropdown = driver.find_element(
        By.ID, "gender"
    )

    dob_input = driver.find_element(
        By.ID, "dob"
    )

    submit_button = driver.find_element(
        By.CSS_SELECTOR, ".submit-btn"
    )


    print("All form elements found successfully!")


    # ========================================================
    # FILL FORM
    # ========================================================

    print("Filling out registration form...")

    first_name_input.send_keys("Sumaya")

    last_name_input.send_keys("Sanzida")

    email_input.send_keys("sumayasanzida@gmail.com")

    mobile_input.send_keys("01678042849")


    # ========================================================
    # SELECT GENDER
    # ========================================================

    print("Selecting gender...")

    select_gender = Select(gender_dropdown)

    select_gender.select_by_visible_text("Female")


    # ========================================================
    # DATE OF BIRTH
    # ========================================================

    print("Setting Date of Birth...")

    dob_input.send_keys("1995-05-15")


    # ========================================================
    # SCREENSHOT PAUSE
    # ========================================================

    print("\n============================================")
    print("FORM IS NOW FILLED.")
    print("Take your screenshot manually.")
    print("============================================")

    input("\nPress ENTER after taking the screenshot...")


    # ========================================================
    # SUBMIT
    # ========================================================

    print("Submitting the registration form...")

    submit_button.click()


    print("\nRegistration form submitted.")

    input(
        "\nPress ENTER to close the browser..."
    )


except Exception as e:

    print(
        f"An error occurred during testing: {e}"
    )

finally:

    driver.quit()


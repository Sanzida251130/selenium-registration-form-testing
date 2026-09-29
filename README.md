# Selenium Registration Form Testing

A **data-driven web form testing project** using Python and Selenium WebDriver. The project automates the testing of a registration form and validates both positive and negative input scenarios using an external CSV test dataset.

The project was developed as part of a Software Testing / Software Testing Methodology laboratory exercise.

---

## 📌 Project Overview

This project demonstrates automated testing of a web-based registration form using **Selenium WebDriver with Python**.

Instead of hardcoding test data inside the automation script, the project uses an external CSV file containing **20 different test cases**. The Selenium script reads each test case, enters the corresponding data into the registration form, validates the result, and stores the execution results in a separate CSV file.

The project covers:

- Mandatory field validation
- Email format validation
- Mobile number format validation
- Boundary value testing
- Valid registration scenarios
- Optional field testing
- Data-driven test execution
- Automated pass/fail result tracking

---

## 🎯 Objectives

The main objectives of this project are:

1. Automate registration form testing using Selenium WebDriver.
2. Validate individual form fields using browser-based HTML5 validation.
3. Separate test logic from test data using a CSV file.
4. Execute multiple test scenarios using a single reusable test script.
5. Test both valid and invalid input combinations.
6. Perform boundary-value testing for mobile numbers.
7. Automatically record validation messages and test results.
8. Generate a structured CSV report for test traceability.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Test automation programming |
| **Selenium WebDriver** | Browser automation and form testing |
| **HTML5** | Registration form |
| **CSS3** | Form styling |
| **Google Chrome** | Browser used for testing |
| **CSV** | Test data and result storage |
| **VS Code** | Development environment |

---

## 📂 Project Structure

```text
selenium-registration-form-testing/
│
├── registration.html
│
├── reg_test.py
├── reg_all_error_chk.py
├── reg_all_error_in_out.py
│
├── registration_test_data.csv
├── registration_test_results.csv
│
├── screenshots/
│
├── README.md
└── .gitignore
```

### Main Files

**`registration.html`**

The registration form being tested.

**`reg_test.py`**

Performs basic Selenium automation by opening the registration form, locating form elements, entering data, selecting gender, setting the date of birth, and submitting the form.

**`reg_all_error_chk.py`**

Runs predefined validation scenarios and checks browser validation behavior using Selenium.

**`reg_all_error_in_out.py`**

The main data-driven testing script. It reads the test cases from `registration_test_data.csv`, executes them against the registration form, compares actual behavior with the expected result, and writes the final results to `registration_test_results.csv`.

**`registration_test_data.csv`**

Contains the input dataset of 20 test cases.

**`registration_test_results.csv`**

Contains the automatically generated test execution results, including actual status, validation messages, and pass/fail results.

---

## 🧪 Test Coverage

The project contains **20 data-driven test cases** covering different categories of input validation.

### Mandatory Field Tests

- Empty mandatory fields
- Missing first name
- Missing email
- Missing gender

### Email Validation Tests

- Email without `@`
- Email without a valid domain
- Email without a username
- Other malformed email formats

### Mobile Number Validation

- Alphabetic characters
- Too few digits
- Too many digits
- Special characters
- Spaces
- Valid mobile numbers

### Boundary Value Tests

The mobile number field accepts **10 to 15 digits**.

Therefore, boundary cases were included to test:

```text
9 digits   → Invalid
10 digits  → Valid
15 digits  → Valid
16 digits  → Invalid
```

### Valid Registration Tests

The test dataset also includes successful registration scenarios with:

- Male and female selections
- Optional last name omitted
- Optional mobile number omitted
- Optional date of birth omitted
- Complete valid registration data

---

## 📊 Data-Driven Testing

The main testing script separates **test logic** from **test data**.

The test cases are stored in:

```text
registration_test_data.csv
```

Each row represents one test scenario.

Example:

```csv
TestID,TestDescription,FirstName,LastName,Email,Mobile,Gender,DOB,ExpectedResult
TC05,Invalid Email No At Symbol,Alex,Doe,alex.example.com,01712345678,Male,1995-01-01,INVALID_EMAIL
```

The same Selenium automation logic can therefore execute multiple test scenarios without modifying the Python code.

---

## 🔍 Validation Approach

The project uses Selenium to access the browser's built-in HTML5 validation state.

The automation checks:

```text
checkValidity()
```

and retrieves:

```text
validationMessage
```

This allows the script to determine whether a field is valid and capture the browser's validation message when invalid input is supplied.

---

## 📈 Test Results

All **20 data-driven test cases passed successfully** during the documented test execution.

The result file contains information such as:

```text
TestID
TestDescription
ExpectedResult
ActualStatus
ValidationMessage
TestResult
```

Example result statuses include:

```text
BLOCKED_MANDATORY_MISSING
BLOCKED_INVALID_EMAIL
BLOCKED_INVALID_MOBILE
FORM_SUBMITTED_SUCCESSFULLY
```

All executed scenarios were recorded as:

```text
PASSED
```

The complete execution results are stored in:

```text
registration_test_results.csv
```

---

## 📸 Screenshots

The project includes screenshots documenting:

- Initial registration form
- Filled registration form
- Selenium automation process
- Mandatory field validation
- Invalid email validation
- Invalid mobile validation
- Successful registration
- Data-driven test execution
- Final test results
- Input test dataset
- Generated output results

Screenshots are included to provide visual evidence of the testing process.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Sanzida251130/selenium-registration-form-testing.git
```

Navigate into the project:

```bash
cd selenium-registration-form-testing
```

### 2. Install Selenium

Make sure Python is installed, then run:

```bash
pip install selenium
```

### 3. Open the project

Open the project folder in VS Code or another Python-compatible editor.

### 4. Run the basic Selenium test

```bash
python reg_test.py
```

### 5. Run the validation test suite

```bash
python reg_all_error_chk.py
```

### 6. Run the data-driven test suite

```bash
python reg_all_error_in_out.py
```

The data-driven script reads:

```text
registration_test_data.csv
```

and generates:

```text
registration_test_results.csv
```

---

## 🧠 Testing Concepts Demonstrated

This project provides practical experience with:

- Functional testing
- Automated testing
- Positive testing
- Negative testing
- Boundary value analysis
- Data-driven testing
- Form validation
- Browser automation
- Test result tracking
- CSV-based test management
- Regression-oriented test execution

---

## 📋 Test Execution Summary

| Category | Result |
|---|---|
| Total Test Cases | 20 |
| Passed | 20 |
| Failed | 0 |
| Test Automation | Selenium WebDriver |
| Test Data | CSV |
| Result Storage | CSV |
| Browser | Google Chrome |

---

## 🚀 Future Improvements

Possible future improvements include:

- Implementing the **Page Object Model (POM)**
- Using **pytest** for test organization
- Adding automated HTML test reports
- Adding screenshots automatically for failed tests
- Adding explicit waits instead of fixed delays
- Running tests through GitHub Actions CI/CD
- Supporting multiple browsers
- Adding more advanced test data generation

---

## 👨‍💻 Author

**[Sumaya Sanzida**

Software Testing / QA Automation Project

---

## 📄 Academic Reference

This project was developed as part of a Software Testing laboratory exercise focused on Selenium-based registration form validation and data-driven testing.
# PART 1

## Test Scenarios and Cases

### Scenario 0: Required Field Validation
**Description**: All required fields should not be empty.

| ID | Test Case | Steps | Expected Result | Priority |
|----|-----------|-------|-----------------|----------|
| 0-1 | Empty Username Validation | 1. Leave username field empty<br>2. Click Register button | Toast popup displays "Username must be at least 5 characters." | High |
| 0-2 | Empty Password Validation | 1. Leave password field empty<br>2. Click Register button | Toast popup displays "Password must be at least 8 characters." | High |
| 0-3 | Empty Email Validation | 1. Leave email field empty<br>2. Click Register button | Toast popup displays "Please enter a valid email." | High |

### Scenario 1: Username Field Validation
**Description**: Username field should accept alphanumeric characters and special symbols.

| ID | Test Case | Steps | Expected Result | Priority |
|----|-----------|-------|-----------------|----------|
| 1-1 | Username Minimum Length Validation | 1. Enter username with less than 5 characters<br>2. Click Register button | Toast popup displays "Username must be at least 5 characters." | High |
| 1-2 | Valid Username Registration | 1. Enter username with 5 or more characters<br>2. Click Register button | Form accepts the username | High |

### Scenario 2: Password Field Validation
**Description**: Password field should accept alphanumeric characters and special symbols.

| ID | Test Case | Steps | Expected Result | Priority |
|----|-----------|-------|-----------------|----------|
| 2-1 | Password Minimum Length Validation | 1. Enter password with less than 8 characters<br>2. Click Register button | Toast popup displays "Password must be at least 8 characters." | High |
| 2-2 | Valid Password Registration | 1. Enter password with 8 or more characters<br>2. Click Register button | Form accepts the password | High |

### Scenario 3: Email Field Validation
**Description**: Email field should accept alphanumeric characters and special symbols.

| ID | Test Case | Steps | Expected Result | Priority |
|----|-----------|-------|-----------------|----------|
| 3-1 | Invalid Email Format Validation | 1. Enter email without '@' symbol<br>2. Click Register button | Toast popup displays "Please enter a valid email." | High |
| 3-2 | Valid Email Registration | 1. Enter valid email (containing '@' symbol)<br>2. Click Register button | Form accepts the email | High |

### Scenario 4: Newsletter Subscription Checkbox
**Description**: Newsletter subscription checkbox should toggle between checked and unchecked states.

| ID | Test Case | Steps | Expected Result | Priority |
|----|-----------|-------|-----------------|----------|
| 4-1 | Checkbox Check Action | 1. Click unchecked newsletter checkbox | Checkbox changes to checked state | Medium |
| 4-2 | Default Checkbox State | 1. Load registration form | Checkbox is in unchecked state by default | Medium |
| 4-3 | Checkbox Uncheck Action | 1. Click checked newsletter checkbox | Checkbox changes to unchecked state | Medium |

## Test Environment
- Browser: Chrome (latest version)
- Platform: Windows OS
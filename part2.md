# PART 2

## Bug Report

## Bug ID: BUG-01
### Title: Poor User Experience Due to Missing Input Requirements

**Severity**: Medium  
**Priority**: High  

### Description
The registration form lacks upfront display of input requirements for Username, Password, and Email fields. Users must go through trial and error to understand the correct input format.

### Steps to Reproduce
1. Navigate to registration page (http://13.209.85.69/)
2. Check Username input field
3. Check Password input field
4. Check Email input field

### Actual results
- Input requirements are only shown through error messages after clicking the Register button
- No prior indication that Username requires 5+ characters, Password requires 8+ characters, and Email must include '@'

### Expected
- Clear display of input requirements below each field:
 - Username: "Must be at least 5 characters"
 - Password: "Must be at least 8 characters"
 - Email: "Please enter a valid email address"

### Impact
- Degraded user experience
- Increased registration time due to unnecessary trial and error

## Bug ID: BUG-002
### Title: Security Vulnerability Due to Weak Password Requirements

**Severity**: High  
**Priority**: High  

### Description
The password field only enforces minimum length (8 characters) with no additional security requirements, allowing creation of weak passwords.

### Steps to Reproduce
1. Navigate to registration page (http://13.209.85.69/)
2. Enter "12345678" in Password field (8-digit numeric password)
3. Fill other fields correctly and click Register

### Actual results
- Accepts simple passwords
- No requirements for special characters or letter case combinations
- Only validates password length

### Expected
Password should require:
- Minimum 8 characters
- At least one uppercase letter
- At least one special character
- At least one number

### Impact
- Increased account security vulnerability
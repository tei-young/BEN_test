# PART 4

## Objectives
* Verify the system can handle 10,000 concurrent users 
* Check response time stays acceptable under load
* Identify the maximum load handling
* Test signup/login flows under peak load

## Tools
### Selected Tool: Apache JMeter
Reasons for selection:
* Free, open-source tool
* Widely used in the industry 
* GUI interface makes it easier to learn

## Test Cases
### Case 1: Login Response Time Test
* Number of Threads: 100 concurrent users (fixed number)
* Steps:
  * Login with test account
  * Measure response time
* Goal: Check if response time stays under 2 seconds

### Case 2: Gradual Load Test for Sign Up
* Number of Threads: 
  * Start with 10 users
  * Add 10 users every 2 minutes
  * Maximum 200 users
* Steps:
  * Create new accounts with test data
  * Record success/failure rates
* Goal: Find the point where system starts showing stress

### Case 3: Stability Test
* Number of Threads: 50 concurrent users (fixed number)
* Steps:
  * Alternate between login and logout
  * 30 second pause between actions
* Goal: Check if system remains stable under consistent moderate load

## Metrics
* Average Response Time
* Successful Transactions per Second

## Test Environment
### AWS Configuration
* Region: ap-northeast-2 (Seoul)
* Instance Type: t2.large (may need adjustment)
* Auto-scaling: Disabled during initial tests

### Test Client Setup
* JMeter installed on local machine
* Direct internet connection (no proxy)
* Windows 10, 11 OS

## Analysis
### Basic Analysis Steps:
1. Record baseline metrics with 100 users
2. Compare metrics as user load increases
3. Look for response times above 3 seconds
4. Look for sudden drops in transactions per second
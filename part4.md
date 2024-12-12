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
### Case 1: Performance Test
* Number of Threads: Start with 100 users(Gradually increase to 1,000 users)
* Steps:
  * Basic login/logout operations
  * Measure response time
* Goal: Baseline performance metrics

### Case 2: Peak Load Test
* Number of Threads: 
  * Start with 1,000 users
  * Increase by 1,000 every 5 minutes
  * Final target: 10,000 users
* Steps:
  * 70% users perform login
  * 30% users perform signup
* Goal: Verify system handles required 10,000 concurrent users

### Case 3: Extended Peak Load Test(peak time)
* Number of Threads:
  * Start with 1,000 users
  * Increase by 2,000 every 10 minutes
  * Final target: 10,000 users maintained for 30 minutes(peak time)
* Steps:
   * Mix of operations:
    * 40% login
    * 40% signup
    * 20% repeated login-logout
  * Record error patterns at each load level
* Goal: Analyze system behavior under various peak time

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
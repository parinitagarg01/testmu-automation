# TestMu AI Automation Assignment

Hi 👋

This repository contains my solution for the TestMu AI Customer Engineering Intern assignment.

## What I have implemented

I created two automated test cases using Python and Playwright:

1. Search for an iPhone on Amazon, print its price, and add it to the cart  
2. Search for a Samsung Galaxy device, print its price, and add it to the cart  

Both test cases are configured to run in parallel using pytest.

## Tech Stack

- Python  
- Playwright  
- Pytest  

## How to run this project

1. Install dependencies:
   pip install playwright pytest pytest-xdist

2. Install browsers:
   playwright install

3. Run the tests:
   pytest

## Features

- Parallel execution using pytest  
- Dynamic product selection (skips ads or unavailable items)  
- Extracts product price and prints it to the console  
- Automates add-to-cart functionality  

## Note

Amazon is a dynamic website, so selectors or behavior may occasionally vary.  
The script is designed to handle common scenarios and works reliably under normal conditions.

## Bonus: LambdaTest Cloud Execution

The test cases were successfully executed on LambdaTest cloud platform using Playwright.


---

Thank you for reviewing my submission!

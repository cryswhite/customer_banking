# customer_banking
Repo for Module 3 assignment

# Overview Comments
This project has been painful but interesting. I have been using 2 different computers (a PC which is so new as to create issue after issue because of OneDrive and my husband's Mac which had the benefit of tons of memory and is a fast computer but is sadly so old that it can't run many of the newer versions I need). With regards to the PC, as of today, I think I have straightened it mostly out and am now saving files only to C: drive. But, alas, I still can't get the scripts to run. As to the Mac, I have ordered one that was built in the last decade, and that should solve those issues. 

That being said, I wasn't clear on how I was supposed to use menu.py, so I used recommendations from ChatGPT to integrate it with customer_banking.py to illustrate the menu options to the user (more on this and other usage of ChatGPT follows).

What I have also learned is how to build my own GPT, named "Crystal's AI Bootcamp Buddy," and Buddy has helped me out quite a bit, explaining the directions, explaining the prompts and supplied code, and helping me troubleshoot. Alongside Buddy, I've been using GitHub Copilot. Unfortunately, they don't always agree, and as I'm just slugging thru this quagmire of information to try to get to the part that actually applies to my reason for joining this program (ethics, governance, applications of AI), well, I can't really gauge which one is more correct. But, since Buddy has a name and is inexhaustible in answering  my questions, I've used Buddy most often, as you will see from this assignment.

I am crediting Buddy with the majority of the work I have provided, and it's his fault for not telling me exactly how to correct the issues. You'd think with billions of dollars of investment, Buddy would be better equipped. But, it does help to level-set my expectations because with its billions of investment and unfathomable hours of training from experts, I don't really have high expectations for my ability to pick this up in a manner of weeks. Fortunately, I see the value of a continued relationship with Buddy, so I'll continue feeding him books I'm reading and other explanatory files. I'll also start using the LMS GPT to see who works best. That being the case, Buddy has a nice image created by DALL-E that makes me like him more.

My final comments are with exception to this intro copy, Buddy actually created the README copy and markdown as well. I thought this would be a great time for him to shine, and, as an executive, it's my job to delegate work to those most capable and with the time to do more of the manual work. I have no desire to become a programmer and have happily spent the past 25 years without feeling such a need. I am essentially auditing this class to understand what is happening with AI, how to apply it within my organization, and what to be mindful of, so that I can continue to make well-researched strategic technology recommendations to solve business challenges.

Between Google, ChatGPT, GitHub Copilot and Python Programming for Dummies, I can't figure out what to fix for "No module named 'customer_banking' or why nothing seems to run correctly. So, please don't feel bad for awarding me poor marks. I have no desire to be a programmer, and I'm not in this program for the certificate. I'm in this, so I can be better informed and provide better recommendations to my employer.

So, with that, I'll let Buddy take it away. 

# Customer Banking System

This project consists of a Python application for a customer banking system. It allows users to calculate and track interest earned on savings and CD accounts. Users can enter their account details, see the interest earned, and view the updated balances after a specified number of months.

## Features

- Calculate interest for savings and CD accounts.
- Update account balances based on interest earned.
- Interactive user prompts for account details.

## Files

- `customer_banking.py`: Main script to run the banking application.
- `savings_account.py`: Contains functionality for savings account operations.
- `cd_account.py`: Manages CD account operations.
- `Account.py`: Defines the `Account` class used by other modules.

## Usage

To use the application, run the `customer_banking.py` file. Follow the on-screen prompts to enter account details and view the calculated results.

```bash
python customer_banking.py

Code Provided by ChatGPT
Several parts of the code were developed with assistance from ChatGPT. This includes:

Savings Account Calculation: Logic to calculate interest for savings accounts and update the balance.

Function: create_savings_account in savings_account.py.
CD Account Calculation: Similar logic for CD accounts.

Function: create_cd_account in cd_account.py.
Main Application Flow: The main script that integrates all components, prompts user input, and displays results.

Script: customer_banking.py.
Debugging Tips: Assistance with debugging issues such as import errors and AttributeError.

Contributions
This project is open to contributions. If you find any bugs or have suggestions for improvement, please feel free to open an issue or submit a pull request.

License
MIT License

Acknowledgments
Thanks to ChatGPT for providing guidance and code snippets.




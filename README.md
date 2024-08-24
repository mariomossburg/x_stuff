Using MacOs with Chrome, kill all open chrome tabs.

Run in local terminal: /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

Go to guest mode, then check connection.
Check: localhost:9222/json to test connection
localhost:9222 should be blank


You will need to download any missing imports to run files
Also, provide sign-in credentials for config file in selenium folder. 

For api folder, you will need to create developer account for and insert tokens.

Adjust arguments for specific criteria 


**To start**
Navigate to main.py inside selenium and start by calling functions from a class. The base URL is vital, and some functions like like.py is set to like a post if it is already clicked into the post.
not from x.com/home 

If encountering errors, try refreshing page or try closing Chrome altogether and rerun: /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
 
Also keep in mind what URL you are running a file from. 









# Selenium Automation with X API Integration

This repository contains a set of automated tasks using Selenium and the X API. The program interacts with X.com and performs specific basic tasks.

## Prerequisites

### Operating System
- **macOS** with **Google Chrome** installed.

### Tools and Libraries
- **Selenium**: For automating browser tasks.
- **X API**: For interacting with X.com (Twitter).
- **Python**: Make sure Python is installed on your system.

### Chrome Setup
To use Chrome with remote debugging enabled, you'll need to run the following command in your local terminal to start Chrome:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

Cancel all other chrome tabs so they do not interfere. 




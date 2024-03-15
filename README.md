# SendMail Project

The SendMail project is designed to notify users via email every time their computer is accessed. This script fetches the computer's name and public IP address, then sends this information to the specified email address. This is particularly useful for monitoring unauthorized access or simply keeping track of when and where your computer is being used.

## Setup Instructions

### Prerequisites

Before setting up the SendMail project, ensure that you have Python installed on your system. This project was developed using Python 3, so it is recommended to use Python 3.x.

Additionally, you must have `pip` installed to manage Python packages.

### Required Python Packages

Install the following Python packages using `pip`:

- `dotenv`: Used for loading environment variables from the `.env` file.
- `requests`: Used to make HTTP requests (in this case, to fetch the public IP address).

You can install these packages by running:

```
pip install python-dotenv requests socket smtplib os time
```

### Setting Up the Environment Variables

1. Create a file named `.env` in the same directory as your `SendMail.py` script.
2. Populate the `.env` file with your email ID, password, and name, as shown below:

```
EMAILID="your_email@gmail.com"
PASSWORD="your_app_specific_password"
NAME="Your Name"
```

### Google App Password

Since this script requires logging in to your email account, it is highly recommended to use an app-specific password, especially if you have two-factor authentication enabled on your Google account.

1. Visit [Google App Passwords](https://myaccount.google.com/apppasswords) and sign in.
2. Under "Select the app and device you want to generate the app password for," choose "Other (Custom name)" and type "startmail".
3. Click "Generate". Google will provide you with a 16-character password.
4. Copy this password to your `.env` file, replacing `your_app_specific_password` with the password you just generated(make sure there is no whitespace between your passwords).

### Setting Up the Task Scheduler

1. Create a batch file named `start.bat` with the following content:

```
@echo off
python SendMail.py
```

Copy Sendmail.py and .env to `C:\Windows\System32`

2. Open Task Scheduler in Windows.
3. Create a new task with the trigger set to "At log on" for any user.
4. For the action, choose "Start a program" and select your `start.bat` file.
5. In the conditions tab, uncheck "Start the task only if the computer is on AC power".
6. Optionally, set "Start only if the following network is available" to any network.
7. Save the task.

### Note

- Ensure that your firewall or antivirus software allows outgoing connections for Python and SMTP traffic.

## Usage

Once everything is set up, the task you created in Task Scheduler will run the `SendMail.py` script every time any user logs onto the computer. An email notification will be sent to the specified email address with details of the login event.




Ensure to replace placeholders (like `your_email@gmail.com`, `your_app_specific_password`, and `Your Name`) with your actual information. The README file is designed to be comprehensive and user-friendly, guiding users through setting up and using the SendMail project without diving into the code specifics.
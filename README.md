
# Drive Social Media Employee Management App

I created this app because there are several steps to creating new employees
and I wanted to expedite the process and remove the human error element from
the process. With this app, new employees get accounts created in Mosyle,
Reftab, and Google Wokspace (including being added to correct OUs and Groups).

This program was written for use by the IT Department and trained secondary
users. Any use outside of this may have terrible consequences and I will not
be help liable for your mistakes. **Use this program at your own risk.**

## Setup

### Libraries

You'll need to ensure that you have pip \(pip3\) installed on your computer
so that you can install the required libraries. If you already have pip installed
go ahead and install the required libraries by running this in your terminal:

`pip3 install -r requirements.txt`

You should receive output letting you know the required libraries have been
installed and are ready for use.

### Keys

In order to user this program, you'll need to configure the appropriate API
keys and passwords that will be used in the program. This includes Reftab,
Mosyle, and Google. Google will require the most setup as it requires you to
have a Google Cloud Project set up and you will need to enable the Google Admin
SDK API, and the Google API Client library for Python - [more information here](https://developers.google.com/admin-sdk/directory/v1/api-lib/python)

## Usage

### New Employee

To add a new employee, run the employeeManagement.py file from your terminal
with the added arguments: new employee

`python employeeManagement.py new employee`

This will initiate the process and create the new user accounts. You will be
given a chance to correct any typographical errors before submitting the
information to the platforms, double check everything is spelled correctly
before submitting or you'll need to go delete the accounts that get created.

### Term Employee

To terminate an employee, run the employeeManagement.py file from your terminal
with the added arguments: term employee

`python employeeManagement.py term employee`

This will initiate the termination process and ask for the appropriate employee
imformation. 

When an employee is terminated \(voluntarily or otherwise\), this app will
expedite the process of locking them out of our systems \(Google\), as well as
update their computer in Reftab and mark it as due immediately, and change the
status label to mark the laptop "Needs to be shipped home". Once the process
has completed, the new password for the ex-employee's Google Workspace account
will be printed to the terminal window.

#### Device List

When using the "Term Employee" option through the GUI, you should now receive a
list of devices which are assigned to the employee. These devices should be 
collected by the terminating manager when the employee is released.

### GUI

run the script with the `gui` argument to run the program with a proper GUI

`python employeeManagement.py gui`

This will bring up the user interface for easier usage for your average user.
Buttons should be self-explainatory once the application loads up.

## Special Thanks

### [rvhoyt](https://github.com/rvhoyt)

rvhoyt created the [Reftab Library](https://github.com/Reftab/ReftabPython) that I worked with. Some additional work was
added to it and may be cleaned up for a pull request to his repo at a later date.

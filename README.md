# Test_Automation
Selenium Webdriver and Unittest framework in Python


Test Automation of different functionalities of the Django site using Selenium Webdriver and Unittest python framework


The basic building blocks of unit testing are test cases — single scenarios that must be set up and checked for correctness. In Unittest, test cases are represented by Unittest. TestCase instances - To make your own test cases you must write subclasses of TestCase or use FunctionTestCase. Some users will find that they have existing test code that they would like to run from Unittest, without converting every old test function to a TestCase subclass.

For this reason, Unittest provides a FunctionTestCase class. This subclass of TestCase can be used to wrap an existing test function. Set-up and tear-down functions can also be provided.

The code can be separated into 4 different segments for maximum re-usability:- main.py, page.py, element.py, locator.py.

main.py:
The script is responsible for setting up the connection, running different tests and tearing down wrapping up the whole process.

locator.py:
The script fetches the desired position of different elements on the website that has to be interacted with.

element.py:
The script interacts with different elements of the site making use of base methods.
We will be using the get and set method to fill different forms and get specific data from the site.

page.py:
The script comprises of methods that actually interacts with different elements of site making use of some base methods when needed from element.py.

The code can easily be altered to test different functionalities of the website such as:- SignUp, Delete Post, Add Post, Password Reset, Update Profile or multiple functionalities at once.

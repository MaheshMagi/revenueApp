# Revenue Application

**Description**: A Revenue query application which provides the consolidated sales based on provided time duration.  

### Linux and MacOS Installation
Execute the following commands on your terminal (without the '$')  
```
$ git clone https://github.com/MaheshMagi/revenueApp.git
$ cd revenueApp

# Check which version of python by executing the following command 
$ python --version (If python latest(3.8.10) is not available please install from here - https://www.python.org/downloads/)

# Create virtual environment
$ python -m venv venv

# Install the dependencies
$ pip3 install -r requirements.txt

# Run the server
$ python manage.py runserver


### Testing
Pytest is used for testing the APIs and the following command will execute the test
$ pytest
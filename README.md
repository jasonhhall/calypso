Python-selenium-project
=========

Getting Started
-----------
 - You will need to add a .env file inside the project directory
```
EMAIL=<YOUR-EMALI>@gmail.com
PASSWORD=<YOUR ACCOUNT PASSWORD>
```
- The Test data is inside the settings.py 
- Install from requirements.txt
```
pipenv install -r ./requirements.txt
```


General Examples
---------
To run all tests on Chrome
```
pytest -v TEST_ITEM_PURCHASE_WORKFLOW.py
```
```
pytest -v TEST_LOGIN_WORKFLOW.py
```
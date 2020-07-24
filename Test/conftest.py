import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# request is a instance for fixture.

# assign tat instance to variable driver so that whichever call the fixture is called

# if there is a variable in there as driver then it will be assigned to the value from fixture method


def pytest_addoption(parser):
    parser.addoption(
        "--Browser_name", action="store", default="IE"
    )


@pytest.fixture(scope="class")
def setup(request):

    browsername = request.config.getoption("Browser_name")
    if browsername == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browsername == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browsername == "IE":
        print("IE driver to be added ")
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    request.cls.driver = driver

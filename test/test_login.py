import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    #driver.close()
    #driver.quit()

def test_open_url(driver):
    driver.get("https://staging.app.smarthop.co/login")
    assert "SmartHop" == driver.title

def test_login(driver):
    #find user element input and type ndiaz+carrier16@smarthop.co
    driver.find_element(By.NAME, 'email').send_keys("ndiaz+carrier5@smarthop.co")
    #find user element password and type 123456
    driver.find_element(By.NAME, 'password').send_keys("123456")
    #click in the button
    wait = WebDriverWait(driver, 40)
    boton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    #select an account
    #driver.find_element(By.XPATH, '//*[@id="fuse-main"]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[3]/div/form/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/p[1]').click()
    assert 'login' in driver.current_url

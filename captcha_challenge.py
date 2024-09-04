import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Set up chrome web driver
service = ChromeService(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# Headless mode
options.add_argument("--headless")
driver = webdriver.Chrome(
    service=service,
    options=options,
)


# Simulate mouse movement
def simulate_mouse_movement():
    action = ActionChains(driver)
    for _ in range(random.randint(3, 7)):
        x_offset = random.randint(-100, 100)
        y_offset = random.randint(-100, 100)
        action.move_by_offset(x_offset, y_offset).perform()
        time.sleep(random.uniform(0.5, 1.5))


def solve_captcha():
    # Switch to iframe that directly houses pX "Press & Hold" button
    WebDriverWait(driver, timeout=300).until(
        EC.frame_to_be_available_and_switch_to_it("iframe_locator")
    )
    # Get the Press & Hold button element (most a div element)
    btn = driver.find_element(By.XPATH, "//div[p[text() = 'Press & Hold']]")
    # Initialize for low-level interactions
    action = ActionChains(driver)
    action.click_and_hold(btn)
    # Initiate click and hold action on button
    action.perform()
    # Keep holding for 10s
    time.sleep(10)
    # Release button
    action.release(btn)
    time.sleep(10)


# Open Walmart
driver.get("https://walmart.com")
solve_captcha()
# Wait for 2 secs
time.sleep(100000000)
# Take a snapshot of the current screen and
# save as `walmart.png` in the current directory
driver.save_screenshot("solved_walmart.png")

# Print text content
body = driver.find_element(By.TAG_NAME, "body")
print(body.text)
# fetching-volume
driver.quit()

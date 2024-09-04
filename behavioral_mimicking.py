# pip install pyautogui
import pyautogui
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


# Set up chrome web driver
service = ChromeService(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# Headless mode
options.add_argument("--headless")
driver = webdriver.Chrome(
    service=service,
    options=options,
)


def simulate_delay(min_time=1, max_time=3):
    delay = random.uniform(min_time, max_time)
    time.sleep(delay)


def simulate_scrolling():
    # Simulate scrolling
    for _ in range(5):
        scroll_distance = random.randint(200, 800)
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        time.sleep(random.uniform(1, 3))


def simulate_human_typing(text):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.3))


# Function to simulate human-like mouse movement across the screen
def simulate_mouse_movement(total_moves=50, move_variance=100):
    action = ActionChains(driver)

    # Get the size of the window
    window_width = driver.execute_script("return window.innerWidth")
    window_height = driver.execute_script("return window.innerHeight")

    # Start at a random position
    current_x = random.randint(0, window_width)
    current_y = random.randint(0, window_height)
    action.move_by_offset(current_x, current_y).perform()

    for _ in range(total_moves):
        # Calculate the next move, adding a variance to mimic human movement
        next_x = current_x + random.randint(-move_variance, move_variance)
        next_y = current_y + random.randint(-move_variance, move_variance)
        # Ensure the mouse stays within the window boundaries
        next_x = max(0, min(window_width - 1, next_x))
        next_y = max(0, min(window_height - 1, next_y))
        # Move the mouse
        action.move_by_offset(next_x - current_x, next_y - current_y).perform()
        # Update the current position
        current_x, current_y = next_x, next_y
        # Random sleep to simulate human pauses
        time.sleep(random.uniform(0.1, 0.5))


# Open Walmart
driver.get("https://walmart.com")
simulate_mouse_movement()
time.sleep(100000000)

# Print text content
body = driver.find_element(By.TAG_NAME, "body")
print(body.text)

driver.quit()

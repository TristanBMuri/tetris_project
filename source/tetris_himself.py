# Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pathlib import Path
import time


# Initialize WebDriver and open the Tetris game
driver = webdriver.Firefox()  # Adjust if you're using a different browser
html_file = Path.cwd() / ".//tetris_game//index.html"
driver.get(html_file.as_uri())

# Wait for the game to load
time.sleep(5)  # Adjust based on your system performance

# Press space to start the game

def get_game_state():
    # Implement logic to capture and analyze the game state
    # This can be complex and might involve image recognition or DOM inspection
    blocks = driver.execute_script("return blocks")

    return blocks

def calculate_best_move(game_state):
    # Implement your AI logic here


    # Return the sequence of moves and rotations

    return ["right", "rotate", "drop"]

def make_move(move):
    
    return "hello"

# Function to poll for the custom event
def poll_for_custom_event():
    value = driver.find_element(By.ID, "start").get_attribute("style")
    if value != "visibility: hidden;":
        return True

def get_score():
    return driver.find_element(By.ID, "score").text

# Main game loop
def start_game():
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SPACE)

    while True:
        get_score()
        state = get_game_state()
        if poll_for_custom_event():
            get_score()
            break
        move = calculate_best_move(state)
        make_move(move)
        time.sleep(0.5)

start_game()

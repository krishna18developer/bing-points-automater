"""
Bing Points Automater
Author: Krishna Teja
GitHub: https://github.com/krishna18developer

A script to automate Bing searches for Microsoft Rewards points.
Works on both Windows and macOS with existing Edge profiles.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import time
import random
import string
import os
import platform

def get_edge_profile_path():
    system = platform.system()
    username = os.getenv('USER') or os.getenv('USERNAME')
    
    if system == "Darwin":  # macOS
        return f"/Users/{username}/Library/Application Support/Microsoft Edge/Default"
    elif system == "Windows":
        # Return the parent User Data directory instead of Default profile
        return f"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Edge\\User Data"
    else:
        raise OSError(f"Unsupported operating system: {system}")
    

def generate_random_search():
    # Generate a random string of 5-10 characters
    length = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def main():
    # Set up Edge options with your profile
    edge_options = Options()
    
    try:
        profile_path = get_edge_profile_path()
        
        # Add these options for Windows to properly handle profiles
        if platform.system() == "Windows":
            # Basic options for stability on Windows
            edge_options.add_argument("--disable-dev-shm-usage")
            edge_options.add_argument("--no-sandbox")
            edge_options.add_argument("--disable-gpu")
            edge_options.add_argument("--remote-debugging-port=9222")
            
            edge_options.add_argument(f"user-data-dir={profile_path}")
            edge_options.add_argument("profile-directory=Default")  # Use Default profile
            edge_options.add_argument("--no-first-run")
            edge_options.add_argument("--no-default-browser-check")
            edge_options.add_argument("--disable-extensions")
            edge_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        else:
            edge_options.add_argument(f"user-data-dir={profile_path}")
        
        # Set up the Edge service with local driver
        driver_name = "msedgedriver.exe" if platform.system() == "Windows" else "msedgedriver"
        edge_service = Service(executable_path=f"./{driver_name}")
        
        print("Initializing Edge browser...")
        # Initialize the browser with the local driver
        driver = webdriver.Edge(service=edge_service, options=edge_options)
        print("Edge browser initialized successfully!")
        
        sleep_input = input("Enter the sleep duration between searches in seconds (default 30): ")
        sleep_duration = 30 if sleep_input == "" else int(sleep_input)

        # Perform 35 searches
        for i in range(35):
            # Navigate to Bing
            driver.get("https://www.bing.com")
            
            # Wait for the search box to be available
            time.sleep(2)
            
            # Find the search box and enter a random search
            search_box = driver.find_element(By.NAME, "q")
            search_term = generate_random_search()
            search_box.clear()
            search_box.send_keys(search_term)
            search_box.send_keys(Keys.RETURN)
            
            print(f"Search {i + 1}/35: {search_term}")
            
            # Wait for specified duration before the next search
            time.sleep(sleep_duration)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main()

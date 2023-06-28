def test_website_loading():
    # Initialize the WebDriver with the path to the downloaded driver
    driver = webdriver.Chrome('/path/to/chromedriver')
    
    # Open the website
    driver.get('https://atg.world')

    try:
        # Wait for the website to load by checking the presence of a specific element
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'Your CSS Selector Here'))
        )
        # If the element is found, print a success message
        print("Website loaded successfully!")
    except TimeoutException:
        # If the element is not found within the specified time (10 seconds), print an error message
        print("Website failed to load!")

    # Close the WebDriver
    driver.quit()

# Run the test
test_website_loading()

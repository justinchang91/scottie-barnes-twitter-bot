from stats import get_stats
from selenium import webdriver
from tweeter import create_tweet


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(options)

    data = get_stats(driver)
    driver.quit()

    create_tweet(data)


main()

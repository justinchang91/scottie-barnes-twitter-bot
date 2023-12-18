from stats import get_stats
from selenium import webdriver
from tweeter import create_tweet


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(options)

    data = get_stats(driver)
    shouldCreateTweet = False

    try:
        file = open("lastGameScraped.txt", "r")
        prev_date = file.readline()
        file.close()
    except:
        prev_date = ""

    if prev_date != data["date"] and "win_loss" in data and data["win_loss"] != "":
        shouldCreateTweet = True
        file = open("lastGameScraped.txt", "w")
        file.write(data["date"])
        file.close()

    driver.quit()

    if shouldCreateTweet:
        create_tweet(data)


main()

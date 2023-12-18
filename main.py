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
        date = file.readline()
        if (
            date != data["date"]
            and "win_loss" in data
            and (data["win_loss"] == "W" or data["win_loss"] == "L")
        ):
            shouldCreateTweet = True
            file = open("lastGameScraped.txt", "w")
            file.write(data["date"])
            file.close()
    except:
        shouldCreateTweet = True
        file = open("lastGameScraped.txt", "w")
        file.write(data["date"])
        file.close()

    driver.quit()

    if shouldCreateTweet:
        create_tweet(data)


main()

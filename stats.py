from selenium.webdriver.common.by import By


def get_stats(driver):
    driver.get("https://www.nba.com/player/1630567/scottie-barnes")

    date = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[1]/a',
    ).text
    match_up = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[2]',
    ).text
    win_loss = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[3]',
    ).text
    minutes = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[4]',
    ).text
    points = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[5]',
    ).text
    fgm = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[6]/a',
    ).text
    fga = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[7]/a',
    ).text
    fg_percent = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[8]',
    ).text
    three_p_m = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[9]/a',
    ).text
    three_p_a = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[10]/a',
    ).text
    three_p_percent = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[11]',
    ).text
    ftm = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[12]',
    ).text
    fta = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[13]',
    ).text
    ft_percent = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[14]',
    ).text
    o_rebounds = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[15]/a',
    ).text
    d_rebounds = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[16]/a',
    ).text
    rebounds = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[17]/a',
    ).text
    assists = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[18]/a',
    ).text
    steals = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[19]/a',
    ).text
    blocks = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[20]/a',
    ).text
    turnovers = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[21]/a',
    ).text
    personal_fouls = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[22]',
    ).text
    plus_minus = driver.find_element(
        By.XPATH,
        '//*[@id="__next"]/div[2]/div[2]/section/div[4]/section[2]/div/div/div/table/tbody/tr[1]/td[23]',
    ).text

    return {
        "date": date,
        "match_up": match_up,
        "win_loss": win_loss,
        "minutes": minutes,
        "points": points,
        "fgm": fgm,
        "fga": fga,
        "fg_percent": fg_percent,
        "three_p_m": three_p_m,
        "three_p_a": three_p_a,
        "three_p_percent": three_p_percent,
        "ftm": ftm,
        "fta": fta,
        "ft_percent": ft_percent,
        "o_rebounds": o_rebounds,
        "d_rebounds": d_rebounds,
        "rebounds": rebounds,
        "assists": assists,
        "steals": steals,
        "blocks": blocks,
        "turnovers": turnovers,
        "personal_fouls": personal_fouls,
        "plus_minus": plus_minus,
    }

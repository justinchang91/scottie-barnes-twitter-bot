import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

team_legend = {
    "ATL": "Hawks",
    "BOS": "Celtics",
    "BKN": "Nets",
    "CHA": "Hornets",
    "CHI": "Bulls",
    "CLE": "Cavaliers",
    "DAL": "Mavericks",
    "DEN": "Nuggets",
    "DET": "Pistons",
    "GSW": "Warriors",
    "GS": "Warriors",
    "HOU": "Rockets",
    "IND": "Pacers",
    "LAC": "Clippers",
    "LAL": "Lakers",
    "MEM": "Grizzlies",
    "MIA": "Heat",
    "MIL": "Bucks",
    "MIN": "Timberwolves",
    "NOP": "Pelicans",
    "NO": "Pelicans",
    "NYK": "Knicks",
    "NY": "Knicks",
    "OKC": "Thunder",
    "ORL": "Magic",
    "PHI": "76ers",
    "PHX": "Suns",
    "POR": "Trail Blazers",
    "SAC": "Kings",
    "SAS": "Spurs",
    "SA": "Spurs",
    "TOR": "Raptors",
    "UTA": "Jazz",
    "UTAH": "Jazz",
    "WAS": "Wizards",
}


def create_tweet(data):
    client = tweepy.Client(
        BEARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    )

    game_status = "win" if data["win_loss"] == "W" else "loss"
    opponent = data["match_up"].split(" ")[2]
    plus_minus = "+" if int(data["plus_minus"]) > 0 else ""
    points = "point" if int(data["points"]) == 1 else "points"
    rebounds = "rebound" if int(data["rebounds"]) == 1 else "rebounds"
    assists = "assist" if int(data["assists"]) == 1 else "assists"
    blocks = "block" if int(data["blocks"]) == 1 else "blocks"
    steals = "steal" if int(data["steals"]) == 1 else "steals"
    turnovers = "turnover" if int(data["turnovers"]) == 1 else "turnovers"
    minutes = "minute" if int(data["minutes"]) == 1 else "minutes"

    initial_text = f"Scottie Barnes in a Raptors {game_status} against the {team_legend[opponent]}:\n\n"
    body_text = f'{data["points"]} {points} ({data["fgm"]}/{data["fga"]} FG)\n{data["rebounds"]} {rebounds}\n{data["assists"]} {assists}\n{data["steals"]} {steals}\n{data["blocks"]} {blocks}\n{data["three_p_m"]}/{data["three_p_a"]} 3PM\n{data["ftm"]}/{data["fta"]} FT\n{data["turnovers"]} {turnovers}\n\n'
    end_text = f'{plus_minus}{data["plus_minus"]} in {data["minutes"]} {minutes}.'

    tweet_text = initial_text + body_text + end_text
    client.create_tweet(text=tweet_text)

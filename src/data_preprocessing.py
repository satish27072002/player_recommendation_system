import pandas as pd

import os

def load_data():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    batting = pd.read_csv(os.path.join(base_path, "data/batting_summaries.csv"))
    bowling = pd.read_csv(os.path.join(base_path, "data/bowling_summaries.csv"))
    match_summary = pd.read_csv(os.path.join(base_path, "data/match_summary.csv"))
    player_info = pd.read_csv(os.path.join(base_path, "data/player_info.csv"))
    teams = pd.read_excel(os.path.join(base_path, "data/teams_with_flags.xlsx"))
    return batting, bowling, match_summary, player_info, teams


def preprocess_batting_data(batting):
    # Example: Calculate average runs
    batting['avg_runs'] = batting.groupby('batsmanName')['runs'].transform('mean')
    return batting

def preprocess_bowling_data(bowling):
    # Example: Calculate economy rate
    bowling['economy_rate'] = bowling['runsConceded'] / bowling['overs']
    return bowling

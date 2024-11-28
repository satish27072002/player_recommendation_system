import pandas as pd

def create_player_metrics(batting, bowling):
    """
    Merge batting and bowling data to create a combined player performance dataset.
    """
    # Ensure batting and bowling data have relevant columns
    batting = batting[['batsmanName', 'avg_runs']].drop_duplicates()
    bowling = bowling[['bowlerName', 'economy_rate']].drop_duplicates()

    # Merge batting and bowling data on player names
    players = pd.merge(
        batting,
        bowling,
        left_on='batsmanName',
        right_on='bowlerName',
        how='outer'
    )
    
    # Rename and clean up the merged dataset
    players.rename(columns={'batsmanName': 'player'}, inplace=True)
    players.drop(columns=['bowlerName'], inplace=True)  # Drop duplicate column
    return players

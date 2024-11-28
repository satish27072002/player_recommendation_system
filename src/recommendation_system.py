def recommend_players(players, role="batsman", threshold=30):

    if role == "batsman":
        # Recommend batsmen with avg_runs above the threshold
        return players[players['avg_runs'] > threshold].sort_values(by="avg_runs", ascending=False)
    elif role == "bowler":
        # Recommend bowlers with economy_rate below the threshold
        return players[players['economy_rate'] < threshold].sort_values(by="economy_rate")
    elif role == "allrounder":
        # Recommend all-rounders (players with both batting and bowling stats)
        return players[(players['avg_runs'] > threshold) & (players['economy_rate'] < threshold)]
    else:
        raise ValueError(f"Invalid role: {role}. Choose 'batsman', 'bowler', or 'allrounder'.")


    # Sample data
    players = pd.DataFrame({
        'player': ['Player1', 'Player2', 'Player3', 'Player4'],
        'avg_runs': [50, 30, 40, 60],
        'economy_rate': [6.0, 7.5, 5.5, 8.0]
    })

    # Test recommendations
    print("Recommended Batsmen:")
    print(recommend_players(players, role="batsman", threshold=35))

    print("\nRecommended Bowlers:")
    print(recommend_players(players, role="bowler", threshold=7.0))

    print("\nRecommended All-Rounders:")
    print(recommend_players(players, role="allrounder", threshold=35))

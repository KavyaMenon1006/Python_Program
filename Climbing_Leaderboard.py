def climbingLeaderboard(ranked, player):
    #sort 
    unique = sorted(set(ranked), reverse=True)
    result = []
    i = len(unique) - 1 
    for score in player:
        while i >= 0 and score >= unique[i]:
            i -= 1
        result.append(i + 2)
    return result

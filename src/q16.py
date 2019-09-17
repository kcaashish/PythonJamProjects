def nextRound(k, scores):
    count = 0
    running = True

    try:
        scoreList = list(scores)
        oneScore = scoreList[k - 1]
    except TypeError:
        scoreList = scores
        if scoreList == 0:
            return 0
        else:
            return 1


    # print(scoreList)

    for score in scoreList:
        while running:
            if oneScore <= score:
                if score != 0:
                    count += 1
                    break
                else:
                    break
            else:
                break
    return count


# print(nextRound(5, (10, 9, 8, 7, 6, 6, 6, 5, 4))) # 7
# print(nextRound(2, (0, 0, 0, 0))) # 0
# print(nextRound(2, (1, 1, 1, 1))) # 4
print(nextRound(20, (20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)))  # 20
# print(nextRound(1, (5, 4, 3, 2)))  # 1
# print(nextRound(1, (0))) # 0


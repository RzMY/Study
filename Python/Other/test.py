def change_score(score):
    for i in range(len(score)):
        if 58 <= score[i] < 60:
            score[i] = 60
    return score

def change_score2(score):
    return [60 if 58 <= s < 60 else s for s in score]

def main():
    score = [90, 80, 70, 59.2, 55, 60, 50]
    print(score)
    print(change_score2(score))
    
if __name__ == '__main__':
    main()
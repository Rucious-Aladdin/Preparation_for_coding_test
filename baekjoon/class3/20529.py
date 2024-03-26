from itertools import combinations

# split caculating distances
def get_distance(mbti1, mbti2):
    dist = 0
    for i in range(4):
        if mbti1[i] != mbti2[i]:
            dist+=1
    return dist
    

TC = int(input())
answers = []
for _ in range(TC):
    # data input
    persons = int(input())
    mbti_pipeline = input().split()
    
    # data dictionary (preprocessing)
    mbti_dict = {}
    for mbti in mbti_pipeline:
        try:
            if mbti_dict[mbti] < 3:
                mbti_dict[mbti] += 1
        except:
            mbti_dict[mbti] = 1
    pruned_mbti_pipeline = []
    for mbti, value in mbti_dict.items():
        pruned_mbti_pipeline.extend([mbti] * value)
    
    # data algorithm
    min_dist = int(1e9)
    for x in combinations(pruned_mbti_pipeline, 3):
        dist1 = get_distance(x[0], x[1])
        dist2 = get_distance(x[0], x[2])
        dist3 = get_distance(x[1], x[2])
        total_dist = dist1 + dist2 + dist3
        if total_dist < min_dist:
            min_dist = total_dist
    
    # collect answers
    answers.append(min_dist)

# print answers
for x in answers:
    print(x)

def latest(scores):
    return scores[-1]

def personal_best(scores):
    return sorted(scores)[-1]


def personal_top_three(scores):
    sorted_scores = sorted(scores)
    return sorted_scores[-3:][::-1]

def low_to_high(scores):
    return sorted(scores)[::-1]

def if_tie(scores):
    top_scores_filtered = []
    for scores in scores:
        if scores not in top_scores_filtered:
            top_scores_filtered.append(scores)
    return top_scores_filtered
    #top_scores_filtered = [score for score in scores if scores.append(scores)]
    #if scores include 2 the same numbers
    #return top 3 scores


# top_scores_filtered = []
# for scores in scores:
#         if scores not in top_scores_filtered:
#             top_scores_filtered.append(scores)

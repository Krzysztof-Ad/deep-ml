import math

def softmax(scores: list[float]) -> list[float]:
    mx = max(scores)

    sm = 0
    for j in range(len(scores)):
        sm += math.exp(scores[j] - mx)
    
    result = []
    for score in scores:
        result.append((math.exp(score - mx)) / sm)
    

    return result
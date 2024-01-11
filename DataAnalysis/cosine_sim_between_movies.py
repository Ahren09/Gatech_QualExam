import numpy as np

def correct_cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0
    return dot_product / (norm_vec1 * norm_vec2)


ratings = {
    "F": np.array([5, 3, 0, 2, 4]),
    "TO": np.array([4, 0, 0, 0, 4]),
    "AD": np.array([4, 0, 0, 4, 0]),
    "BBT": np.array([0, 2, 1, 0, 0]),
    "IV": np.array([1, 0, 1, 1, 0]),
}

for (v1, v2) in [("F", "AD"), ("F", "BBT"), ("F", "IV"), ("TO", "AD"), ("TO", "BBT"), ("TO", "IV"), ]:
    print(v1, v2, correct_cosine_similarity(ratings[v1], ratings[v2]))


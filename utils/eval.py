from typing import List

import numpy as np

from rouge.rouge import rouge_w_sentence_level

def evaluate_single(prediction: str, ground_truth: str) -> np.array:
    gt_tokens = ground_truth.strip().split(" ")
    pre_tokens = prediction.strip().split(" ")

    # ROUGE-W
    _, _, rouge_w = rouge_w_sentence_level(pre_tokens, gt_tokens)

    return float(prediction == ground_truth), rouge_w

def evaluate_list(prediction: List, ground_truth: List) -> np.array:
    exact_match_scores, rouge_scores = [], []

    for i in range(len(ground_truth)):
        em, rouge = evaluate_single(prediction[i], ground_truth[i])
        exact_match_scores.append(em)
        rouge_scores.append(rouge)
        # if(prediction[i] != ground_truth[i]):
        #     print(prediction[i], '---------', ground_truth[i])
    return {"acc": np.mean(exact_match_scores), "rouge-w": np.mean(rouge_scores)}


def get_details(prediction: List, ground_truth: List) -> np.array:
    exact_match_scores, rouge_scores = [], []

    for i in range(len(ground_truth)):
        em, rouge = evaluate_single(prediction[i], ground_truth[i])
        exact_match_scores.append(em)
        rouge_scores.append(rouge)
        # if(prediction[i] != ground_truth[i]):
        #     print(prediction[i], '---------', ground_truth[i])
    return rouge_scores, exact_match_scores

from knowledge_base import KNOWLEDGE_BASE


def search_knowledge(question):

    question = question.lower()

    best_match = None
    highest_score = 0

    for item in KNOWLEDGE_BASE:

        score = 0

        for keyword in item["keywords"]:

            if keyword in question:
                score += 1

        if score > highest_score:
            highest_score = score
            best_match = item

    return best_match

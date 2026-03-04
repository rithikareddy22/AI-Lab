import random


human_responses = [
    "I love watching movies on weekends.",
    "Sometimes I feel tired after work.",
    "I think pizza is the best comfort food.",
    "That depends on how you look at it.",
    "Can you explain what you mean?"
]


def ai_response(question):
    question = question.lower()
    
    if "hello" in question:
        return "Hello! How can I assist you today?"
    elif "how are you" in question:
        return "I am functioning properly."
    elif "name" in question:
        return "I am an artificial intelligence program."
    else:
        return "That is an interesting question."


def human_response():
    return random.choice(human_responses)

def turing_test():
    print("\n===== Turing Test Simulation =====")
    print("You will chat with two participants: A and B.")
    print("One is Human, one is AI.")
    print("After 3 questions, guess who is AI.\n")

    participants = ["AI", "Human"]
    random.shuffle(participants)

    for i in range(3):
        question = input("Ask a question: ")

        for idx, role in enumerate(participants):
            if role == "AI":
                response = ai_response(question)
            else:
                response = human_response()

            print(f"Participant {chr(65+idx)}: {response}")
        print()

    guess = input("Who is AI? (A/B): ").upper()

    actual_ai_index = participants.index("AI")
    correct_answer = chr(65 + actual_ai_index)

    if guess == correct_answer:
        print("Correct! You identified the AI.")
    else:
        print("Wrong guess.")
    
    print("AI was Participant", correct_answer)


if __name__ == "__main__":
    turing_test()
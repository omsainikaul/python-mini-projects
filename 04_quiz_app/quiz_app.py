def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C) Paris"
        },
        {
            "question": "What is 27 + 3?",
            "options": ["A) 30", "B) 35", "C) 40", "D) 45"],
            "answer": "A) 30"
        },
        {
            "question": "Which is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
            "answer": "B) Jupiter"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen"],
            "answer": "C) William Shakespeare"
        },
        {
            "question": "What is the boiling point of water at sea level?",
            "options": ["A) 90°C", "B) 100°C", "C) 110°C", "D) 120°C"],
            "answer": "B) 100°C"
        },
        {
            "question": "What is the capital of Japan?",
            "options": ["A) Seoul", "B) Beijing", "C) Tokyo", "D) Bangkok"],
            "answer": "C) Tokyo"
        }
    ]

    score = 0
 
    for index,q in enumerate(questions):  
        print(f"Q{index + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("Your answer(A/B/C/D): ") 
        if user_answer.strip().upper() == q['answer'][0]:
            print("Correct!\n")
            score += 1

    print(f"Your final score is {score}/{len(questions)}")

run_quiz()
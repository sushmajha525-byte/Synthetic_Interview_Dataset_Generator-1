from typing import Dict, List

QuestionBank = Dict[str, Dict[str, List[str]]]

question_bank: QuestionBank = {

    "Programming & Object-Oriented Concepts": {

        "Easy": [
            "What is a variable and why is it used in programming?",
            "What is the difference between a list and a tuple in Python?",
            "What is a function and what are its benefits?",
            "What is the purpose of a dictionary in Python?",
            "What is Object-Oriented Programming (OOP)?"
        ],

        "Medium": [
            "What is the difference between a class and an object?",
            "Explain inheritance with an example.",
            "What is encapsulation and why is it important?",
            "What is exception handling and how is it implemented in Python?",
            "What are Python modules and why are they used?"
        ],

        "Hard": [
            "Explain polymorphism and its advantages.",
            "What are decorators in Python and where are they used?",
            "Explain generators and their benefits over lists.",
            "What is the difference between shallow copy and deep copy?",
            "How does multithreading work in Python and what is the role of the GIL?"
        ]
    },

    "SQL & Database Systems": {

        "Easy": [
            "What is a Database Management System (DBMS)?",
            "What is SQL and why is it used?",
            "What is a primary key?",
            "What is a foreign key?",
            "What is a database table?"
        ],

        "Medium": [
            "What is normalization and why is it important?",
            "What are SQL joins and why are they used?",
            "What is the difference between DELETE, DROP, and TRUNCATE?",
            "What is indexing and how does it improve performance?",
            "What are ACID properties in a database?"
        ],

        "Hard": [
            "Explain database transactions with an example.",
            "What is a deadlock and how can it be prevented?",
            "What is the difference between clustered and non-clustered indexes?",
            "What is database sharding and when is it used?",
            "Explain concurrency control in DBMS."
        ]
    },

    "Machine Learning & AI": {

        "Easy": [
            "What is Machine Learning?",
            "What is the difference between AI and Machine Learning?",
            "What is supervised learning?",
            "What is unsupervised learning?",
            "What is a dataset in Machine Learning?"
        ],

        "Medium": [
            "What is overfitting and how can it be reduced?",
            "What is underfitting?",
            "What is feature engineering?",
            "What is classification in Machine Learning?",
            "What is cross-validation and why is it used?"
        ],

        "Hard": [
            "Explain gradient descent and its role in model training.",
            "What is the bias-variance tradeoff?",
            "What is regularization and why is it important?",
            "What is ensemble learning and how does it improve performance?",
            "What is hyperparameter tuning and why is it necessary?"
        ]
    },

    "Software Engineering": {

        "Easy": [
            "What is the Software Development Life Cycle (SDLC)?",
            "What is version control and why is it important?",
            "What is Git?",
            "What is debugging?",
            "What is software testing?"
        ],

        "Medium": [
            "What is a REST API?",
            "What is unit testing?",
            "What is integration testing?",
            "What is Agile methodology?",
            "What is code review and why is it important?"
        ],

        "Hard": [
            "Explain Continuous Integration and Continuous Deployment (CI/CD).",
            "What are design patterns and why are they used?",
            "What is microservices architecture?",
            "What is dependency injection?",
            "Explain the SOLID principles of software design."
        ]
    }
}


def get_all_domains() -> List[str]:
    return list(QUESTION_BANK.keys())


def get_all_difficulties() -> List[str]:
    return ["Easy", "Medium", "Hard"]


def get_questions(domain: str, difficulty: str) -> List[str]:
    if domain not in QUESTION_BANK:
        raise KeyError(f"Unknown domain: '{domain}'.")
    if difficulty not in QUESTION_BANK[domain]:
        raise KeyError(f"Unknown difficulty: '{difficulty}'.")
    return QUESTION_BANK[domain][difficulty]


def count_questions() -> int:
    return sum(
        len(questions)
        for domain in QUESTION_BANK.values()
        for questions in domain.values()
    )


def get_question_distribution() -> Dict[str, Dict[str, int]]:
    return {
        domain: {
            difficulty: len(questions)
            for difficulty, questions in difficulties.items()
        }
        for domain, difficulties in QUESTION_BANK.items()
    }


if __name__ == "__main__":
    print(f"Total questions : {count_questions()}")
    for domain, levels in get_question_distribution().items():
        for difficulty, count in levels.items():
            print(f"  {domain} | {difficulty} | {count}")
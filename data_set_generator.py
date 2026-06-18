import json
import csv
from pathlib import Path

from question_bank import question_bank
from answer_bank import answer_bank


def generate_dataset():

    dataset = []

    print("Question Bank Domains:", list(question_bank.keys()))
    print("Answer Bank Domains:", list(answer_bank.keys()))

    for domain, difficulty_levels in question_bank.items():

        print(f"\nDomain: {domain}")

        for difficulty, questions in difficulty_levels.items():

            print(f"  Difficulty: {difficulty}")
            print(f"  Questions: {len(questions)}")

            if domain not in answer_bank:
                print("  Domain missing in answer_bank")
                continue

            if difficulty not in answer_bank[domain]:
                print("  Difficulty missing in answer_bank")
                continue

            print(f"  Answers Available: {len(answer_bank[domain][difficulty])}")

            for index, question in enumerate(questions):

                if index >= len(answer_bank[domain][difficulty]):
                    print(f"Missing answer at index {index}")
                    continue

                answers = answer_bank[domain][difficulty][index]

                for label in ["correct", "partial", "incorrect"]:

                    dataset.append({
                        "domain": domain,
                        "difficulty": difficulty,
                        "question": question,
                        "answer": answers[label],
                        "label": label
                    })

    print("Final Dataset Size:", len(dataset))

    return dataset


def export_json(dataset, output_path):
    """Exports dataset to JSON."""

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(dataset, file, indent=4, ensure_ascii=False)


def export_csv(dataset, output_path):
    """Exports dataset to CSV."""

    with open(output_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "domain",
                "difficulty",
                "question",
                "answer",
                "label"
            ]
        )

        writer.writeheader()
        writer.writerows(dataset)


def main():

    data_folder = Path("data")
    data_folder.mkdir(exist_ok=True)

    dataset = generate_dataset()
    print("Question Bank Domains:", question_bank.keys())
    print("Answer Bank Domains:", answer_bank.keys())

    export_json(
        dataset,
        data_folder / "interview_dataset.json"
    )

    export_csv(
        dataset,
        data_folder / "interview_dataset.csv"
    )

    print("=" * 50)
    print("Dataset Generated Successfully")
    print("=" * 50)
    print(f"Total Samples : {len(dataset)}")
    print(f"JSON File     : {data_folder/'interview_dataset.json'}")
    print(f"CSV File      : {data_folder/'interview_dataset.csv'}")


if __name__ == "__main__":
    main()
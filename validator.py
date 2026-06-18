import json
from pathlib import Path
from collections import Counter


VALID_LABELS = {"correct", "partial", "incorrect"}


def load_dataset(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_dataset(dataset):

    report = {}

    report["total_samples"] = len(dataset)

    required_fields = {
        "domain",
        "difficulty",
        "question",
        "answer",
        "label"
    }

    missing_fields = 0
    invalid_labels = 0

    domain_counter = Counter()
    difficulty_counter = Counter()
    label_counter = Counter()

    duplicate_checker = set()
    duplicate_records = 0

    for record in dataset:

        if not required_fields.issubset(record.keys()):
            missing_fields += 1

        if record.get("label") not in VALID_LABELS:
            invalid_labels += 1

        domain_counter[record.get("domain")] += 1
        difficulty_counter[record.get("difficulty")] += 1
        label_counter[record.get("label")] += 1

        key = (
            record.get("domain"),
            record.get("difficulty"),
            record.get("question"),
            record.get("answer"),
            record.get("label")
        )

        if key in duplicate_checker:
            duplicate_records += 1
        else:
            duplicate_checker.add(key)

    report["missing_fields"] = missing_fields
    report["invalid_labels"] = invalid_labels
    report["duplicate_records"] = duplicate_records
    report["domain_distribution"] = dict(domain_counter)
    report["difficulty_distribution"] = dict(difficulty_counter)
    report["label_distribution"] = dict(label_counter)

    report["status"] = (
        "PASSED"
        if (
            missing_fields == 0
            and invalid_labels == 0
            and duplicate_records == 0
        )
        else "FAILED"
    )

    return report


def save_report(report):

    data_folder = Path("data")
    data_folder.mkdir(exist_ok=True)

    report_path = data_folder / "validation_report.json"

    with open(report_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return report_path


def print_report(report):

    print("\n" + "=" * 50)
    print("DATASET VALIDATION REPORT")
    print("=" * 50)

    print(f"Total Samples      : {report['total_samples']}")
    print(f"Missing Fields     : {report['missing_fields']}")
    print(f"Invalid Labels     : {report['invalid_labels']}")
    print(f"Duplicate Records  : {report['duplicate_records']}")

    print("\nDomain Distribution")
    for domain, count in report["domain_distribution"].items():
        print(f"  {domain}: {count}")

    print("\nDifficulty Distribution")
    for difficulty, count in report["difficulty_distribution"].items():
        print(f"  {difficulty}: {count}")

    print("\nLabel Distribution")
    for label, count in report["label_distribution"].items():
        print(f"  {label}: {count}")

    print(f"\nValidation Status  : {report['status']}")
    print("=" * 50)


def main():

    dataset_path = Path("data") / "interview_dataset.json"

    dataset = load_dataset(dataset_path)

    report = validate_dataset(dataset)

    report_file = save_report(report)

    print_report(report)

    print(f"\nValidation report saved to: {report_file}")


if __name__ == "__main__":
    main()
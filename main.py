from data_set_generator import (
    generate_dataset,
    export_json,
    export_csv
)

from validator import (
    validate_dataset,
    save_report,
    print_report
)

from pathlib import Path


def main():

    print("=" * 60)
    print("Synthetic Interview Dataset Generator")
    print("=" * 60)

    data_folder = Path("data")
    data_folder.mkdir(exist_ok=True)

    dataset = generate_dataset()

    json_file = data_folder / "interview_dataset.json"
    csv_file = data_folder / "interview_dataset.csv"

    export_json(dataset, json_file)
    export_csv(dataset, csv_file)

    report = validate_dataset(dataset)

    report_path = save_report(report)

    print("\nDataset Generation Completed Successfully!")
    print(f"Total Samples : {len(dataset)}")
    print(f"JSON File     : {json_file}")
    print(f"CSV File      : {csv_file}")

    print_report(report)

    print(f"\nValidation Report : {report_path}")

    print("\nProject Executed Successfully!")


if __name__ == "__main__":
    main()
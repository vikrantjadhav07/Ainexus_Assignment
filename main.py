import csv
from source.extract import extract_data
from change.transform import transform_data

def main():
    print("hello")
    # Step 1: Extract data from the API
    raw_data = extract_data()

    # Step 2: Transform the extracted data
    transformed_data = transform_data(raw_data)
    print("data transformed successfully")

    with open("F:\\api_data\\loaded\\load.csv", 'w',newline="") as fb:
        f = csv.DictWriter(fb, fieldnames=transformed_data[0].keys())
        f.writeheader()
        f.writerows(transformed_data)


if __name__ == "__main__":
    main()



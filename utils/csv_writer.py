import csv


def save_csv(data):

    with open("Maharera_Data_project.csv", "a", encoding="utf-8-sig", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(data)

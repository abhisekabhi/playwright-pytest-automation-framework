import csv

from Pages.maharera_page import MahareraPage

from utils.csv_writer import save_csv


def test_scrape(page):

    scraper = MahareraPage(page)

    with open("All_link_1.csv") as f:

        urls = csv.reader(f)

        for row in urls:

            url = row[0]

            print("Opening:", url)

            scraper.open_url(url)

            scraper.solve_captcha()

            project_data = scraper.get_project_data()

            final_data = []

            final_data.append(url)

            final_data.extend(project_data)

            print(final_data)

            save_csv(final_data)

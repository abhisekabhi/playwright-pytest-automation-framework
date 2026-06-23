import easyocr


class MahareraPage:

    def __init__(self, page):

        self.page = page
        self.reader = easyocr.Reader(["en"], gpu=False)

    def open_url(self, url):

        self.page.goto(url)
        self.page.wait_for_timeout(5000)

    def solve_captcha(self):
        for i in range(3):

            canvas = self.page.locator("#captcahCanvas").first

            if canvas.count() == 0:
                return False

            canvas.screenshot(path="canvas.png")

            result = self.reader.readtext("canvas.png")

            text = " ".join([item[1] for item in result])

            text = text.strip().replace(" ", "")

            print("Captcha:", text)

            self.page.locator("[name='captcha']").fill(text)

            self.page.locator(".btn").click()

            self.page.wait_for_timeout(3000)

            if self.page.locator("button:has-text('Ok')").is_visible():

                self.page.locator("button:has-text('Ok')").click()

                continue

            else:
                return True

        return False

    def get_project_data(self):

        try:
            # page ka screenshot before checking element
            self.page.screenshot(path="before_building_name.png", full_page=True)

            self.page.wait_for_selector(
                "//label[text()=' Building Name ']", timeout=60000
            )

        except Exception as e:

            print("Building Name not found")
            print(e)

            # error wala screenshot
            self.page.screenshot(path="error.png", full_page=True)

            return ["N/A"] * 5

        data = []

        locators = [
            '[style="background-color: #fdf8f7; padding: 5px 2%; border: 1px solid #f7eae8;"]',
            '//*[@id="hidden_div"]/div/div/div/div/form/fieldset/div[2]/div[1]/div/div[1]',
            '//*[@id="hidden_div"]/div/div/div/div/form/fieldset/div[3]/div/div[1]/div/div[1]',
            '[style="background-color: #fdf8f7; border: 1px solid #f7eae8; border-radius: 4px; margin: 5px 0 5px 0; padding: 5px;"]',
            '[style="background-color: #ffffff; border: 1px solid #e5e5e5; border-radius: 4px; margin: 5px 0 5px 0; padding: 5px;"]',
        ]

        for loc in locators:

            try:

                text = self.page.locator(loc).text_content(timeout=10000)

                data.append(text.strip())

            except Exception as e:

                print("Locator failed:", loc)

                # locator fail screenshot
                self.page.screenshot(path="locator_error.png", full_page=True)

                data.append("N/A")

        # final data screenshot
        self.page.screenshot(path="data_loaded.png", full_page=True)

        return data

import csv


class TestData:
    CHROME_EXECUTABLE_PATH = "../Resources/Drivers/chromedriver.exe"
    EDGE_EXECUTABLE_PATH = "../Resources/Drivers/msedgedriver.exe"
    BASE_URL = "https://www.saucedemo.com/"

    def extract_csv(filename):
        datalist = []
        file = open(filename, 'r')
        reader = csv.reader(file)
        next(reader)

        for rows in reader:
            datalist.append(rows)

        return datalist

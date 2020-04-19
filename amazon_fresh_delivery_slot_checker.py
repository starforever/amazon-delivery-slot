import time

from bs4 import BeautifulSoup
from selenium import webdriver

START_PAGE_URL = "https://www.amazon.com/"
REFRESH_INTERNAL = 60


def check_delivery_slot(page_source: str) -> bool:
    soup = BeautifulSoup(page_source)
    no_slot_elem = soup.find(
        "div", string="No doorstep delivery windows are available for"
    )
    if no_slot_elem != None:
        return False
    return True


def alert_delivery_slot() -> None:
    alert_text = "Found delivery slot! Please proceed to checkout."
    print(alert_text)


def main() -> None:
    driver = webdriver.Chrome()
    driver.get(START_PAGE_URL)

    print(
        "Login to your account. Add items to cart. Then proceed to the page to reserve a delivery slot."
    )

    while True:
        r = input("Enter OK to continue: ")
        if r == "OK":
            break

    while True:
        if check_delivery_slot(driver.page_source):
            alert_delivery_slot()
            break

        print(f"No delivery slot. Retry in {REFRESH_INTERNAL} seconds.")
        time.sleep(REFRESH_INTERNAL)
        driver.refresh()


if __name__ == "__main__":
    main()

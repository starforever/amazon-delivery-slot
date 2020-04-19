import time

from bs4 import BeautifulSoup
from selenium import webdriver

START_PAGE_URL = "https://www.amazon.com/"
REFRESH_INTERNAL = 60


def check_delivery_slot(page_source: str) -> bool:
    soup = BeautifulSoup(page_source, "html5lib")
    no_slot_elem = soup.find(
        "div", string="No doorstep delivery windows are available for"
    )
    if no_slot_elem != None:
        return False
    return True


def alert_delivery_slot() -> None:
    alert_text = "Found delivery slot! Please proceed to checkout."
    print(alert_text)


def confirm_and_continue(confirm_text: str) -> None:
    while True:
        r = input(f"Enter {confirm_text} to continue: ")
        if r == confirm_text:
            break


def main() -> None:
    driver = webdriver.Chrome()
    driver.get(START_PAGE_URL)

    print(
        "Log in to your account. Add items to cart. Then proceed to the page to reserve a delivery slot."
    )
    confirm_and_continue("OK")

    while not check_delivery_slot(driver.page_source):
        print(f"No delivery slot. Retry in {REFRESH_INTERNAL} seconds.")
        time.sleep(REFRESH_INTERNAL)
        driver.refresh()

    alert_delivery_slot()
    confirm_and_continue("OK")


if __name__ == "__main__":
    main()

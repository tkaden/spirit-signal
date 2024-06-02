from data import read_csv
from scraper import scrape_spirits
from notify import notify_users

def main():
    # Step 1: Read input data
    spirits_data = read_csv('spirits.csv')

    # Step 2: Scrape for available spirits
    available_spirits = scrape_spirits(spirits_data)

    # Step 3: Notify users
    notify_users(available_spirits)

if __name__ == "__main__":
    main()
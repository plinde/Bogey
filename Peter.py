
import requests

def main():
    print("Welcome to the Golf Score Tracker!")

    r = requests.get("https://www.golfpars.com/course/marietta-city")


if __name__ == "__main__":
    # Entry point of the script
    main()

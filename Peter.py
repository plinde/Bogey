
import requests

def main():
    print("Welcome to the Golf Score Tracker!")

    r = requests.get("https://www.golfpars.com/course/marietta-city")

    print("hello")

if __name__ == "__main__":
    # Entry point of the script
    main()

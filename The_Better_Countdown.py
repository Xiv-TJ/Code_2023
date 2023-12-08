
import time
def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    if seconds == 0:
        print("Time's up!")
def main():
    try:
        seconds = int(input("From what time would you like to count down from, in seconds? "))
        countdown(seconds)
    except ValueError:
        print("Please enter an actual number.")
if __name__ == "__main__":
    main()
    
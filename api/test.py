import time

time_in_seconds = 2

def read_tweets_from_file(filename, interval=time_in_seconds):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        for line in lines:
            if ':' in line:
                key, tweet = line.split(':', 1)
                tweet = tweet.strip()  
                if tweet:
                    print(f" Tweet: {tweet}")
                    time.sleep(interval)
            else:
                print(f"Skipped invalid line: {line}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

read_tweets_from_file('tweets.txt')

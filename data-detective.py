import csv


# Load CSV

def load_tweets(filename="twitter_dataset.csv"):
    tweets = []
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                tweets.append(row)
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    return tweets



# Quest 1: Data Auditor — Clean missing fields

def audit_data(tweets):
    cleaned = []
    fixed = 0
    removed = 0

    for tweet in tweets:
        # Remove rows with missing Text
        if not tweet.get("Text", "").strip():
            removed += 1
            continue

        # Replace missing Likes / Retweets with 0
        if not tweet.get("Likes", "").strip():
            tweet["Likes"] = "0"
            fixed += 1
        if not tweet.get("Retweets", "").strip():
            tweet["Retweets"] = "0"
            fixed += 1

        cleaned.append(tweet)

    print("=" * 50)
    print("QUEST 1: Data Audit")
    print("=" * 50)
    print(f"  Rows removed  (missing Text)   : {removed}")
    print(f"  Fields fixed  (missing Likes/RT): {fixed}")
    print(f"  Total clean tweets             : {len(cleaned)}")
    return cleaned



# Quest 2: Viral Post — Find max Likes (no max())

def find_viral_post(tweets):
    if len(tweets) == 0:
        print("No tweets to analyse.")
        return

    max_tweet = tweets[0]
    for tweet in tweets:
        if int(tweet["Likes"]) > int(max_tweet["Likes"]):
            max_tweet = tweet

    print("\n" + "=" * 50)
    print("QUEST 2: Viral Post")
    print("=" * 50)
    print(f"  Username : {max_tweet.get('Username', 'N/A')}")
    print(f"  Likes    : {max_tweet['Likes']}")
    print(f"  Text     : {max_tweet.get('Text', 'N/A')}")



# Quest 3: Custom Sort — Partial Selection Sort
# We only need top 10, so we run Selection Sort just 10 times (find the max each pass and swap
# it to the front). This is O(10 * n) instead of
# O(n²), fast on large datasets, no built-ins used.

def partial_selection_sort_top10(tweets, top_n=10):
    arr = list(tweets)
    n = len(arr)
    limit = top_n if top_n < n else n

    for i in range(limit):
        max_idx = i
        for j in range(i + 1, n):
            if int(arr[j]["Likes"]) > int(arr[max_idx]["Likes"]):
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr[:limit]


def show_top10(tweets):
    top10 = partial_selection_sort_top10(tweets, top_n=10)

    print("\n" + "=" * 50)
    print("QUEST 3: Top 10 Most Liked Tweets (Selection Sort)")
    print("=" * 50)
    for rank, tweet in enumerate(top10, start=1):
        print(f"  #{rank:>2}  Likes: {int(tweet['Likes']):<8}  @{tweet.get('Username', 'N/A')}")
        print(f"        {tweet.get('Text', '')[:80]}")
        print()



# Quest 4: Content Filter — keyword search

def search_tweets(tweets):
    keyword = input("\nEnter a search word: ").strip().lower()
    results = []

    for tweet in tweets:
        if keyword in tweet.get("Text", "").lower():
            results.append(tweet)

    print("\n" + "=" * 50)
    print(f"QUEST 4: Search Results for '{keyword}'")
    print("=" * 50)
    print(f"  Matching tweets: {len(results)}")
    for tweet in results:
        print(f"\n  @{tweet.get('Username', 'N/A')}  |  Likes: {tweet['Likes']}")
        print(f"  {tweet.get('Text', '')[:120]}")



# Main

if __name__ == "__main__":
    raw_tweets = load_tweets("twitter_dataset.csv")

    if len(raw_tweets) == 0:
        print("Dataset is empty or could not be loaded. Exiting.")
    else:
        clean_tweets = audit_data(raw_tweets)
        find_viral_post(clean_tweets)
        show_top10(clean_tweets)
        search_tweets(clean_tweets)

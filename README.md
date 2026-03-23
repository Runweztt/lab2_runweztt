# Lab 2 — The Social Media Data Detective

## Files
| File | Description |
|------|-------------|
| `data-detective.py` | Main Python analysis script |
| `feed-analyzer.sh` | Bash script for top-user analysis |
| `twitter_dataset.csv` | Dataset (download from Kaggle) |

---

## Requirements
- Python 3.x (no third-party libraries needed)
- A Unix-like terminal (Linux / macOS / WSL on Windows) for the shell script

---

## How to Run

### Python Script
```bash
# Make sure twitter_dataset.csv is in the same directory
python3 data-detective.py
```
The script will:
1. **Audit** the data (Quest 1) — fix/remove bad rows and report counts
2. **Find the viral post** (Quest 2) — print the tweet with the most Likes
3. **Show the Top 10** (Quest 3) — sorted by Likes using Bubble Sort
4. **Search tweets** (Quest 4) — prompt you for a keyword and list matches

### Shell Script
```bash
# Give the script execute permission (first time only)
chmod +x feed-analyzer.sh

# Run it
./feed-analyzer.sh
```
This prints the **Top 5 Most Active Users** (by number of posts) in `twitter_dataset.csv`.

---

## How the Custom Sorting Algorithm Works (Quest 3)

**Partial Selection Sort** is used to find the Top 10 most-liked tweets.  
The algorithm scans the entire unsorted portion of the list to find the tweet with the highest Likes and swaps it into the current front position; repeating this only 10 times (instead of n times) gives us the top 10 in O(10 × n) time, which is far faster than a full O(n²) sort on a large dataset while still being a hand-written algorithm with no built-in sort or max functions.

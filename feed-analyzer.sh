#!/usr/bin/env bash
FILE="twitter_dataset.csv"

if [ ! -f "$FILE" ]; then
  echo "Error: '$FILE' not found."
  exit 1
fi

echo "============================================"
echo " Top 5 Most Active Users in $FILE"
echo "============================================"

python3 -c "
import csv
counts = {}
with open('$FILE', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user = row['Username'].strip()
        counts[user] = counts.get(user, 0) + 1

sorted_users = sorted(counts.items(), key=lambda x: x[1], reverse=True)
for user, count in sorted_users[:5]:
    print(f'  {count:<6} tweets  ->  @{user}')
"

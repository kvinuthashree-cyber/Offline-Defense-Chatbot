import csv
import datetime

def auto_update_csv():
    filename = 'defense_data.csv'  # Path to your CSV file

    today = datetime.date.today().strftime('%Y-%m-%d')

    # Simulated "today's defense news" (offline fixed entry)
    news_entry = {
        "question": "What is the latest defense news as of today?",
        "answer": f"On {today}, the Indian Navy successfully completed sea trials for its new missile frigate under the Project 17A program. DRDO also announced progress in next-gen radar systems testing in Ladakh region."
    }

    # Check if today's news is already added
    already_updated = False
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if news_entry["question"] == row["question"] and news_entry["answer"] == row["answer"]:
                    already_updated = True
                    break
    except FileNotFoundError:
        # If the file does not exist, we'll create it below
        pass

    if not already_updated:
        # Append today's news to the CSV
        with open(filename, 'a', newline='', encoding='utf-8') as f:
            fieldnames = ['question', 'answer']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            try:
                # Check if file is empty, write header
                f.seek(0)
                if f.tell() == 0:
                    writer.writeheader()
            except:
                pass

            writer.writerow(news_entry)
            print("🟢 CSV updated with today’s defense news.")
    else:
        print("✅ CSV already up-to-date.")

# Import and name reference file
import csv

csv_file_path = r'C:\Users\micha\OneDrive\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv'

# Initialize variables to store data 
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
dates = []

# Open and read CSV file
with open(csv_file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader, None)

    for row_number, row in enumerate(csvreader, start=1):
        total_months += 1
        date = row[0]

        try:
            profit_loss = int(row[1])
        except ValueError:
            print(f"Skipping row {row_number} - Non-numeric value found in 'Profit/Losses' column: {row[1]}")
            continue

        net_total += profit_loss

        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)

        previous_profit_loss = profit_loss

# Check if there are no valid rows
if total_months == 0:
    print("No valid data found in the CSV file.")
else:
    average_change = sum(changes) / len(changes)

    max_increase = max(changes)
    max_decrease = min(changes)

    max_increase_date = dates[changes.index(max_increase)]
    max_decrease_date = dates[changes.index(max_decrease)]

    # print results
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${average_change:.2f}')
    print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')
    print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')
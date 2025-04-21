import os
import csv

# Hardcoded CSV file path (replace this with your own file path)
CSV_FILE_PATH = r"C:\Users\Ic\Desktop\Buzz Chatbot\complete database access chatbot\sample_1GB_data.csv"

# Check if the file exists
def file_exists(filepath):
    return os.path.isfile(filepath)

# Main chatbot function
def chatbot():
    print("Welcome! I'm Chatbot.\n")

    # Check if the file exists
    if not file_exists(CSV_FILE_PATH):
        print("❌ Chatbot: Uh-oh! I couldn't find the CSV file. 📂")
        print("📌 Please enter the relevant information about your dataset.")
        return

    # Open the file and read headers
    with open(CSV_FILE_PATH, 'r', encoding='utf-8', errors='ignore') as file:
        reader = csv.reader(file)
        headers = next(reader)

    # Display available commands
    print("📑 Available commands:")
    print("👉 'show number' — display that many rows")
    print("👉 'search keyword' — search rows for a keyword")
    print("👉 'showcols col1,col2,... number' — display specific columns and rows")
    print("👉 'row row_number column_name' — display a specific row and column")
    print("👉 'developer' — find out my developer's name")
    print("👉 'exit' — to quit the chatbot\n")

    # Start chatbot loop
    while True:
        user_input = input("🧑 You: ").lower()

        if user_input == 'exit':
            print("👋 Chatbot: Goodbye, see you next time!")
            break

        elif user_input.startswith('show '):
            try:
                num_rows = int(user_input[5:].strip())
                print(f"\n 🤖Chatbot: Showing {num_rows} rows:\n")
                with open(CSV_FILE_PATH, 'r', encoding='utf-8', errors='ignore') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for i, row in enumerate(reader):
                        print(row)
                        if i + 1 >= num_rows:
                            break
                print("\n 🤖Chatbot: Done.\n")
            except ValueError:
                print("❌ Chatbot: Please enter a valid number after 'show'.")

        elif user_input.startswith('search '):
            keyword = user_input[7:].strip()
            if keyword:
                print(f"\n🔍 Chatbot: Searching for '{keyword}':\n")
                with open(CSV_FILE_PATH, 'r', encoding='utf-8', errors='ignore') as file:
                    reader = csv.reader(file)
                    next(reader)
                    found = False
                    for row in reader:
                        if any(keyword.lower() in cell.lower() for cell in row):
                            print(row)
                            found = True
                    if not found:
                        print(f"🤖 Chatbot: No matches found for '{keyword}'.")
                print("\n 🤖Chatbot: Done.\n")
            else:
                print("❌ Chatbot: Enter a keyword after 'search'.")

        elif user_input.startswith('showcols '):
            try:
                parts = user_input[9:].strip().split()
                col_names = parts[0].split(',')
                num_rows = int(parts[1])

                with open(CSV_FILE_PATH, 'r', encoding='utf-8', errors='ignore') as file:
                    reader = csv.reader(file)
                    headers = next(reader)
                    col_indexes = [headers.index(col) for col in col_names]

                    print(f"\n📑 Chatbot: Showing {num_rows} rows for columns {col_names}:\n")
                    for i, row in enumerate(reader):
                        selected_data = [row[idx] for idx in col_indexes]
                        print(selected_data)
                        if i + 1 >= num_rows:
                            break
                print("\n✅ Chatbot: Done.\n")
            except (ValueError, IndexError):
                print("❌ Chatbot: Invalid format or unknown column name.")
                print("👉 Example: showcols Name,Email 5")

        elif user_input.startswith('row '):
            try:
                parts = user_input[4:].strip().split()
                row_number = int(parts[0])
                column_name = parts[1]

                with open(CSV_FILE_PATH, 'r', encoding='utf-8', errors='ignore') as file:
                    reader = csv.reader(file)
                    headers = next(reader)
                    if column_name not in headers:
                        print(f"❌ Chatbot: Column '{column_name}' not found.")
                        continue

                    row_data = list(reader)[row_number - 1]
                    col_index = headers.index(column_name)
                    print(f"\n🤖 Chatbot: Row {row_number}, Column '{column_name}' = {row_data[col_index]}")
                print("\n✅ Chatbot: Done.\n")
            except (ValueError, IndexError):
                print("❌ Chatbot: Invalid format or row number out of range.")
                print("👉 Example: row 14 Age")

        elif user_input in ["developer", "who is your developer?", "what is your developer name?"]:
            print("🤖 Chatbot: My developer is Rao Zain.")

        else:
            print("🤖 Chatbot: Please enter the relevant information about your dataset .")

# Run chatbot if executed directly
if __name__ == "__main__":
    chatbot()

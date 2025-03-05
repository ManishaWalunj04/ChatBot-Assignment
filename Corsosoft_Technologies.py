import datetime
import re


def is_valid_input(user_input, pattern):
    return bool(re.fullmatch(pattern, user_input.strip()))


def get_current_datetime():
    now = datetime.datetime.now()
    return now.strftime("%d %B %Y, %I:%M %p")


def process_list_operations():
    while True:
        user_input = input("Chatbot: Please enter a list of integers (comma-separated, integer): ")
        if not is_valid_input(user_input, r'\d+(,\s*\d+)*'):
            print("Chatbot: Error! The list must contain only integers separated by commas.")
            continue

        numbers = list(map(int, user_input.replace(" ", "").split(',')))  # Allow spaces after commas
        print(f"Chatbot:\n  Sum: {sum(numbers)}\n  Maximum: {max(numbers)}\n  Reversed List: {list(reversed(numbers))}")

        while True:
            remove_duplicates = input("Chatbot: Would you like to remove duplicates? (Yes/No)")
            if remove_duplicates == "Yes":
                numbers = sorted(set(numbers))
                print(f"Chatbot: Updated List: {numbers}")
                print(f"Chatbot:\n  Sum: {sum(numbers)}\n  Maximum: {max(numbers)}\n  Reversed List: {list(reversed(numbers))}")
            elif remove_duplicates == "No":
                break
            else:
                print("Chatbot: Keyword mismatch message - Enter correct keyword.")
        return


def generate_primes():
    while True:
        user_input = input("Chatbot: Enter the range (start and end, comma-separated): ")
        if not is_valid_input(user_input, r'\d+,\s*\d+'):
            print("Chatbot: Error! The input must be two integers separated by a comma.")
            continue
        start, end = map(int, user_input.replace(" ", "").split(','))
        primes = [num for num in range(start, end + 1) if
                  num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]
        print(f"Chatbot: Prime Numbers: {primes}")
        return


def search_history(chat_history):
    keyword = input("Chatbot: Enter the keyword to search in chat history: ").strip()
    if not keyword:
        print("Chatbot: Keyword mismatch message - Enter correct keyword..")
        return
    results = [line for line in chat_history if keyword.lower() in line.lower()]
    if results:
        print("Chatbot: Found the following lines:")
        for line in results:
            print(f"  - {line}")
    else:
        print("Chatbot: No matching history found.")


def main():
    chat_history = []
    command_count = {}
    print("Chatbot: Hello! I’m your assistant! How can I help you today?")

    while True:
        user_input = input("User: ")
        chat_history.append(f"User: {user_input}")

        if user_input in ["Hi", "Hello"]:
            print("Chatbot: Hi there! How can I help you today?")
        elif user_input in ["todays date", "time"]:
            print(f"Chatbot: {get_current_datetime()}")
        elif user_input == "list operation":
            process_list_operations()
            command_count["list operation"] = command_count.get("list operation", 0) + 1
        elif user_input == "generate primes":
            generate_primes()
            command_count["generate primes"] = command_count.get("generate primes", 0) + 1
        elif user_input == "Search History":
            search_history(chat_history)
            command_count["Search History"] = command_count.get("Search History", 0) + 1
        elif user_input == "bye":
            print("Chatbot: Here’s a summary of your session:")
            print(f"   - Commands Used: {sum(command_count.values())}")
            if command_count:
                most_used = max(command_count, key=command_count.get)
                print(f"   - Most Frequent Command: {most_used}")

            while True:
                save_summary = input("Chatbot: Do you want to save this summary? (yes/no) ").strip().lower()
                if save_summary == "yes":
                    filename = f"summary_{datetime.datetime.now().strftime('%d%m%Y')}.txt"
                    with open(filename, "w") as file:
                        file.write("Chatbot Session Summary:\n")
                        file.write(f"Commands Used: {sum(command_count.values())}\n")
                elif save_summary == "no":
                    break
                else:
                    print("Chatbot: Please enter 'yes' or 'no'.")
            print("Chatbot: Bye, have a good day!!")
            break
        else:
            print("Chatbot: Keyword mismatch message - Enter correct keyword.")


if __name__ == "__main__":
    main()







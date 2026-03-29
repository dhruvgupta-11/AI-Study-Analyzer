from core.analyzer import (
    get_subjects,
    get_topics,
    get_dependencies,
    get_learning_path
)

from ml.predict import predict_difficulty
from core.utils import print_list, print_message, print_separator


def show_subjects():
    print_list("Available Subjects", get_subjects())


def show_topics(subject):
    print_list("Topics", get_topics(subject))


def show_dependencies(subject, topic):
    prereq = get_dependencies(subject, topic)

    if prereq is None:
        print_message("Topic not found")
    elif prereq == []:
        print_message("No prerequisites required")
    else:
        print_list("Prerequisites", prereq)


def show_learning_path(subject, topic):
    path = get_learning_path(subject, topic)
    print_list("Learning Path", path)


def show_difficulty(text):
    difficulty = predict_difficulty(text)
    print_message(f"Estimated Difficulty: {difficulty}")


def main():
    while True:
        print_separator()
        print("===== AI Study Analyzer =====")
        print("1. Show Subjects")
        print("2. Show Topics (by Subject)")
        print("3. Show Prerequisites")
        print("4. Show Learning Path")
        print("5. Check Difficulty")
        print("6. Full Analysis")
        print("7. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            show_subjects()

        elif choice == "2":
            show_subjects()
            subject = input("\nEnter subject: ").strip()

            if subject not in get_subjects():
                print_message("Invalid subject")
                continue

            show_topics(subject)

        elif choice == "3":
            show_subjects()
            subject = input("\nEnter subject: ").strip()

            if subject not in get_subjects():
                print_message("Invalid subject")
                continue

            show_topics(subject)
            topic = input("\nEnter topic: ").strip()

            show_dependencies(subject, topic)

        elif choice == "4":
            show_subjects()
            subject = input("\nEnter subject: ").strip()

            if subject not in get_subjects():
                print_message("Invalid subject")
                continue

            show_topics(subject)
            topic = input("\nEnter topic: ").strip()

            show_learning_path(subject, topic)

        elif choice == "5":
            text = input("\nEnter topic/question: ").strip()
            show_difficulty(text)

        elif choice == "6":
            show_subjects()
            subject = input("\nEnter subject: ").strip()

            if subject not in get_subjects():
                print_message("Invalid subject")
                continue

            show_topics(subject)
            topic = input("\nEnter topic: ").strip()

            if topic not in get_topics(subject):
                print_message("Invalid topic")
                continue

            show_difficulty(topic)
            show_dependencies(subject, topic)
            show_learning_path(subject, topic)

        elif choice == "7":
            print_message("Exiting...")
            break

        else:
            print_message("Invalid choice")


if __name__ == "__main__":
    main()
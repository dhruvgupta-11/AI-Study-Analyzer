def print_list(title, items):
    print(f"\n{title}:")
    for item in items:
        print("-", item)


def print_message(message):
    print(f"\n{message}")


def print_separator():
    print("\n" + "=" * 30)


def validate_subject(subject, subjects_list):
    return subject in subjects_list


def validate_topic(topic, topics_list):
    return topic in topics_list
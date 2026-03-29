from data.dependencies import dependencies
from data.topics import topics


def get_subjects():
    return list(topics.keys())


def get_topics(subject):
    return topics.get(subject, [])


def get_dependencies(subject, topic):
    return dependencies[subject].get(topic, None)


def get_learning_path(subject, topic, visited=None):
    if visited is None:
        visited = []

    prereq = get_dependencies(subject, topic)

    if prereq:
        for p in prereq:
            if p not in visited:
                get_learning_path(subject, p, visited)

    if topic not in visited:
        visited.append(topic)

    return visited
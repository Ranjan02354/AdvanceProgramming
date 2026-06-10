from typing import List, Dict, Set
from collections import defaultdict
from functools import reduce


def total_time_per_user(logs: List[Dict]) -> Dict[str, float]:
    grouped = defaultdict(list)

    for log in logs:
        grouped[log["user"]].append(log["duration"])

    return {
        user: reduce(lambda x, y: x + y, durations, 0.0)
        for user, durations in grouped.items()
    }


def most_active_users(logs: List[Dict], k: int) -> List[str]:
    totals = total_time_per_user(logs)

    sorted_users = sorted(
        totals.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return [user for user, _ in sorted_users[:k]]


def unique_actions(logs: List[Dict]) -> Set[str]:
    return {log["action"] for log in logs}


if __name__ == "__main__":

    logs = [
        {"user": "CSB24077", "action": "YouTube", "duration": 1.5},
        {"user": "CSB24017", "action": "Instagram", "duration": 2.0},
        {"user": "CSB24067", "action": "WhatsApp", "duration": 0.5},
        {"user": "CSB24071", "action": "YouTube", "duration": 3.0},
        {"user": "CSB24080", "action": "Facebook", "duration": 1.0},
        {"user": "CSB24062", "action": "Chrome", "duration": 2.5},
    ]

    print("Total time per user:")
    print(total_time_per_user(logs))

    print("\nMost active users:")
    print(most_active_users(logs, 2))

    print("\nUnique actions:")
    print(unique_actions(logs))
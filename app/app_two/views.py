"""Small views module providing a remove_duplicates helper for tests.

We include a tiny, self-contained implementation here so tests can import
`app_two.views.remove_duplicates` without relying on imports across sibling
packages. The function preserves the order of first occurrences.
"""

from typing import Iterable, List, TypeVar

T = TypeVar("T")


def remove_duplicates(seq: Iterable[T]) -> List[T]:
    """Return a new list with duplicates removed, preserving order.

    Args:
        seq: Any iterable of hashable items.

    Returns:
        A list with only the first occurrence of each item kept.
    """
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


__all__ = ["remove_duplicates"]

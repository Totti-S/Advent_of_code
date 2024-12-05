import typing as t

def nums(a: list[str]) -> list[int]:
    return list(map(int, a))

def is_sublist(a: list[t.Any], b: list[t.Any]) -> bool:
    return all([item in b for item in a])
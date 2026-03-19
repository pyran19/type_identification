from __future__ import annotations

from .solver import DEFENDING_TYPE_NAMES, find_minimum_attack_type_sets


def main() -> None:
    minimum_count, attack_sets = find_minimum_attack_type_sets()
    print(f"Target defending types: {', '.join(DEFENDING_TYPE_NAMES)}")
    print(f"Minimum required attack types: {minimum_count}")
    print("Attack type sets that achieve the minimum:")
    for attack_set in attack_sets:
        print(f"- {', '.join(attack_set)}")

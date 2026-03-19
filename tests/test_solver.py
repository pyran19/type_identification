from type_identification.solver import (
    build_signature_map,
    find_minimum_attack_type_sets,
    is_distinguishable,
)


def test_example_fire_water_grass_requires_two_attack_types() -> None:
    candidates = ("fire", "water", "grass")

    assert not is_distinguishable(("water",), candidates)
    assert is_distinguishable(("fire", "water"), candidates)

    minimum_count, attack_sets = find_minimum_attack_type_sets(
        candidate_attack_types=("fire", "water", "grass"),
        target_types=candidates,
    )

    assert minimum_count == 2
    assert ("fire", "water") in attack_sets


def test_signature_map_matches_expected_pattern() -> None:
    signatures = build_signature_map(("fire", "water"))

    assert signatures["fire"] == (0.5, 2.0)
    assert signatures["water"] == (0.5, 0.5)
    assert signatures["grass"] == (2.0, 0.5)


def test_full_type_search_returns_stable_minimum() -> None:
    minimum_count, attack_sets = find_minimum_attack_type_sets()

    assert minimum_count == 4
    assert attack_sets == [
        ("fire", "electric", "fighting", "psychic"),
        ("grass", "ice", "fighting", "bug"),
        ("grass", "fighting", "bug", "rock"),
        ("ice", "fighting", "poison", "bug"),
    ]

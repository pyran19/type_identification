from type_identification.solver import (
    ATTACK_TYPE_NAMES,
    TYPELESS_DEFENDING_TYPE,
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


def test_typeless_defender_is_all_neutral() -> None:
    signatures = build_signature_map(("normal", "fire", "water", "electric"))

    assert signatures[TYPELESS_DEFENDING_TYPE] == (1.0, 1.0, 1.0, 1.0)


def test_full_type_search_returns_stable_minimum() -> None:
    minimum_count, attack_sets = find_minimum_attack_type_sets()

    assert minimum_count == 4
    assert attack_sets == [("fire", "electric", "fighting", "psychic")]


def test_default_search_uses_only_standard_attack_types() -> None:
    minimum_count, attack_sets = find_minimum_attack_type_sets()

    assert minimum_count <= len(ATTACK_TYPE_NAMES)
    assert all(set(attack_set).issubset(set(ATTACK_TYPE_NAMES)) for attack_set in attack_sets)

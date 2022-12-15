from common import Position


def test_position_manhattan_distance() -> None:
    assert Position(4, 1).manhattan_distance(Position(0, 0)) == 5

import pytest
from leaderboard import Leaderboard


def test_add_player():
    lb = Leaderboard()
    lb.add_player("Alice")
    assert len(lb) == 1


def test_add_player_with_initial_score():
    lb = Leaderboard()
    lb.add_player("Alice", initial_score=500)
    assert lb.get_top_n(1) == [("Alice", 500)]


def test_record_match_updates_scores():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    lb.add_player("Bob", 100)
    lb.record_match("Alice", "Bob")
    assert lb.get_top_n(2) == [("Alice", 110), ("Bob", 90)]


def test_get_rank():
    lb = Leaderboard()
    lb.add_player("Alice", 300)
    lb.add_player("Bob", 100)
    lb.add_player("Carol", 200)
    assert lb.get_rank("Alice") == 1
    assert lb.get_rank("Carol") == 2
    assert lb.get_rank("Bob") == 3

def test_add_player_negative_score_raises():
    lb = Leaderboard()
    with pytest.raises(ValueError):
        lb.add_player("Alice", initial_score=-5)
 
 
def test_add_player_duplicate_raises():
    lb = Leaderboard()
    lb.add_player("Alice")
    with pytest.raises(ValueError):
        lb.add_player("Alice")
 
 
 
def test_record_match_unregistered_winner_raises():
    lb = Leaderboard()
    lb.add_player("Alice")
    with pytest.raises(KeyError):
        lb.record_match("Ghost", "Alice")
 
 
def test_record_match_unregistered_loser_raises():
    lb = Leaderboard()
    lb.add_player("Alice")
    with pytest.raises(KeyError):
        lb.record_match("Alice", "Ghost")
 
 
def test_record_match_zero_points_raises():
    lb = Leaderboard()
    lb.add_player("Alice")
    lb.add_player("Bob")
    with pytest.raises(ValueError):
        lb.record_match("Alice", "Bob", points=0)
 
 
 
def test_get_rank_unregistered_raises():
    lb = Leaderboard()
    with pytest.raises(KeyError):
        lb.get_rank("Ghost")
 
 
 
def test_get_top_n_negative_raises():
    lb = Leaderboard()
    with pytest.raises(ValueError):
        lb.get_top_n(-1)
 
 
def test_get_top_n_returns_sorted():
    lb = Leaderboard()
    lb.add_player("Alice", 30)
    lb.add_player("Bob", 50)
    lb.add_player("Carol", 10)
    result = lb.get_top_n(2)
    assert result == [("Bob", 50), ("Alice", 30)]
 
 
 
def test_get_percentile_unregistered_raises():
    lb = Leaderboard()
    with pytest.raises(KeyError):
        lb.get_percentile("Ghost")
 
 
def test_get_percentile_single_player():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    assert lb.get_percentile("Alice") == 100.0
 
 
def test_get_percentile_multiple_players():
    lb = Leaderboard()
    lb.add_player("Alice", 10)
    lb.add_player("Bob", 20)
    lb.add_player("Carol", 30)
    assert lb.get_percentile("Alice") == 0.0
    assert lb.get_percentile("Carol") == round(2 / 3 * 100, 2)
 
 
 
def test_apply_bonus_unregistered_raises():
    lb = Leaderboard()
    with pytest.raises(KeyError):
        lb.apply_bonus("Ghost", 1.5)
 
 
def test_apply_bonus_zero_multiplier_raises():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    with pytest.raises(ValueError):
        lb.apply_bonus("Alice", 0)
 
 
def test_apply_bonus_updates_score():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    lb.apply_bonus("Alice", 1.5)
    assert lb.get_top_n(1) == [("Alice", 150)]

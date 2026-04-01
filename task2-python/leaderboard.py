class Leaderboard:
    """A competitive gaming / hackathon leaderboard."""

    def __init__(self):
        # name -> {"score": int, "wins": int, "losses": int}
        self._players = {}

    def add_player(self, name: str, initial_score: int = 0) -> None:
        """Register a new player with an optional starting score."""
        if initial_score < 0:
            raise ValueError("Initial score cannot be negative")
        if name in self._players:
            raise ValueError(f"Player '{name}' is already registered")
        self._players[name] = {"score": initial_score, "wins": 0, "losses": 0}

    def record_match(self, winner: str, loser: str, points: int = 10) -> None:
        """Record a match outcome, awarding `points` to winner and deducting from loser."""
        if winner not in self._players:
            raise KeyError(f"Player '{winner}' is not registered")
        if loser not in self._players:
            raise KeyError(f"Player '{loser}' is not registered")
        if points <= 0:
            raise ValueError("Points must be positive")
        self._players[winner]["score"] += points
        self._players[winner]["wins"] += 1
        self._players[loser]["score"] = max(0, self._players[loser]["score"] - points)
        self._players[loser]["losses"] += 1

    def get_rank(self, name: str) -> int:
        """Return the 1-based rank of the player (highest score = rank 1)."""
        if name not in self._players:
            raise KeyError(f"Player '{name}' is not registered")
        player_score = self._players[name]["score"]
        return sum(1 for p in self._players.values() if p["score"] > player_score) + 1

    def get_top_n(self, n: int) -> list:
        """Return a list of (name, score) tuples for the top n players, highest score first."""
        if n < 0:
            raise ValueError("n must be non-negative")
        ranked = sorted(
            self._players.items(),
            key=lambda item: item[1]["score"],
            reverse=True,
        )
        return [(name, data["score"]) for name, data in ranked[:n]]

    def get_percentile(self, name: str) -> float:
        """Return the player's percentile rank (0.0–100.0, higher is better)."""
        if name not in self._players:
            raise KeyError(f"Player '{name}' is not registered")
        total = len(self._players)
        if total == 1:
            return 100.0
        player_score = self._players[name]["score"]
        below = sum(1 for p in self._players.values() if p["score"] < player_score)
        return round(below / total * 100, 2)

    def apply_bonus(self, name: str, multiplier: float) -> None:
        """Multiply a player's score by `multiplier` (e.g., 1.5 for a 50% bonus)."""
        if name not in self._players:
            raise KeyError(f"Player '{name}' is not registered")
        if multiplier <= 0:
            raise ValueError("Multiplier must be positive")
        self._players[name]["score"] = int(self._players[name]["score"] * multiplier)

    def get_win_rate(self, name: str) -> float:
        """Return the player's win rate as a fraction (0.0–1.0), or 0.0 if no games played."""
        if name not in self._players:
            raise KeyError(f"Player '{name}' is not registered")
        p = self._players[name]
        total = p["wins"] + p["losses"]
        return p["wins"] / total if total > 0 else 0.0

    def reset(self) -> None:
        """Remove all players from the leaderboard."""
        self._players.clear()

    def __len__(self) -> int:
        return len(self._players)

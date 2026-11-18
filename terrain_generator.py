"""Generate canonical terrain deterministically from specification and seed."""
from src.api import Terrain, TerrainGenerationSpec


class TerrainGenerator:
    """Keep state local; identical inputs must also agree across fresh instances."""

    def __init__(self) -> None:
        # No state needed: the same input always gives the same terrain.
        pass

    def generate_terrain(self, specification: TerrainGenerationSpec, seed: int) -> Terrain:
        # Straight path: every cell is floor ('.'), one row or one column wide.
        row = "." * specification.columns
        rows = tuple(row for _ in range(specification.rows))
        return Terrain(rows)
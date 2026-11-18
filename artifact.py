"""TODO: implement initial artifact data; introductory gameplay has no artifacts."""
from src.api import ArtifactDefinition, Position


class Artifact:
    """Expose read-only canonical identity, position, and nonnegative value."""

    def __init__(self, artifact_id: str, position: Position, value: int) -> None:
        # raise NotImplementedError("TODO Artifact: implement constructor and properties")
        ArtifactDefinition(artifact_id, position, value)
        self._artifact_id = artifact_id
        self._position = position
        self._value = value

    @property
    def artifact_id(self) -> str:
        # raise NotImplementedError("TODO Artifact.artifact_id")
        return self._artifact_id

    @property
    def position(self) -> Position:
        # raise NotImplementedError("TODO Artifact.position")
        return self._position

    @property
    def value(self) -> int:
        # raise NotImplementedError("TODO Artifact.value")
        return self._value
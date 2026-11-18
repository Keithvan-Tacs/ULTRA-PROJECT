"""TODO: select one public action from each immutable world observation."""
from src.api import WorldAction, WorldActionType, WorldSnapshot


class AgentController:
    """A new controller is constructed for each run; arrival still needs EXIT."""

    def __init__(self) -> None:
        # raise NotImplementedError("TODO AgentController: implement constructor and choose_action")
        pass

    def choose_action(self, state: WorldSnapshot, agent_id: str) -> WorldAction:
        # Return an exact WorldAction; illegal responses are rejected, not changed to WAIT.
        # raise NotImplementedError("TODO AgentController.choose_action")
        here = state.agent_position
        goal = state.exit_position

        # On the exit: arriving is not enough, so return EXIT.
        if here == goal:
            return WorldAction(WorldActionType.EXIT)

        # Otherwise step toward the exit using the real coordinates.
        if goal.column > here.column:
            return WorldAction(WorldActionType.MOVE_EAST)
        if goal.column < here.column:
            return WorldAction(WorldActionType.MOVE_WEST)
        if goal.row > here.row:
            return WorldAction(WorldActionType.MOVE_SOUTH)
        return WorldAction(WorldActionType.MOVE_NORTH)
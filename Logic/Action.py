from Util.HistoryLogger import HistoryLogger


class Action(object):
    """Tuple of actor and associated action that should be performed"""
    def __init__(self, actor, action):
        self.actor = actor
        self.action = action
        self.logger = HistoryLogger()

    def perform(self):
        self.actor.performAction(self.action)
        self.logger.log(self.actor.name + " " + self.action.name + "\n")

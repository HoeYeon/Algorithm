from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __init__(self, name: str, skills: List[str], load: int):
        self._name = name
        self._skills = skills
        self._load = load

    def __str__(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    def __init__(self, ID: str, restrictions: List[str]):
        self._ID = ID
        self._restrictions = restrictions


class FinderPolicy(object):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        pass


class LeastLoadedAgent(FinderPolicy):
    def __init__(self):
        pass

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        target = sorted(agents, key=getLoaded)
        target[0]._load += 1
        print("Least Loaded", target[0])
        return target[0]


class LeastFlexibleAgent(FinderPolicy):
    def __init__(self):
        print("Lease")

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        print(ticket._restrictions)
        agents = list(filter(lambda agent: all(
            restriction in agent._skills for restriction in ticket._restrictions), agents))
        target = sorted(agents, key=getSkills)
        target[0]._load += 1
        print("Least Flexible", target[0])
        return target[0]


def getLoaded(obj):
    return obj._load


def getSkills(obj):
    return len(obj._skills)


ticket = Ticket(ID="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

least_loaded_policy = LeastLoadedAgent()
# returns the Agent with name "B" because of their currently lower load.
least_loaded_policy.find(ticket, [agent1, agent2])

least_flexible_policy = LeastFlexibleAgent()
# returns the Agent with name "A" because of their lower flexibility.
least_flexible_policy.find(ticket, [agent1, agent2])

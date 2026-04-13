MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

agents = []

for codename, score in zip(codenames, scores):
    agents.append(Agent(codename, score))

agents.sort(lambda x: x.score)

print(agents[0].codename, agents[0].score)
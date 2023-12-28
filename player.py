class Player():
    def __init__(self, idx: int = None) -> None:
        self._id = idx
        self._balance = 0
        self.rewards = []

    @property
    def id(self):
        return self._id

    def reward(self):
        return self.rewards

    def add_reward(self, reward):
        self.rewards.append(str(reward))

    def balance(self):
        return self._balance

    def set_balance(self, amount):
        self._balance = int(amount)

    def add_to_balance(self, amount=0):
        self._balance += int(amount)

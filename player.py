class Player():
    """
    Class Player contains atributes:

    param id: Id of a player
    type id: int

    param balance: Player's balance durring a round
    type balance: int

    param rewards: rewards player got by spinning the wheel
                   and giving correct consonant
    type rewards: list[str]

    param total balance: Sum of player's balances in won rounds
    type total balance: int

    """
    def __init__(self, idx: int = None) -> None:
        """
        Creates instance of Player
        """
        self._id = idx
        self._balance = 0
        self.rewards = []
        self._total_balance = 0

    @property
    def id(self):
        """
        Returns id of a player
        """
        return self._id

    def reward(self):
        """
        Returns list of player's rewards
        """
        return self.rewards

    def add_reward(self, reward):
        """
        Adds won reward to player's rewards list
        """
        self.rewards.append(str(reward))

    def clear_reward(self, reward):
        """
        Removes all rewards from player's rewards list
        """
        self.rewards.clear()

    def balance(self):
        """
        Returns player's current balance
        """
        return self._balance

    def set_balance(self, amount):
        """
        Sets player's current balance
        """
        self._balance = int(amount)

    def add_to_balance(self, amount=0):
        """
        Adds given amount to player's current balance
        """
        self._balance += int(amount)

    def total_balance(self):
        """
        Returns player's total balance
        """
        return self._total_balance

    def add_to_total_balance(self, amount=0):
        """
        Adds given amount to player's total balance
        """
        self._total_balance += int(amount)

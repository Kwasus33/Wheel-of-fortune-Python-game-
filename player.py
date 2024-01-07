class Player():
    """
    Class Player contains atributes:

    param id: Id of a player
    type id: int

    param balance: Player's balance durring a round
    type balance: int

    param total balance: Sum of player's balances in won rounds
    type total balance: int

    param rewards: rewards player got by spinning the wheel and giving correct
                   consonant, for temporary storage - is cleared every round
    type rewards: list[str]

    param total rewards: rewards player got in won rounds,
                         saves data from param rewards when player wins a round
    type total rewards: list[str]

    """
    def __init__(self, idx: int = None) -> None:
        """
        Creates instance of Player
        """
        self._id = idx
        self._balance = 0
        self._total_balance = 0
        self._rewards = []
        self._total_rewards = []

    @property
    def id(self) -> int:
        """
        Returns id of a player
        """
        return self._id

    def reward(self) -> list:
        """
        Returns 'temporary' list of player's rewards got during round
        """
        return self._rewards

    def add_reward(self, reward: str) -> None:
        """
        Adds got reward to player's rewards list
        """
        self._rewards.append(str(reward))

    def remove_rewards(self) -> None:
        """
        Removes all rewards from player's rewards list
        """
        self._rewards.clear()

    def total_rewards(self) -> list:
        """
        Returns list of player's rewards collected in won rounds
        """
        return self._total_rewards

    def set_total_rewards(self, rewards: list) -> None:
        """
        Adds rewards collected during won round to list of player's won rewards
        """
        for reward in rewards:
            self._total_rewards.append(reward)

    def balance(self) -> int:
        """
        Returns player's current balance
        """
        return self._balance

    def set_balance(self, amount) -> None:
        """
        Sets player's current balance
        """
        self._balance = int(amount)

    def add_to_balance(self, amount=0) -> None:
        """
        Adds given amount to player's current balance
        Amount defaults to zero
        """
        self._balance += int(amount)

    def total_balance(self) -> int:
        """
        Returns player's total balance
        """
        return self._total_balance

    def add_to_total_balance(self, amount=0) -> None:
        """
        Adds given amount to player's total balance
        """
        self._total_balance += int(amount)

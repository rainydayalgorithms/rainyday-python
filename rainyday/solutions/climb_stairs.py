def climb(n: int) -> int:
    """
    :type n: int
    :rtype: int
    """

    # Climb Stairs
    # You can take either 1 or 2 steps at a time to get to the top of the stairs
    # Return how many different stair-climbing combinations there are for n stairs

    stair_combos = [None] * (n+1)
    stair_combos[0] = 1
    stair_combos[1] = 1
    for i in range(2, n + 1):
        stair_combos[i] = stair_combos[i - 1] + stair_combos[i - 2]

    return stair_combos[n]

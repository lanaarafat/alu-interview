def rain(walls):
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    # Calculate the maximum height to the left of each wall
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Calculate the maximum height to the right of each wall
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate the amount of water retained at each position
    water_retained = 0
    for i in range(n):
        water_retained += min(left_max[i], right_max[i]) - walls[i]

    return water_retained

# Test cases
walls1 = [0, 1, 0, 2, 0, 3, 0, 4]
walls2 = [2, 0, 0, 4, 0, 0, 1, 0]

print(rain(walls1))
print(rain(walls2))

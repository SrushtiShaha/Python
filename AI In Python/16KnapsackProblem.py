def solve_knapsack():
    # Item data: (Name, Points, Weight)
    items = [
        ("pocketknife", 10, 1),
        ("Beans", 20, 5),
        ("potatoes", 15, 10),
        ("Unions", 2, 1),
        ("sleeping bag", 30, 7),
        ("Rope", 10, 5),
        ("compass", 30, 1)
    ]

    max_weight = 20
    n = len(items)

    # Initialize DP table
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        name, points, weight = items[i - 1]

        for w in range(max_weight + 1):
            if weight <= w:
                dp[i][w] = max(
                    points + dp[i - 1][w - weight],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack selected items
    selected_items = []
    w = max_weight

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, points, weight = items[i - 1]
            selected_items.append(items[i - 1])
            w -= weight

    # Results
    print("--- Survival Backpack Optimization ---")
    print(f"{'Item':<15} | {'Points':<8} | {'Weight':<8}")
    print("-" * 35)

    total_weight = 0

    for name, p, wt in selected_items:
        print(f"{name:<15} | {p:<8.2f} | {wt:<8.2f}")
        total_weight += wt

    print("-" * 35)
    print(f"Total Survival Points: {dp[n][max_weight]:.2f}")
    print(f"Total Weight Used: {total_weight:.2f} / {max_weight} kg")


if __name__ == "__main__":
    solve_knapsack()
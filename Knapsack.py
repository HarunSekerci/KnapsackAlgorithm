def knapsackFunction(values, weights, capacity):
    count = len(weights)  # Eleman sayısı
    # Dinamik programlama matrisinin oluşturulması
    Matris = [[0 for temp in range(capacity+1)]for temp in range(count + 1)]
    #print(Matris)
    for i in range(1, count + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                Matris[i][j] = max(Matris[i - 1][j], values[i - 1] + Matris[i - 1][j - weights[i - 1]])
            else:
                Matris[i][j] = Matris[i - 1][j]

    """for i in range(count + 1):
        for j in range(capacity + 1):
               print(Matris[i][j], end=" ")
        print("\n")"""
    maxValue = Matris[count][capacity]
    usedWeights = []
    j = capacity
    for i in range(count, 0, -1):
        if Matris[i][j] != Matris[i - 1][j]:
            usedWeights.append(weights[i - 1])
            j -= weights[i - 1]
            #print("Kullanılan ağırlık ",weights[i-1])

    return maxValue, usedWeights

# Verilerin Alınması
with open("veriler.txt", "r") as file:
    lines = file.readlines()
    values = list(map(int, lines[0].strip().split(",")))
    weights = list(map(int, lines[1].strip().split(",")))
    capacity = int(lines[2].strip())


maxValue, usedWeights = knapsackFunction(values, weights, capacity)

print("Maximum değer:", maxValue)
print("Kullanılan ağırlıklar:", ", ".join(map(str, usedWeights)))

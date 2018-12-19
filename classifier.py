from decimal import Decimal, getcontext


def distance(item1, item2):
    # Returns distance between two values
    squared_difference = 0
    for i in range(len(item1)):
        squared_difference += (item1[i] - item2[i]) ** 2
    final_distance = squared_difference ** 0.5
    return final_distance


def min_max_normalize(lst):
    # Converts data to a value between 0 - 1
    getcontext().prec = 15
    minimum = min(lst)
    maximum = max(lst)
    normalized_values = []
    for x in lst:
        normalized_values.append(float(Decimal(x-minimum) / Decimal(maximum-minimum)))
    return normalized_values


def classify(unknown, dataset, labels, k):
    # First determine distance to all items in dataset
    distances = []
    for item in dataset:
        data_point = min_max_normalize(dataset[item])
        norm_unknown = min_max_normalize(unknown)
        distance_to_point = distance(data_point, norm_unknown)
        distances.append([distance_to_point, item])
    distances.sort()

    # Then take only the k closest points
    neighbors = distances[0:k]
    group1 = 0
    group2 = 0
    for neighbor in neighbors:
        title = neighbor[1]
        if labels[title] == 0:
            group1 += 1
        elif labels[title] == 1:
            group2 += 1

    # Return 0 (group1) or 1 (group2)
    if group2 > group1:
        return 1
    else:
        return 0

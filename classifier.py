from decimal import Decimal, getcontext


def distance(item1, item2):
    # Returns distance between two values
    squared_difference = 0
    for i in range(len(item1)):
        squared_difference += (item1[i] - item2[i]) ** 2
    final_distance = squared_difference ** 0.5
    return final_distance


def min_max_normalize(dict):
    # Converts data in dictionary to values between 0 - 1
    getcontext().prec = 15
    fields_count = len(dict[list(dict.keys())[0]])

    # For each column in dataset:
    for i in range(fields_count):

         # Find minimum:
        minimum = Decimal('Infinity')
        for key in dict.keys():
            if (dict[key][i] < minimum):
                minimum = dict[key][i]

        # Find maximum:
        maximum = Decimal('-Infinity')
        for key in dict.keys():
            if (dict[key][i] > maximum):
                maximum = dict[key][i]

        # Normalize each value:
        for key in dict.keys():
            dict[key][i] = float(Decimal(dict[key][i]-minimum) / Decimal(maximum-minimum))

    return dict


def classify(unknown, dataset, labels, k):
    # First determine distance to all items in dataset
    distances = []

    # Normalize dataset with unknown, then separate unknown:
    dataset["unknown"] = unknown
    normalized_data = min_max_normalize(dataset)
    norm_unknown = normalized_data.pop("unknown")

    for item in normalized_data:
        data_point = normalized_data[item]
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

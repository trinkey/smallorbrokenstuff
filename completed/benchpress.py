# This program prioritizes the weights at the far left (bescides the bar + clips) of the list.
# Because of how this is coded, you can have as many or as few different weights as you want.
# The first 3 from each list are as follows:
# 1 - bar
# 2 - left clip
# 3 - right clip
weights = [20, 5, 5, 25, 20, 15, 10, 5, 2.5, 2, 1.5, 1, 0.5]
icon = ["---", "<", ">", "R", "B", "Y", "G", "W", "r", "b", "y", "g", "w"]
clipsRequired = True

while True:
    output = icon[0]
    try:
        weight = int(round(float(input("Weight (kg): "))))
        if clipsRequired:
            weight -= (weights[1] + weights[2])
        weight -= weights[0]
        if weight >= 0:
            for i in range(len(weights) - 3):
                while weight >= 2 * weights[i + 3]:
                    output = icon[i + 3] + output + icon[i + 3]
                    weight -= (weights[i + 3] * 2)
            if clipsRequired:
                output = icon[1] + output + icon[2]
            print(output)
        else:
            print("Too light of a weight, sorry :(")
    except:
        print("Bad input")
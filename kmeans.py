#!/usr/bin/env python3

import random
import matplotlib.pyplot as plt
import math

values = []
clusters = []
num_clusters = 4
colors = ["ro", "go", "co", "mo", "yo", "ko", "wo"]


def plot_chart():
    plt.clf()
    for i in range(len(values)):
        plt.plot(values[i][0], values[i][1], values[i][2])

    for i in range(len(clusters)):
        plt.plot(clusters[i][0], clusters[i][1], colors[i], markersize=22)
    plt.draw()


def calculate_distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calculate_colours():
    for i in range(len(values)):
        distances = []
        for j in range(len(clusters)):
            distance = calculate_distance(
                values[i][0], clusters[j][0], values[i][1], clusters[j][1]
            )
            distances.append([distance, j])
        min_distance = min(distances)
        values[i][2] = colors[min_distance[1] % len(colors)]


def calculate_centroids():
    for i in range(len(clusters)):
        x = 0
        y = 0
        count = 0
        for j in range(len(values)):
            if values[j][2] == colors[i]:
                x += values[j][0]
                y += values[j][1]
                count += 1
        if count != 0:
            clusters[i][0] = x / count
            clusters[i][1] = y / count


def on_key(event):
    if event.key == " ":
        calculate_centroids()
        calculate_colours()
        plot_chart()
    elif event.key == "r":
        create_random_values()
        create_random_clusters()
        plot_chart()


def create_random_clusters():
    clusters.clear()
    for _ in range(num_clusters):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        clusters.append([x, y])


def create_random_values():
    values.clear()
    for _ in range(50):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        values.append([x, y, "bo"])


create_random_values()
create_random_clusters()

fig, ax = plt.subplots()
plot_chart()
plt.connect("key_press_event", on_key)
plt.show()

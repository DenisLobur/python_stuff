from die import Die
import plotly.express as px

# Create two D6 dice

die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.

# Using for loop
# results = []
# for roll_num in range(50_000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# Using for-comprehension
results = [die_1.roll() + die_2.roll() for _ in range(50_000)]

# Analyze the results.

max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)

# Using for loop
# frequencies = []
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# Using for-comprehension
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

# Save result as HTML file
# fig.write_html('dice_visual_d6d10.html')

# Show results
fig.show()
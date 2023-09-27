plt.figure(figsize=(6, 6))
sns.boxplot(data=df[['food_preparation_time', 'delivery_time']], orient="v", color='#F07C02', width=0.5) # i like the smaller width from a purely aesthetic standpoint

plt.title('The Ranges of Food Prep and Delivery Times')
plt.ylim(0, 40)
plt.ylabel('Minutes')

# remove the top and right spines (borders)
ax = plt.gca() # for making customizations to our axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.set_xticks([]) # remove x-axis ticks
# Add text annotations for the labels under each box
label_positions = [0, 1]  # positioning: 0 is the left box, and 1 is the right box, since these are categorical
label_texts = ['Food Prep', 'Delivery']  # set the labels for the left and right boxes
for i in range(len(label_positions)):
    plt.text(label_positions[i], 0, label_texts[i], ha='center', va='center', fontsize=10)


# add solid red lines to highlight the range of food prep and delivery times
plt.vlines(0.3, ymin=df['food_preparation_time'].min(), ymax=df['food_preparation_time'].max(), color='red', linewidth=1.2)
plt.vlines(1.3, ymin=df['delivery_time'].min(), ymax=df['delivery_time'].max(), color='red', linewidth=1.2)
# adding 0.3 to the x coordinates so that the lines are plotted just to the right of the box and whisker plots

# Add red text labels to the left of the red lines denoting their lengths
line_length_var1 = df['food_preparation_time'].max() - df['food_preparation_time'].min()
line_length_var2 = df['delivery_time'].max() - df['delivery_time'].min()
# centering the annotations to their corresponding lines along the y axis
y_coord1 = df['food_preparation_time'].min() + ((df['food_preparation_time'].max() - df['food_preparation_time'].min())/2)
y_coord2 = df['delivery_time'].min() + ((df['delivery_time'].max() - df['delivery_time'].min())/2)
plt.text(0.32, y_coord1, f'{line_length_var1} minutes', color='red', fontsize=10)
plt.text(1.32, y_coord2, f'{line_length_var2} minutes', color='red', fontsize=10)


plt.show()

plt.figure(figsize=(6, 6))

category_counts = df['day_of_the_week'].value_counts()
sns.barplot(x=category_counts.index, y=category_counts, color='#F07C02', saturation=1)

plt.title('Weekend Versus Weekday Ordering')
plt.ylabel('Number of Orders')
plt.ylim(0, 1500)
plt.xticks()

# remove the top and right spines (borders)
ax = plt.gca() # for making customizations to our axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.set_xticks([]) # remove x-axis ticks
# add text annotations for the labels under each box
label_positions = [0, 1]  # positioning: 0 is the left box, and 1 is the right box, since these are categorical
label_texts = ['Weekends', 'Weekdays']  # set the labels for the left and right boxes
for i in range(len(label_positions)):
    plt.text(label_positions[i], -50, label_texts[i], ha='center', va='center', fontsize=10)

# add total number of orders as text annotations at the top of each bar
for i, count in enumerate(category_counts):
    plt.text(i, count + 25, str(count), ha='center', va='center', fontsize=10)

# a horizontal line at the average number of orders at any given day
mean_value = df['day_of_the_week'].value_counts().mean()
plt.axhline(mean_value, color='black', linestyle='--', label=f'Mean ({mean_value:.2f})')
plt.text(1, mean_value + 25, "average number of orders over the week", ha='center', va='center', fontsize=9, color='black') # label the line

plt.show()

# for presentation purposes, I want to highlight the most popular kinds of cuisine
plt.figure(figsize=(8, 6))

category_counts = df['cuisine_type'].value_counts()
custom_palette = {category: "#F07C02" if count > 100 else "#ADADAD" for category, count in category_counts.items()} # for highlighting cuisine that gets the most orders - specifically, if more than 100 orders are placed, then orange else grey
sns.barplot(x=category_counts.index, y=category_counts, palette=custom_palette, saturation=1 ); # seaborn changes the saturation by default, which will change the color away from our palette

plt.title('Orders Across Cuisine Types');
plt.ylabel('Number of Orders');
plt.ylim(0, 650);
plt.xticks(rotation=90);

# remove the top and right spines (borders)
ax = plt.gca() # for making customizations to our axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# add total number of orders as text annotations at the top of each bar
for i, count in enumerate(category_counts):
    plt.text(i, count + 10, str(count), ha='center', va='center', fontsize=10)

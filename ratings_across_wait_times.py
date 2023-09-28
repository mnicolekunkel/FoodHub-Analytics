# we need to ensure rating is read as a quantitative variable
df['rating'] = df['rating'].replace(['Not given'],np.nan) # turn not given to sometime quantitativedly compatible
df['rating'] = df['rating'].astype(float) # make rating read as a numeric value

df['total_time'] = df['delivery_time']+df['food_preparation_time'] # get the total amt of time it takes waiting from ordering until delivery

# set the figure size
plt.figure(figsize=(7, 6))  # longer and not too tall

sns.lineplot(data=df, x='total_time', y='rating', color='#F07C02');

plt.title('Ratings Across Customer Wait Times');
plt.xlabel('Wait Time (minutes)')
plt.ylabel('Rating')

# remove the top and right spines (borders)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# a horizontal line at the average number of orders at any given day
mean_value = df['rating'].mean()
plt.axhline(mean_value, color='black', linestyle='--', label=f'Mean ({mean_value:.2f})')
plt.text(73, mean_value, "average rating", ha='center', va='center', fontsize=9, color='black') # label the line

plt.show()

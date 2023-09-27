# define colors for our top performing companies
color_mapping = {
    "Shake Shack": '#F07C02', # foodhub orange
    "The Meatball Shop": '#F07C02',
    "Blue Ribbon Sushi": '#F07C02',
    "Blue Ribbon Fried Chicken": '#F07C02',
    "Parm":'#F07C02'
}

# define the percentage of orders that come from these restaurants:
percent_annot = round(sum(df['restaurant_name'].value_counts()[:5])/len(df)*100,2)
# each row represents an order and contained the name of the restaurant from which it came in the restaurant_name column

# initialize a variable to keep track of the bottom position
left = 0

# set the figure size
plt.figure(figsize=(10, 3))  # longer and not too tall

# create a stacked bar chart by interatively aggregating % ratings in a  single bar
for i, row in data.iterrows():
    category = row['restaurant_name'] # what we are aggregating
    count = row['order_count'] # for adding text a little further below below
    color = color_mapping.get(category, '#ADADAD')  # default to gray if color not defined
    plt.barh(0, count, left=left, color=color); # horizontal bar of percentage with predefined parameters
    
    left += count

# annotation: the portion of orders that come from the top 5 performing restaurants
x_value = sum(df['restaurant_name'].value_counts()[:5])/2 # middle of the counts, where our label should be placed along the x axis
plt.text(x_value, 0, f'{percent_annot}% of orders', 
         ha='center', va='center', color='black', fontsize=10)

# annotation: the total number of orders placed
x_value2 = df.shape[0] # edge of the bar chart
plt.text(x_value2 + 25, 0, f'{x_value2} orders placed', 
         ha='center', va='center', color='black', fontsize=10, rotation=270)

plt.title('Performance of Most Popular Restaurants') # give title
plt.xlabel('Number of Orders')
plt.yticks([])# remove y-axis ticks and labels, since we have a legend

# remove the top and right spines (borders)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()

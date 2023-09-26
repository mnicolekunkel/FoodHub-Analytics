data = {
    'rating': ["Not given", "5 stars", "4 stars", "3 stars"],
    'percentage': [38.78, 30.98, 20.34, 9.91]
}

# define colors for each rating category
color_mapping = {
    "Not given": '#545470',
    "5 stars": '#F07C02',
    "4 stars": '#ffba08',
    "3 stars": '#ADADAD'
}

df = pd.DataFrame(data)

# initialize a variable to keep track of the left position (this figure will be flipped, so it will be stacked left to right)
left = 0

# set the figure size
plt.figure(figsize=(10, 3))  # longer along the x axis for readability and not too tall in this case

# create a stacked bar chart by interatively aggregating % ratings in a  single bar and plotting as we go
for i, row in df.iterrows(): # allows us to iterate over the rows we need:
    category = row['rating'] # 1. what we are aggregating
    percentage = row['percentage'] # and 2. for labeling and defining values
    
    color = color_mapping.get(category, 'gray')  # default to gray if color not defined
    plt.barh(0, percentage, left=left, color=color) # horizontal bar of percentage with predefined parameters

   # add text labels for rating and percentage on our plot
    plt.text(left + percentage / 2, 0, f'{category}\n{percentage:.2f}%', 
             ha='center', va='center', color='white', fontsize=10)
    
    left += percentage # interatively stacking our bars

plt.title('Ratings from Customers') # give title
plt.yticks([])# remove y-axis ticks and labels
# remove the top and right spines (borders):
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()

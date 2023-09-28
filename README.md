## FoodHub-Analytics
After conducting freelance exploratory data analysis using Python, I share some insights and templates for presenting insights to your stakeholders.

I'm not at liberty to share the dataset I worked with, but I presented a snapshot of 5 rows of data and information about thhe data to understand its structure in order to help follow along the code.
I recommend looking through the pdf file containing a presentation of results and then going to the figure template you desire in this repository.

# Info about the dataset:
- order_id: Unique ID of the order
- customer_id: ID of the customer who ordered the food
- restaurant_name: Name of the restaurant
- cuisine_type: Cuisine ordered by the customer
- cost: Cost of the order
- day_of_the_week: Indicates whether the order is placed on a weekday or weekend (The weekday is from Monday to Friday and the weekend is Saturday and Sunday)
- rating: Rating given by the customer out of 5
- food_preparation_time: Time (in minutes) taken by the restaurant to prepare the food. This is calculated by taking the difference between the timestamps of the restaurant's order confirmation and the delivery person's pick-up confirmation.
- delivery_time: Time (in minutes) taken by the delivery person to deliver the food package. This is calculated by taking the difference between the timestamps of the delivery person's pick-up confirmation and drop-off information

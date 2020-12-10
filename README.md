# pizza-chat-bot
Creating a chat bot to order pizzas.


Placing an order:

User interacts with bot.
After user provides contact number a post request is sent to server with all details.
Server returns orderID.
Dialogflow responds this orderId to user.


Checking Status:

User sends orderID.
Post request is sent to server with orderID.
Status of order is decided based on the timestamp stored in database.
Status is sent as response.
Dialogflow responds the status to user.

Api used

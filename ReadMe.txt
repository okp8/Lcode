Discord Leetcode Bot
Introduction
This Discord bot provides a convenient way to access LeetCode problems based on different categories such as algorithms, databases, JavaScript, shell scripting, and concurrency. The bot also features a timer to track your coding sessions.

Authors
Tanav Bollam
Jesse Singh
Ohm Patel
Shiv Shekhar
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/leetcode-discord-bot.git
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up a Discord bot and obtain the token. Replace the placeholder BOT_TOKEN in the code with your actual bot token.

Set the CHANNEL_ID to the appropriate Discord channel ID where you want the bot to send messages.

Usage
Start the bot:

bash
Copy code
python bot.py
The bot will now be ready to respond to commands in your Discord server.

Bot Commands
!hello: Bot says hello.
!bye: Bot says goodbye.
LeetCode Problem Commands:
!easy_database
!medium_database
!hard_database
!easy_algorithms
!medium_algorithms
!hard_algorithms
!easy_concurrency
!medium_concurrency
!hard_concurrency
!easy_javascript
!medium_javascript
!hard_javascript
!easy_shell
!medium_shell
!hard_shell
Timer Commands:
!start: Starts a coding session timer.
!end: Ends the current coding session and displays the duration.
Contributing
If you have suggestions, improvements, or new features you'd like to add, feel free to fork the repository and submit a pull request.


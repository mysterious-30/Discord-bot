# Discord Bot with Keep-Alive

This project is a Discord bot built using **Python** and the **discord.py** library. The bot provides various functionalities such as:

- **Message Purge**: Allows users to delete a specified number of messages.
- **Avatar**: Displays the avatar of a specific user.
- **Scheduled Cleanup**: Automatically purges messages in a specified channel at scheduled times.
- **Welcome and Farewell Messages**: Sends welcome and farewell messages when a member joins or leaves the server.
- **Keep-Alive Server**: A Flask-based web server is used to keep the bot alive on hosting platforms like Heroku or Replit.

## Features

- **Message Purging**: Allows administrators to purge a set number of messages from a channel.
- **Avatar Command**: Retrieves the avatar of any user.
- **Scheduled Message Cleanup**: Automates message cleanup in channels at specific times.
- **Welcome/Farewell Messages**: Sends custom messages when a user joins or leaves the server.
- **Keep-Alive Server**: A simple Flask server that prevents the bot from going idle by responding to periodic pings.

## Setup

### 1. Install Dependencies

Make sure you have **Python 3.8+** installed. Then, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

Here is the list of dependencies in `requirements.txt`:

```
discord.py
flask
pytz
```

### 2. Create a Discord Bot

If you haven't created a Discord bot yet, follow these steps:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application and add a bot to it.
3. Copy the bot token and replace the placeholder `YOUR_BOT_TOKEN` in the code with it.

### 3. Configure the Bot

In the bot code, there are a few placeholders you need to replace with your actual values:

- Replace `YOUR_BOT_TOKEN` with your Discord bot token.
- Replace `YOUR_DISCORD_ID` with your Discord user ID (this is required for the shutdown command).
- Replace `WELCOME_CHANNEL_ID` and `FAREWELL_CHANNEL_ID` with the channel IDs where you want the bot to send welcome and farewell messages.

### 4. Hosting the Bot

If you're hosting the bot on a platform like **Heroku** or **Replit**, you need to keep the bot alive using a **keep-alive** mechanism. This bot uses a **Flask** server that will respond to HTTP requests and prevent the platform from shutting it down due to inactivity.

1. **Flask Server**:
   The bot includes a simple Flask server that runs in a separate thread. This server listens for HTTP requests to the root URL (`/`) and returns a response to confirm that the bot is running.

2. **Keep-Alive with External Services**:
   Use services like **UptimeRobot** to periodically ping your bot’s server to ensure it stays alive. Set up the service to ping the URL of your Flask server at regular intervals (e.g., every 5 minutes).

### 5. Run the Bot

Run the bot by executing the following command:

```bash
python bot.py
```

This will start both the Flask server (to keep the bot alive) and the bot itself.

### 6. Stop the Bot

To shut down the bot, use the `~shutdown` command. Only the bot owner (defined by their Discord ID) can use this command.

## Commands

### 1. `~purge <amount>`
Purges a specified number of messages in the current channel.

Example:
```
~purge 10
```

### 2. `~avatar <user>`
Displays the avatar of a specified user. If no user is mentioned, it will show the avatar of the command author.

Example:
```
~avatar @username
```

### 3. `~autoclean <channel> <time>`
Schedules a message cleanup at a specified time for a given channel. Time must be in **HH:MM** format.

Example:
```
~autoclean #general 14:30
```

### 4. `~shutdown`
Shuts down the bot. This command can only be used by the bot owner.

Example:
```
~shutdown
```

## Contributing

Feel free to fork this project, open issues, and submit pull requests. Make sure to test your changes and ensure everything works correctly before submitting.

---

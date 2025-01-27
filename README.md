Here's a detailed README description for your project:

---

# Discord Multi-Utility Bot  

This project is a versatile **Discord Bot** built using Python and the `discord.py` library. It is designed to provide several utilities for managing Discord servers, automating tasks, and enhancing the user experience. Whether you're looking for advanced logging, message purging, or automated channel cleanup, this bot offers all these features and more in a clean, intuitive implementation.  

---

## Key Features  

### **1. Server and Channel Logging**  
- The bot monitors messages sent in any server it is a part of.  
- Automatically creates a dedicated text channel in a personal server to log messages from other servers.  
- Message logs include the author's username, user ID, message content, and the server name.  
- If a corresponding logging channel doesn’t exist, it creates one dynamically.  

### **2. Auto Channel Cleanup**  
- Provides a feature for users to schedule automatic cleanup of messages in a channel.  
- Users can specify the time in **HH:MM** format and the bot will automatically purge messages in the selected channel at the scheduled time.  
- Supports Indian Standard Time (IST) for scheduling.  
- Deleted messages are logged and saved in a text file for review.  

### **3. Welcome and Farewell Messages**  
- Sends a custom welcome message when a user joins a server.  
- Includes a warm greeting and the user’s mention for visibility.  
- Sends a farewell message when a user leaves the server, mentioning their username and user ID.  

### **4. Message Purging**  
- Provides an easy-to-use command to purge messages from a channel.  
- Users with proper permissions can delete a specified number of messages.  
- Logs details of all purged messages into a text file.  
- Automatically shares the log file in the channel for reference.  

### **5. Avatar Display**  
- Displays the avatar of any server member with a simple command.  
- Users can view their own avatar or mention another member to view theirs.  

### **6. Bot Management**  
- Includes an owner-only `shutdown` command to safely terminate the bot.  
- Graceful handling of errors with descriptive messages, such as invalid commands or permissions issues.  

### **7. Logging**  
- Comprehensive logging using Python’s `logging` module.  
- Maintains two separate log files:  
  - **`discord.log`**: Tracks bot activities, such as events and errors.  
  - **`message_purge.log`**: Tracks purged messages with timestamps and content.  

---

## Technical Details  

### **1. Programming Language**  
- Python 3.10  

### **2. Libraries and Dependencies**  
- **`discord.py`**: Core library for interacting with the Discord API.  
- **`asyncio`**: For asynchronous programming and task scheduling.  
- **`pytz`**: Handles time zone conversions, allowing scheduling in Indian Standard Time (IST).  
- **`logging`**: Provides robust logging for events, errors, and activities.  
- **`datetime`**: For handling and formatting dates and times.  
- **`re`**: Used for validating user inputs, such as time formats.  

### **3. Hosting and Deployment**  
- Includes a `keep_alive` function, suggesting it can be hosted on platforms like **Replit**, **Heroku**, or **Vercel**.  
- Secure environment variable management ensures that sensitive information like the bot token remains private.  

---

## Commands  

| Command                 | Description                                                                                   | Permissions Required        |
|-------------------------|-----------------------------------------------------------------------------------------------|-----------------------------|
| `~purge <amount>`       | Deletes the specified number of messages from the current channel.                            | Manage Messages             |
| `~avatar [@member]`     | Displays the avatar of the mentioned member or the command user if no mention is provided.    | None                        |
| `~autoclean`            | Initiates the auto-clean setup to schedule message purging in a specific channel.             | None                        |
| `~schedule`             | Reschedules a previously set auto-clean task based on saved preferences.                      | None                        |
| `~shutdown`             | Safely shuts down the bot (owner-only).                                                      | Owner Only                  |

---

## How It Works  

1. **Message Logging:**  
   When a message is sent in any server where the bot is active, it checks the bot owner's personal server for a dedicated logging channel for that server. If no such channel exists, it creates one and forwards all relevant message details.  

2. **Auto Cleanup:**  
   Users can schedule a cleanup task by specifying the target channel and a time. The bot will wait asynchronously until the target time and then purge messages from the specified channel. Deleted messages are logged for review.  

3. **Welcome and Farewell:**  
   Upon a member joining or leaving the server, the bot sends a personalized message in the welcome channel (predefined by its ID).  

4. **Error Handling:**  
   Invalid commands, missing permissions, or improperly formatted inputs are gracefully handled, with meaningful error messages provided to the user.  

---

## Installation  

### Prerequisites  
1. Python 3.10 or above installed.  
2. A Discord bot token.  
3. The following Python libraries installed:  
   ```bash
   pip install discord.py pytz
   ```  

### Setup  
1. Clone this repository to your local machine:  
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```  

2. Set up the required environment variables:  
   - **`token`**: Your Discord bot token.  

3. Run the bot:  
   ```bash
   python bot.py
   ```  

---

## Contributing  

Contributions are welcome! If you encounter any bugs or have ideas for new features, feel free to open an issue or create a pull request.  

---

## License  

This project is licensed under the MIT License. See the LICENSE file for details.  

---

Feel free to replace placeholders like `<repository-url>` or `<repository-folder>` with your actual repository details.

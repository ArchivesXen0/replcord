import requests
import random

# Example codes for redemption
example_codes = ['AIFI218484', 'LKG43MF2K1', 'LM22KE1O92', 'LOYU24IR42']

# Webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1258282659809988709/cvHr3p1NfybMDLOpvC5TARu2QVsSKUC7VJyqOwx3OZeM0W45yoFi70-msafO4WAuzABh'

# Avatar URL
AVATAR_URL = 'https://i.imgur.com/7bM6vSk.png'  # Replace with the URL of your uploaded image

# Function to send webhook message
def send_webhook(message, username="Giveaway Bot", avatar_url=AVATAR_URL):
    data = {
        'content': message,
        'username': username,
        'avatar_url': avatar_url
    }
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        response.raise_for_status()
        print(f"Webhook message sent: {message}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending webhook message: {e}")

# Function to handle balance command
def handle_balance(username):
    # Placeholder logic to check balance (replace with actual implementation)
    balance = random.randint(0, 100)  # Example: random balance generation
    message = f"Balance for {username}: ${balance}"
    send_webhook(message)

# Function to handle leaderboard command
def handle_leaderboard():
    # Placeholder logic to generate leaderboard (replace with actual implementation)
    leaderboard = [
        {"username": "User1", "score": 10},
        {"username": "User2", "score": 8},
        {"username": "User3", "score": 6},
    ]
    leaderboard_message = "Leaderboard:\n"
    for idx, entry in enumerate(leaderboard, start=1):
        leaderboard_message += f"{idx}. {entry['username']} - {entry['score']} points\n"
    send_webhook(leaderboard_message)

# Function to handle claim command
def handle_claim(username):
    # Placeholder logic to handle claiming rewards (replace with actual implementation)
    message = f"{username} claimed a special reward! Congratulations!"
    send_webhook(message)

# Function to handle invite command
def handle_invite(username):
    # Placeholder logic to simulate inviting friends (replace with actual implementation)
    message = f"{username} invited friends and earned rewards!"
    send_webhook(message)

# Function to handle status command
def handle_status():
    # Placeholder logic to get current status (replace with actual implementation)
    status_message = "Current status: Giveaways are active! Claim your rewards now!"
    send_webhook(status_message)

# Function to handle send command
def handle_send(command):
    # Placeholder logic to handle sending messages (replace with actual implementation)
    parts = command.split(maxsplit=1)
    if len(parts) == 2:
        _, message = parts
        send_webhook(message)
    else:
        send_webhook("Invalid command format. Usage: >send [Message]")

# Function to handle redeem command
def handle_redeem(command):
    # Placeholder logic to handle redeeming gift cards (replace with actual implementation)
    parts = command.split(maxsplit=3)
    if len(parts) == 4:
        _, platform, amount, username = parts
        code = random.choice(example_codes)
        message = f"{username} just redeemed {amount} giftcard for {platform}! LET'S GOOO"
        send_webhook(message)
    else:
        send_webhook("Invalid command format. Usage: >redeem [Platform] [Amount] [Username]")

# Function to handle invitechecker command
def handle_invitechecker():
    # Placeholder logic to display invite counts (replace with actual implementation)
    invite_data = {
        "randyhandybbg": 122,
        "expiris.gs": 32,
        "its.wraps": 22,
        "aqualza.gs": 12
    }
    invite_message = "Invite Checker:\n"
    for username, invites in invite_data.items():
        invite_message += f"{username} has {invites} invites\n"
    send_webhook(invite_message)

# Function to display help command
def display_help():
    # This function won't send the message to Discord webhook
    help_message = (
        "Available Commands:\n"
        ">balance [Username] - Check the balance of a user\n"
        ">leaderboard - Show the top users by points\n"
        ">claim [Username] - Claim a reward or special prize\n"
        ">invite [Username] - Simulate inviting friends and earn rewards\n"
        ">status - Show the current status of giveaways\n"
        ">send [Message] - Send a custom message to the server\n"
        ">redeem [Platform] [Amount] [Username] - Redeem a gift card\n"
        ">invitechecker - Display invite counts\n"
        ">help - Display this help message"
    )
    print(help_message)

# Main function to handle commands
def main():
    print(">Welcome to replcord! Try these cmds, >balance >leaderboard >claim >invite >status >send >redeem >invitechecker")
    while True:
        command = input("> ")
        if command.startswith(">balance"):
            _, username = command.split(maxsplit=1)
            handle_balance(username)
        elif command.startswith(">leaderboard"):
            handle_leaderboard()
        elif command.startswith(">claim"):
            _, username = command.split(maxsplit=1)
            handle_claim(username)
        elif command.startswith(">invite"):
            _, username = command.split(maxsplit=1)
            handle_invite(username)
        elif command.startswith(">status"):
            handle_status()
        elif command.startswith(">send"):
            _, message = command.split(maxsplit=1)
            handle_send(message)
        elif command.startswith(">redeem"):
            handle_redeem(command)
        elif command.startswith(">invitechecker"):
            handle_invitechecker()
        elif command.startswith(">help"):
            display_help()
        else:
            print("Invalid command. Use '>balance [Username]', '>leaderboard', '>claim [Username]', '>invite [Username]', '>status', '>send [Message]', '>redeem [Platform] [Amount] [Username]', '>invitechecker', or '>help'.")

if __name__ == "__main__":
    main()

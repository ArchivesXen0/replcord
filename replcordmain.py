import requests
import random

# Example codes for redemption
example_codes = ['AIFI218484', 'LKG43MF2K1', 'LM22KE1O92', 'LOYU24IR42']

# Function to send webhook message
def send_webhook(username, platform, amount, code):
    webhook_url = 'https://discord.com/api/webhooks/1258282659809988709/cvHr3p1NfybMDLOpvC5TARu2QVsSKUC7VJyqOwx3OZeM0W45yoFi70-msafO4WAuzABh'  # Replace with your webhook URL

    message = f"{username} just redeemed {amount}$ ({platform}) giftcard! LET'S GOOO\nSend 1$ to this CashApp for a 10$ giftcard! https://cash.app/$Justhim732713"
    data = {
        'content': message,
        'username': "GIFTCARD REDEEMER",  # Set the webhook username to GIFTCARD REDEEMER
        'avatar_url': 'https://i.imgur.com/7bM6vSk.png'  # Example avatar URL
    }

    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        print(f"Webhook message sent: {message}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending webhook message: {e}")

# Function to handle redeem command
def handle_redeem(command):
    parts = command.split(maxsplit=4)
    if len(parts) == 4:
        _, platform, amount, username = parts
        code = random.choice(example_codes)
        send_webhook(username, platform.upper(), amount.upper(), code)
    else:
        print("Invalid command format. Usage: >redeem [Platform] [Amount] [Username]")

# Main function to handle commands
def main():
    print(">Welcome to replcord! Try these cmds, >send >redeem")
    while True:
        command = input("> ")
        if command.startswith(">redeem"):
            handle_redeem(command)
        elif command.startswith(">send"):
            print("Placeholder for send command handling.")
            # Implement handling for send command if needed
        else:
            print("Invalid command. Use '>redeem [Platform] [Amount] [Username]' or '>send [Username] [Message]'.")

if __name__ == "__main__":
    main()

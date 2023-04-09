import functools
import discord

def chat_helper(client, sender):
    def helper(func):
        @functools.wraps(func)
        async def wrapper(interaction: discord.Interaction, *, message: str):
            if interaction.user == client.user:
                return
            await interaction.response.defer()
            try:
                receive = await func(interaction=interaction, message=message)
            except Exception as e:
                receive = str(e)
            await sender.send_message(interaction, message, receive)

        return wrapper
    return helper

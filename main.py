
import os

from dotenv import load_dotenv
import discord

from src.discordBot import DiscordClient, Sender
from src.logger import logger
from src.chatgpt import ChatGPT, DALLE
from src.models import OpenAIModel
from src.memory import Memory
from src.server import keep_alive
from src.utils import chat_helper

load_dotenv()

models = OpenAIModel(api_key=os.getenv('OPENAI_API'), model_engine=os.getenv('OPENAI_MODEL_ENGINE'))

memory = Memory(system_message=os.getenv('SYSTEM_MESSAGE'))
chatgpt = ChatGPT(models, memory)
dalle = DALLE(models)


def run():
    client = DiscordClient()
    sender = Sender()

    @client.tree.command(name="chat", description="Have a chat with ChatGPT")
    @chat_helper(client=client, sender=sender)
    async def chat(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id
        return chatgpt.get_response(user_id, message)

    @client.tree.command(name="new_chat", description="Start a new chat with ChatGPT")
    @chat_helper(client=client, sender=sender)
    async def new_chat(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id
        chatgpt.reset_history(user_id)
        return chatgpt.get_response(user_id, message)

    @client.tree.command(name="summarize", description="Text summarization with ChatGPT")
    @chat_helper(client=client, sender=sender)
    async def summarize(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id
        chatgpt.reset_history(user_id)
        return chatgpt.get_response(user_id, f"幫我摘要以下內容並以中文回傳: {message}")

    @client.tree.command(name="translate", description="Text translation with ChatGPT")
    @chat_helper(client=client, sender=sender)
    async def translate(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id
        chatgpt.reset_history(user_id)
        return chatgpt.get_response(user_id, f"幫我翻譯以下內容並以中文回傳: {message}")

    @client.tree.command(name="imagine", description="Generate image from text")
    async def imagine(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        image_url = dalle.generate(prompt)
        await sender.send_image(interaction, prompt, image_url)

    @client.tree.command(name="reset", description="Reset ChatGPT conversation history")
    async def reset(interaction: discord.Interaction):
        user_id = interaction.user.id
        logger.info(f"resetting memory from {user_id}")
        try:
            chatgpt.reset_history(user_id)
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send(f'> Reset ChatGPT conversation history < - <@{user_id}>')
        except Exception as e:
            logger.error(f"Error resetting memory: {e}")
            await interaction.followup.send('> Oops! Something went wrong. <')

    client.run(os.getenv('DISCORD_TOKEN'))


if __name__ == '__main__':
    keep_alive()
    run()

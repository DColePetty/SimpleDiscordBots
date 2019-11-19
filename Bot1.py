import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        if message.content.startswith('!help'):
            await message.channel.send('try !help, !hello, woot!'.format(message))
        if message.content.startswith('I'):
            await message.channel.send('-f'.format(message))
        if message.content.startswith('woot'):
            await message.channel.send('woot woot to you, human'.format(message))

client = MyClient()
client.run('NjE5MzQzNTE2Nzc4MjMzODY4.XXG3JQ.9Z9LvR-kgmXHo4edY1g77kxRCHk')
print("it should have worked")

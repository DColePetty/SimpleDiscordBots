#MinigameMonsters Bot
import discord
import MinigameMonsters
import time

global PlayerNameList
PlayerNameList = []
global PlayerMonsterKillsList
PlayerMonsterKillsList = []

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
        if message.content.startswith('-b'):
            await message.channel.send('Hello {0.author.mention}, Welcome to a new Adventure!\n-s: your stats\n-f fight monsters'.format(message))

        if message.content.startswith('-roll'):
            rolled = True

        if message.content.startswith('-f'):
            await message.channel.send('Hello {0.author.mention}, have fun on your adventure!'.format(message))
            if str(message.author) not in PlayerNameList:
                PlayerNameList.append(str(message.author))
                PlayerMonsterKillsList.append(0)
            else:
                print(str(message.author) + " is in the list already :)")
            a = MinigameMonsters.Hero()
            b = MinigameMonsters.MonsterGoblin()
            await message.channel.send('Goblins have been running amuck lately... \n I am sure there is some nearby though...'.format(message))
            time.sleep(3)
            await message.channel.send('You hear footsteps approaching... '.format(message))
            time.sleep(4)

            #await message.channel.send('Ah! A GOBLIN RACES TOWARDS YOU\ntype -roll to roll and see how well you defend yourself and attack the monster!'.format(message))

            while(a.currHP > 0 and b.currHP > 0):
                playerRoll = a.roll()
                await message.channel.send(('You rolled a: ' + str(playerRoll) + ' \n').format(message))
                goblinRoll = b.roll()
                #print("Hero Roll: " + str(playerRoll) + "\tGoblin Roll: " + str(goblinRoll))
                if(playerRoll > goblinRoll):
                    b.currHP -= a.attackDamage
                if(playerRoll == goblinRoll):
                    print('PARRY!')
                if(playerRoll < goblinRoll):
                    a.currHP -= b.attackDamage
                if(playerRoll == 0):
                    a.currHP -= 1
                if(playerRoll == 10):
                    b.currHP -= a.attackDamage
                await message.channel.send(("\tHero HP: " + str(a.currHP) + "\tGoblin HP: " + str(b.currHP) + " ").format(message))

                time.sleep(2)
                #print("\tHero HP: " + str(a.currHP) + "\tGoblin HP: " + str(b.currHP))
            if(a.currHP > b.currHP):
                await message.channel.send(("I never doubted you for a second, adventurer. \nYour valor will not be forgotten! \n\t{0.author.mention} ").format(message))
                loc = PlayerNameList.index(str(message.author))
                PlayerMonsterKillsList[loc] = PlayerMonsterKillsList[loc]+1
            else:
                await message.channel.send(("It seems you have passed out. That is ok. There is always tomorrow- If the goblins kill you, you will stop bringing them new swords and clothes! \n\t{0.author.mention} ").format(message))
            i = 0
            for entry in PlayerNameList:
                print(str(PlayerNameList[i]) + ':' + str(PlayerMonsterKillsList[i]))
                i= i+1
        if message.content.startswith('-s'):
            await message.channel.send('woot woot to you, human'.format(message))

client = MyClient()
client.run('NjE5Mzk3ODQyNjUzNTQ0NDQ4.XXHpgg.5GOiN4g5SPtOZzOQbEWjnL3c6JA')
print("it should have worked")

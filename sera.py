# This example requires the 'members' privileged intents
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random



description = '''Hi I'm Sera <3'''
load_dotenv()
TOKEN: str = os.getenv('SERA_BOT_TOKEN')
print(TOKEN)
bot = commands.Bot(command_prefix='sera', description=description, case_insensitive=True)



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="MORE"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(name='seraphine', aliases=["sera", 'seraboo'])
@commands.cooldown(100, 120, commands.BucketType.user)
async def seraphine(ctx):
    await ctx.send("Seraphine in your Area!")


@bot.command(aliases=["awi"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def ahri(ctx):
    ahrilines = ['Ahri is my leader.', 'Ahri can sing sooo good', "She's so kind to me", "Remember Ahri's advice. Stars shine with their own light. I've got this!",
                 "Hey, Ahri! Take a look and recognize a queen.", "Miss Ahri, did I sing too loud? I wasn't trying to!"]
    await ctx.send("Where is Æhri? #Kahri <:ahripupdiscordemote:820152343613669413>")


@bot.command(aliases=["agawi", "kali"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def akali(ctx):
    akalilines = ["Gonna earn my custom mic just like Akali.", "Akali, I'm always on fire... so don't get burned!",
                  "Akali! Oh no! Did I... 'go to work' too hard?"]
    await ctx.send(random.choice(akalilines))


@bot.command(aliases=["Evie", "Eve"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def evelynn(ctx):
    evelines = ["EVIEEE", "Evelynn will kill me if I screw this up. So let's sparkle and win!", "Evelynn, what's higher than the top? That's me.",
                "I didn't mean to hurt your feelings, Eve. Wait... you have feelings?"]
    await ctx.send(random.choice(evelines))

@bot.command(aliases=["kai'sa", 'kaikai', "kai"])
@commands.cooldown(2, 120, commands.BucketType.user)
async def kaisa(ctx):
    kaisalines = ["I've practiced this choreography a million times. I can't disappoint Kai'Sa. I won't!", "Kai'Sa, you're cool, but I'm cold.",
                  "Her food is so delicious", "Oops. I rushed that choreo didn't I, Kai'Sa?"]
    await ctx.send(random.choice(kaisalines))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):
        await ctx.author.send(error.args[0])



bot.run(TOKEN)
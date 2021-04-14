# This example requires the 'members' privileged intents
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random



description = '''Hi I'm Kai'sa and I can summon Noly'''
load_dotenv()
TOKEN: str = os.getenv('KAISA_BOT_TOKEN')
print(TOKEN)
bot = commands.Bot(command_prefix='!', description=description, case_insensitive=True)




@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Drum Go Drum"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(name='kaisa', aliases=["kai'sa", 'kaikai', "kai"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def kaisa(ctx):
    embed_title = "WE SUMMON THEE NOLY, SIMPER OF KAI'SA, DAUGHTER OF THE VOID"
    i = random.randint(1, 22)
    embed = discord.Embed(title=embed_title)
    embed.set_image(url=f"https://share.geozukunft.at/kaisa/{i}.jpg")
    await ctx.send(embed=embed)


@bot.command(aliases=['nyoly', 'dj'])
@commands.cooldown(1, 120, commands.BucketType.user)
async def noly(ctx, *args):
    embed_title = "OMG I love Noly her drÆwings from me are sooo cool I love her."
    embed = discord.Embed(title=embed_title)
    embed.set_image(url=f"https://share.geozukunft.at/kaisa/21.jpg")
    await ctx.send(embed=embed)


@bot.command(aliases=['pspspsps', 'psps', 'pspsps'])
@commands.cooldown(1, 120, commands.BucketType.user)
async def summon(ctx):
    embed_title = "NOLY PSSPSPSPS"
    embed = discord.Embed(title=embed_title)
    embed.set_image(url=f"https://share.geozukunft.at/kaisa/pspsps.jpg")
    await ctx.send(embed=embed)


@bot.command(aliases=["awi", "gf", "wife"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def ahri(ctx):
    ahrilines = ['Where is my Æhri? #Kahri <:ahripupdiscordemote:820152343613669413>', 'I love her so much', "I haven't seen her all day I hope she's not overworking herself"]
    await ctx.send("Where is Æhri? #Kahri <:ahripupdiscordemote:820152343613669413>")


@bot.command(aliases=["agawi", "rogue", "childhead"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def akali(ctx):
    akalilines = ["No Ramen now you had some yesterday!", "I love that cutie so much", "Yes you'll get Ramen today. <:AhriCharm:802053233623302174>"]
    await ctx.send(random.choice(akalilines))


@bot.command(aliases=["Evie", "Eve"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def evelynn(ctx):
    evelines = ["EVIEEE", "What has she done again?", "She's probably in the garage"]
    await ctx.send(random.choice(evelines))

@bot.command(aliases=["Sera"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def seraphine(ctx):
    seralines = ["Protect her at all costs", "She's so sweet", "Her voice is soo beautiful", "I hope she's not doing dumb stuff with Akali again"]
    await ctx.send(random.choice(seralines))


@bot.command(aliases=["nyaqling"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def suqling(ctx):
    embed_title = "WE ALL HERE HAVE GATHERED TODAY TO PRAY TO OUR ONE AND ONLY NYAQLING"
    images = ['prayer1', 'prayer2']
    embed = discord.Embed(title=embed_title)
    selected = random.choice(images)
    embed.set_image(url=f"https://share.geozukunft.at/kaisa/{selected}.jpg")
    await ctx.send(embed=embed)


@bot.command(aliases=["horny", "spin"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def horni(ctx):
    await ctx.send("Got the Boom got the base gonna shake it in your face")
    await ctx.send("https://share.geozukunft.at/kaisa/spin.gif")

@bot.command(aliases=["luv", "kithes", "kiss"])
@commands.cooldown(2, 120, commands.BucketType.user)
async def love(ctx):
    lovefiles = ["love1.jpg"]

    embed = discord.Embed()
    embed.set_image(url=f"https://share.geozukunft.at/kaisa/{random.choice(lovefiles)}")

    await ctx.send(embed=embed)

@bot.command(aliases=['ramen','eat', 'lunch', 'dinner'])
@commands.cooldown(2, 120, commands.BucketType.user)
async def food(ctx):
    foodlines = ["I'm already cooking don't be so impatient", "We already had Ramen yesterday and the last 3 days before....", "Dinner will be ready in 5"]
    await ctx.send(random.choice(foodlines))

@bot.command(aliases=['pissed'])
@commands.cooldown(1, 120, commands.BucketType.channel)
async def mad(ctx):
    madlines = ["Yes I'm mad", "I like the Mad Lions they are a cool team!", "GRRR"]
    await ctx.send(random.choice(madlines))

@bot.command(aliases=["jan"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def angst(ctx):
    await ctx.send("We summon the maker of Angst.")

@bot.command(aliases=["hummm", "hum", "humm"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def microwave(ctx):
    images = ["humm.png", "microwave.png"]
    embed = discord.Embed()
    embed.set_image(url=f"https://share.geozukunft.at/kaisa/{random.choice(images)}")

    await ctx.send(embed=embed)

@bot.command(aliases=["hinge", "huhhh"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def door(ctx):
    images = ["door1.jpg"]
    embed = discord.Embed()
    embed.set_image(url=f"https://share.geozukunft.at/kaisa/{random.choice(images)}")

    await ctx.send(embed=embed)

@bot.command(aliases=["oil", "dry", "WD 40"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def wd40(ctx):
    await ctx.send("Gotta lubricate that hinge")
    await ctx.send("https://share.geozukunft.at/kaisa/wd40.gif")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):
        await ctx.author.send(error.args[0])



bot.run(TOKEN)
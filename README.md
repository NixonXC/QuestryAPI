# QuestryAPI
my first api lol and its really basic

# [Api Url](https://api.pixiej.xyz)

# Imports

```py
import requests
import json
```
# Slash command examples

Questions

```py
@bot.slash_command()
async def question(ctx):
  url = requests.get('http://api.pixiej.xyz/')
  res = url.json()
  em = discord.Embed(title="Question", description=res['question'], color=discord.Color.blurple())
  em.set_footer(text=f"api.pixiej.xyz {res['datetime']}")
  await ctx.respond(embed = em)
```

Jokes

```py
@bot.slash_command()
async def joke(ctx):
  url = requests.get('http://api.pixiej.xyz/')
  res = url.json()
  em = discord.Embed(title="Joke", description=res['joke'], color=discord.Color.blurple())
  em.set_footer(text=f"api.pixiej.xyz {res['datetime']}")
  await ctx.respond(embed = em)
```

# there is a 90% chance I am not gonna update dis repo

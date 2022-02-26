# QuestryAPI
my first api lol and its really basic

[Api Url](https://api.pixiej.xyz)

100 Requests Per Minute

# Imports

```py
import requests
import json
```
# Slash command examples

<h2>Questions</h2>

```py
@bot.slash_command()
async def question(ctx):
  url = requests.get('http://api.pixiej.xyz/')
  res = url.json()
  em = discord.Embed(title="Question", description=res['question'], color=discord.Color.blurple())
  em.set_footer(text=f"api.pixiej.xyz {res['datetime']}")
  await ctx.respond(embed = em)
```

<h2>Jokes</h2>

```py
@bot.slash_command()
async def joke(ctx):
  url = requests.get('http://api.pixiej.xyz/')
  res = url.json()
  em = discord.Embed(title="Joke", description=res['joke'], color=discord.Color.blurple())
  em.set_footer(text=f"api.pixiej.xyz {res['datetime']}")
  await ctx.respond(embed = em)
```

<h2>Facts</h2>

```py
@bot.slash_command()
async def fact(ctx):
  url = requests.get('http://api.pixiej.xyz/')
  res = url.json()
  em = discord.Embed(title="Fact", description=res['fact'], color=discord.Color.blurple())
  em.set_footer(text=f"api.pixiej.xyz {res['datetime']}")
  await ctx.respond(embed = em)
```

# there is 50% chance that I am not going to update this repo

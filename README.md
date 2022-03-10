# QuestryAPI
my first api lol and its really basic

[Api Url](https://api.pixiej.xyz)

<h4>Ratelimit: 100 Requests Per Minute</h4>

# Imports

```py
import aiohttp
import requests
```
# simple example

```py
import requests

url = requests.get("https://api.pixiej.xyz/")
result = url.json()
a = result['question']
b = result['datetime']
c = result['joke']
d = result['fact']
data_set = 'question: ' + a, 'datetime: ' + b, 'joke: '+ c, 'fact: ' + d
print(data_set)
```

# Slash command examples

<h2>Questions</h2>

```py
async def get_question():
  async with aiohttp.ClientSession() as r:
    async with r.get("http://api.pixiej.xyz/") as content:
      req = await content.json(content_type='text/html')
      embed = discord.Embed(title=req["question"], colour = discord.Colour.blue())
      embed.set_footer(text=f"api.pixiej.xyz {req['datetime']}")
      return embed

@bot.slash_command()
async def question(ctx):
  em = await get_question()
  await ctx.respond(embed = em)
```

<h2>Jokes</h2>

```py
async def get_joke():
  async with aiohttp.ClientSession() as r:
    async with r.get("http://api.pixiej.xyz/") as content:
      req = await content.json(content_type='text/html')
      embed = discord.Embed(title=req["joke"], colour = discord.Colour.blue())
      embed.set_footer(text=f"api.pixiej.xyz {req['datetime']}")
      return embed
      
@bot.slash_command()
async def joke(ctx):
  em = await get_joke()
  await ctx.respond(embed = em)
```

<h2>Facts</h2>

```py
async def get_fact():
  async with aiohttp.ClientSession() as r:
    async with r.get("http://api.pixiej.xyz/") as content:
      req = await content.json(content_type='text/html')
      embed = discord.Embed(title=req["fact"], colour = discord.Colour.blue())
      embed.set_footer(text=f"api.pixiej.xyz {req['datetime']}")
      return embed

@bot.slash_command()
async def fact(ctx):
  em = await get_fact()
  await ctx.respond(embed = em)
```

# there is 50% chance that I am not going to update this repo

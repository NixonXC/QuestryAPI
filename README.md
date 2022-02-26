# QuestryAPI
my first api lol and its really basic

# Imports

```py
import requests
import json
```
# Slash command example

```py
@bot.slash_command()
async def question(ctx):
  url = requests.get('http://api.pixiej.xyz/')
  res = url.json()
  em = discord.Embed(title="Question", description=res['question'], color=discord.Color.blurple())
  await ctx.respond(embed = em)
```

# there is a 90% chance I am not gonna update dis repo

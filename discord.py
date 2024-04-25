import discord

client = discord.Client()

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if channel.name == 'waitingroom':  
            await channel.send(f'Καλώς ορίσατε στον server μας, {member.mention}! Παρακαλώ αναμείνατε από τους moderators να σας δώσουν πρόσβαση στο κανάλι iw2024volunteers. Aπολαύστε την τη διαμονή σου σας! Με εκτίμηση, To Helpdesk του Ionian Wikithon')


client.run('YOUR_DISCORD_BOT_TOKEN')
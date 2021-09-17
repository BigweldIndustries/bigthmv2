import discord,asyncio,youtube_dl
from discord.ext import commands
import os



def get_prefix(bot, msg):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['$', 'b!', 'r!'] #Your bot prefix(s)

    return commands.when_mentioned_or(*prefixes)(bot, msg)

bot=commands.Bot(command_prefix=get_prefix,description='bigthm based!', help_command=None)




exts=['music'] #Add your Cog extensions here


@bot.event
async def on_ready():
    song_name='master jonah'  #Status name
    activity_type=discord.ActivityType.listening #Status type
    await bot.change_presence(activity=discord.Activity(type=activity_type,name=song_name))
    print(bot.user.name)

@bot.command()
async def help(ctx, args=None):
    help_embed = discord.Embed(colour=discord.Color.from_rgb(255, 0, 0), title="Bigthm Help")

        help_embed.add_field(
            name="Play",
            value="Plays a song",
            inline=False
        )
        help_embed.add_field(
            name="Skip",
            value="Skips a song",
            inline=False
        )
        help_embed.add_field(
            name="Download",
            value="Downloads a song",
            inline=False
        )
        help_embed.add_field(
            name="Join",
            value="Joins a vc",
            inline=False
        )
        help_embed.add_field(
            name="Leave",
            value="Leaves vc",
            inline=False
        )
        help_embed.add_field(
            name="Pause",
            value="Pauses a song",
            inline=False
        )
        help_embed.add_field(
            name="Queue",
            value="Shows the queue",
            inline=False
        )
        help_embed.add_field(
            name="Repeat",
            value="Repeats a song",
            inline=False
        )
        help_embed.add_field(
            name="Reset",
            value="Resets the current song",
            inline=False
        )
        help_embed.add_field(
            name="Resume",
            value="Resumes a song",
            inline=False
        )
        help_embed.add_field(
            name="Stop",
            value="hops off",
            inline=False
        )
        help_embed.add_field(
            name="Volume",
            value="Changes volume",
            inline=False
        )

    await ctx.send(embed=help_embed)




for i in exts:
    bot.load_extension(i)


bot.run(os.environ['TOKEN'])

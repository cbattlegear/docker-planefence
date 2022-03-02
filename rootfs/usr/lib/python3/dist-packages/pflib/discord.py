import discord_webhook as dw

def build(username, urls, title, description, color=None):
    webhook = dw.DiscordWebhook(url=urls, username=username)

    if color is None:
        color = 0x007bff  # Blue
    embed = dw.DiscordEmbed(title=title, color=color, description=description)
    embed.set_footer(text="Planefence by kx1t - docker:kx1t/planefence")

    webhook.add_embed(embed)

    return webhook, embed

def field(embed, name, value, inline=None):
    if inline is None:
        inline = True
    embed.add_embed_field(name=name, value=value, inline=inline)

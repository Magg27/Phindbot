import subprocess, colorama, re, discord, os
from colorama import Fore
from dotenv import load_dotenv
from discord.ext import commands
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

colorama.init()

load_dotenv()

options = webdriver.ChromeOptions()
options.binary_location = os.getenv('PATH_TO_CHROMIUM')
options.add_argument("--no-sandbox")
options.add_argument("--disable-popup-blocking")
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
options.add_argument('window-size=600,800')
driver = uc.Chrome(service=Service(executable_path='/PATH/TO/CHROMIUM/DRIVER/'), options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get('https://www.phind.com')
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'Basic Search'))).click()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def clear_thread():
    driver.find_element(By.CSS_SELECTOR, '.fw-bold.col-10.fs-5').click()
    return True

def ask_basic(question):
    driver.find_elements(By.NAME, 'q')[-1].send_keys(question + Keys.RETURN)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-light.btn-sm.dropdown.dropdown-toggle.m-1')))
    elements = driver.find_elements(By.CSS_SELECTOR, '.col-lg-8.col-xl-7')[-1].find_elements(By.XPATH, '*')[0].find_elements(By.XPATH, '*')[0].find_elements(By.XPATH, '*')
    response = ""
    for element in elements:
        # Don't include Answer | {model} header in response 
        if element.aria_role == "heading":
            continue
        # Wrap content in md codeblock if in a Phind codeblock
        try: 
            element.find_element(By.CSS_SELECTOR, 'pre')
            response = response + f'```{element.get_attribute("textContent")}```'
            continue
        except:
            pass
        # TODO: Prefix with list number if in a ordered list (below doesn't work properly)
        """
        try:
            ol = element.find_element(By.CSS_SELECTOR, 'ol')
            for li in element.find_elements(By.CSS_SELECTOR, 'li'):
                response + f'{li.find_element(By.CSS_SELECTOR, "::marker")}. {element.get_attribute("textContent")}'.replace("\n", "")
            continue
        except:
            pass
        """
        response = response + '\r' + element.get_attribute('textContent')
    return response

def split_string(message, max_length):
    sentences = re.findall(r'[^.!?]+[.!?]+', message)
    split_strings = []
    current_string = ''

    for sentence in sentences:
        if len(current_string) + len(sentence) <= max_length:
            current_string += sentence + ' '
        else:
            split_strings.append(current_string.strip())
            current_string = sentence + ' '

    if current_string.strip() != '':
        split_strings.append(current_string.strip())

    return split_strings

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='search')
async def search(ctx, *args):
    question = ' '.join(args)
    print(Fore.CYAN + 'Question: ' + Fore.RESET + question)

    try:
        response = ask_basic(question)
        print(Fore.MAGENTA + 'Phind: ' + Fore.RESET + response)

        msgs = split_string(response, 1980)
        for msg in msgs:
            await ctx.reply(msg)

        #await message.reply(f'**Phind:** {response}')
    except subprocess.CalledProcessError as e:
        await ctx.reply(f'**Error:** \n ```{e.output}```')
    except TimeoutException: 
        await ctx.reply(f'Phind timed out, please try again')
@bot.command(name='clear')

async def clear(ctx):
    try:
        clear_thread()
        await ctx.reply('New thread.')
    except subprocess.CalledProcessError as e:
         await ctx.reply(f'**Error:** \n ```{e.output}```')


DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(DISCORD_TOKEN)

### Authors: Tanav Bollam, Jesse Singh, Ohm Patel, Shiv Shekhar
### Discord Leetcode Bot

# Import required files for program
from discord.ext import commands
import discord
import os
import sys
from time import sleep
import leetcode
from dataclasses import dataclass
import datetime
import random

#Bot token is required to connect bot with discord server
BOT_TOKEN = "Upon request"
CHANNEL_ID = 1211167948912336897


@dataclass
class Session:
  is_active: bool = False
  start_time: int = 0

# ! sign is the call sign to summon the bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

session = Session()

#This is the function that is called when the bot is ready to be used
@bot.event
async def on_ready():
  

  channel = bot.get_channel(CHANNEL_ID)
  await channel.send("""
  Hello! Commands: 
  !easy_database, !medium_database, !hard_database, 
  !easy_algorithms, !medium_algorithms, !hard_algorithms, 
  !easy_concurrency, !medium_concurrency, !hard_concurrency, 
  !easy_javascript, !medium_javascript, !hard_javascript, 
  !easy_shell, !medium_shell, !hard_shell
                    """)


# ---------------------Bot Greetings---------------------
#Bot says hello!
@bot.command()
async def hello(ctx):
  await ctx.send("Hello!")


#bot says Goodbye!
@bot.command()
async def bye(ctx):
  await ctx.send("Goodbye!")


# ---------------------LeetCode---------------------

# ---------------------Algorithms---------------------
AlgorithmsEasy = [
    "https://leetcode.com/problems/two-sum/description/",
    "https://leetcode.com/problems/palindrome-number/description/",
    "https://leetcode.com/problems/roman-to-integer/description/",
    "https://leetcode.com/problems/longest-common-prefix/description/",
    "https://leetcode.com/problems/valid-parentheses/description/",
    "https://leetcode.com/problems/merge-two-sorted-lists/description/",
    "https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/",
    "https://leetcode.com/problems/remove-element/description/",
    "https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/",
    "https://leetcode.com/problems/search-insert-position/description/"
]

AlgorithmsMedium = [
    "https://leetcode.com/problems/add-two-numbers/description/",
    "https://leetcode.com/problems/longest-substring-without-repeating-characters/description/",
    "https://leetcode.com/problems/longest-palindromic-substring/description/",
    "https://leetcode.com/problems/zigzag-conversion/description/",
    "https://leetcode.com/problems/reverse-integer/description/",
    "https://leetcode.com/problems/string-to-integer-atoi/description/",
    "https://leetcode.com/problems/container-with-most-water/description/",
    "https://leetcode.com/problems/integer-to-roman/description/",
    "https://leetcode.com/problems/3sum/description/"
]

AlgorithmsHard = [
    "https://leetcode.com/problems/greatest-common-divisor-traversal/description/?envType=daily-question&envId=2024-02-25",
    "https://leetcode.com/problems/median-of-two-sorted-arrays/description/",
    "https://leetcode.com/problems/regular-expression-matching/description/",
    "https://leetcode.com/problems/merge-k-sorted-lists/description/",
    "https://leetcode.com/problems/reverse-nodes-in-k-group/description/",
    "https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/",
    "https://leetcode.com/problems/longest-valid-parentheses/description/",
    "https://leetcode.com/problems/sudoku-solver/description/",
    "https://leetcode.com/problems/first-missing-positive/description/",
    "https://leetcode.com/problems/trapping-rain-water/description/"
]

# ---------------------Database---------------------

DatabaseEasy = [
    "https://leetcode.com/problems/combine-two-tables",
    "https://leetcode.com/problems/employees-earning-more-than-their-managers",
    "https://leetcode.com/problems/duplicate-emails",
    "https://leetcode.com/problems/customers-who-never-order",
    "https://leetcode.com/problems/delete-duplicate-emails",
    "https://leetcode.com/problems/rising-temperature",
    "https://leetcode.com/problems/game-play-analysis-i",
    "https://leetcode.com/problems/employee-bonus",
    "https://leetcode.com/problems/find-customer-referee",
    "https://leetcode.com/problems/customer-placing-the-largest-number-of-orders"
]

DatabaseMedium = [
    "https://leetcode.com/problems/second-highest-salary",
    "https://leetcode.com/problems/nth-highest-salary",
    "https://leetcode.com/problems/rank-scores",
    "https://leetcode.com/problems/consecutive-numbers",
    "https://leetcode.com/problems/department-highest-salary",
    "https://leetcode.com/problems/game-play-analysis-iv",
    "https://leetcode.com/problems/managers-with-at-least-5-direct-reports",
    "https://leetcode.com/problems/investments-in-2016",
    "https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends",
    "https://leetcode.com/problems/tree-node"
]

DatabaseHard = [
    "https://leetcode.com/problems/greatest-common-divisor-traversal/?envType=daily-question&envId=2024-02-25",
    "https://leetcode.com/problems/department-top-three-salaries",
    "https://leetcode.com/problems/trips-and-users",
    "https://leetcode.com/problems/human-traffic-of-stadium"
]

# ---------------------JavaScript---------------------

##JavaScript
JavaScriptEasy = [
    "https://leetcode.com/problems/counter/description/",
    "https://leetcode.com/problems/sleep/description/",
    "https://leetcode.com/problems/array-prototype-last/description/",
    "https://leetcode.com/problems/function-composition/description/",
    "https://leetcode.com/problems/filter-elements-from-array/description/",
    "https://leetcode.com/problems/apply-transform-over-each-element-in-array/description/",
    "https://leetcode.com/problems/array-reduce-transformation/description/",
    "https://leetcode.com/problems/generate-fibonacci-sequence/description/",
    "https://leetcode.com/problems/counter-ii/description/"
]

JavaScriptMedium = [
    "https://leetcode.com/problems/check-if-object-instance-of-class/description/",
    "https://leetcode.com/problems/cache-with-time-limit/description/",
    "https://leetcode.com/problems/memoize/description/",
    "https://leetcode.com/problems/snail-traversal/description/",
    "https://leetcode.com/problems/flatten-deeply-nested-array/description/",
    "https://leetcode.com/problems/debounce/description/",
    "https://leetcode.com/problems/group-by/description/",
    "https://leetcode.com/problems/promise-time-limit/description/",
    "https://leetcode.com/problems/nested-array-generator/description/",
    "https://leetcode.com/problems/call-function-with-custom-context/description/"
]

JavaScriptDifficult = [
    "https://leetcode.com/problems/greatest-common-divisor-traversal/description/?envType=daily-question&envId=2024-02-25",
    "https://leetcode.com/problems/memoize-ii/description/",
    "https://leetcode.com/problems/design-cancellable-function/description/"
]

# ---------------------Pandas---------------------

##Pandas
PandasEasy = [
    "https://leetcode.com/problems/combine-two-tables/description/?lang=pythondata",
    "https://leetcode.com/problems/employees-earning-more-than-their-managers/description/?lang=pythondata",
    "https://leetcode.com/problems/duplicate-emails/description/?lang=pythondata",
    "https://leetcode.com/problems/customers-who-never-order/description/?lang=pythondata",
    "https://leetcode.com/problems/delete-duplicate-emails/description/?lang=pythondata",
    "https://leetcode.com/problems/rising-temperature/description/?lang=pythondata",
    "https://leetcode.com/problems/employee-bonus/description/?lang=pythondata",
    "https://leetcode.com/problems/find-customer-referee/description/?lang=pythondata",
    "https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/?lang=pythondata",
    "https://leetcode.com/problems/big-countries/description/?lang=pythondata"
]

PandasMedium = [
    "https://leetcode.com/problems/second-highest-salary/description/?lang=pythondata",
    "https://leetcode.com/problems/nth-highest-salary/description/?lang=pythondata",
    "https://leetcode.com/problems/rank-scores/description/?lang=pythondata",
    "https://leetcode.com/problems/consecutive-numbers/description/?lang=pythondata",
    "https://leetcode.com/problems/department-highest-salary/description/?lang=pythondata",
    "https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?lang=pythondata",
    "https://leetcode.com/problems/investments-in-2016/description/?lang=pythondata",
    "https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/?lang=pythondata",
    "https://leetcode.com/problems/tree-node/description/?lang=pythondata",
    "https://leetcode.com/problems/exchange-seats/description/?lang=pythondata"
]

PandasHard = [
    "https://leetcode.com/problems/greatest-common-divisor-traversal/description/?envType=daily-question&envId=2024-02-25",
    "https://leetcode.com/problems/department-top-three-salaries/description/?lang=pythondata",
    "https://leetcode.com/problems/trips-and-users/description/?lang=pythondata",
    "https://leetcode.com/problems/human-traffic-of-stadium/description/?lang=pythondata"
]

# ---------------------Shell---------------------

##Shell
ShellEasy = [
    "https://leetcode.com/problems/valid-phone-numbers/description/",
    "https://leetcode.com/problems/tenth-line/description/"
]

ShellMedium = [
    "https://leetcode.com/problems/word-frequency/description/",
    "https://leetcode.com/problems/transpose-file/description/"
]

ShellDifficult = [
    "https://leetcode.com/problems/greatest-common-divisor-traversal/?envType=daily-question&envId=2024-02-25"
]

# implement random difficult shell question here

# ---------------------Concurrency---------------------
ConcurrencyEasy = ["https://leetcode.com/problems/print-in-order/description/"]

ConcurrencyMedium = [
    "https://leetcode.com/problems/print-foobar-alternately/",
    "https://leetcode.com/problems/print-zero-even-odd/description/",
    "https://leetcode.com/problems/building-h2o/description/",
    "https://leetcode.com/problems/fizz-buzz-multithreaded/description/",
    "https://leetcode.com/problems/the-dining-philosophers/description/"
]

ConcurrencyHard = [
    "https://leetcode.com/problems/greatest-common-divisor-traversal/description/?envType=daily-question&envId=2024-02-25"
]

# implement random difficult concurrency question here

# ---------------------Algos---------------------

#Commands for requesting a certain type of problem
@bot.command()
async def easy_database(ctx):
  await ctx.send(random.choice(DatabaseEasy))
  # implement random easy database questions here


@bot.command()
async def medium_database(ctx):
  await ctx.send(random.choice(DatabaseMedium))
  # implement random medium database question here


@bot.command()
async def hard_database(ctx):
  await ctx.send(random.choice(DatabaseHard))
  # implement random difficult database question here


@bot.command()
async def easy_algorithms(ctx):
  await ctx.send(random.choice(AlgorithmsEasy))
  # implement random easy algorithms questions here


@bot.command()
async def medium_algorithms(ctx):
  await ctx.send(random.choice(AlgorithmsMedium))
  # implement random medium algorithms question here


@bot.command()
async def hard_algorithms(ctx):
  await ctx.send(random.choice(AlgorithmsHard))
  # implement random difficult algorithms question here


@bot.command()
async def easy_concurrency(ctx):
  await ctx.send(random.choice(ConcurrencyEasy))
  # implement random easy concurrency questions here


@bot.command()
async def medium_concurrency(ctx):
  await ctx.send(random.choice(ConcurrencyMedium))
  # implement random medium concurrency question here


@bot.command()
async def hard_concurrency(ctx):
  await ctx.send(random.choice(ConcurrencyHard))


@bot.command()
async def easy_javascript(ctx):
  await ctx.send(random.choice(JavaScriptEasy))
  # implement random easy javascript questions here


@bot.command()
async def medium_javascript(ctx):
  await ctx.send(random.choice(JavaScriptMedium))
  # implement random easy javascript questions here


@bot.command()
async def hard_javascript(ctx):
  await ctx.send(random.choice(JavaScriptDifficult))


@bot.command()
async def easy_shell(ctx):
  await ctx.send(random.choice(ShellEasy))
  # implement random easy shell questions here


@bot.command()
async def medium_shell(ctx):
  await ctx.send(random.choice(ShellMedium))
  # implement random medium shell question here


@bot.command()
async def hard_shell(ctx):
  await ctx.send(random.choice(ShellDifficult))


# Start the timer
@bot.command()
async def start(ctx):
  if session.is_active:
    await ctx.send("A session is already active!")
    return

  session.is_active = True
  session.start_time = ctx.message.created_at.timestamp()
  human_readable_time = ctx.message.created_at.strftime("Started at %H:%M:%S")
  await ctx.send(f"Session started at {human_readable_time}")


# ---------------------Bot Timers ---------------------


# End the timer
@bot.command()
async def end(ctx):
  if not session.is_active:
    await ctx.send("No session is already!")
    return

  session.is_active = False
  end_time = ctx.message.created_at.timestamp()
  duration = end_time - session.start_time
  human_readable_time = str(datetime.timedelta(seconds=duration))
  await ctx.send(f"Session ended after {human_readable_time}. ")


bot.run(BOT_TOKEN)

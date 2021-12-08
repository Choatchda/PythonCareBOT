import discord
import math
from discord.ext import commands

class math_data(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # ลองใช้เมธอด Math
        # ลองใช้ ceil
    @commands.command()
    async def ceil(self, ctx, *, par):
        x = math.ceil(float(par))
        emBed = discord.Embed(title="ลองใช้ math.ceil", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='number = {0}\nx = math.ceil(number)\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)
    
    # ลองใช้ log
    @commands.command()
    async def log(self, ctx, par, par2):
        x = math.log(int(par), int(par2))
        emBed = discord.Embed(title="ลองใช้ math.log", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='x = math.log({0}, {1})\nprint(x)' .format(par, par2))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)
    
    # ลองใช้ floor
    @commands.command()
    async def floor(self, ctx, *, par):
        x = math.floor(float(par))
        emBed = discord.Embed(title="ลองใช้ math.floor", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='number = {0}\nx = math.floor(number)\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)
    
    # @commands.command()

    # รับข้อความจาก User ใน Topic ต่างๆ
    @commands.Cog.listener("on_message")
    async def on_message(self, message):

        #  Math
        if message.content == "!math":
            emBed = discord.Embed(title="Math", description="import math เพื่อเป็นการเรียกใช้ฟังก์ชัน Math \
            \nจะเป็นฟังก์ชั่น Math ที่ใช้บ่อยในการทำโจทย์พิมพ์ !math ตามด้วยชื่อ Method เพื่อเรียกดู", color=0x6F9DC3)
            emBed.add_field(name="ceil", value='ปัดเศษขึ้น')
            emBed.add_field(name="floor", value='ปัดเศษลง')
            emBed.add_field(name="sqrt", value='Square root ตัวเลขที่เราใส่ลงไป')
            emBed.add_field(name="sin", value='เปลี่ยนค่าตัวเลขที่เราใส่ลงไปเป็นค่า Sin')
            emBed.add_field(name="cos", value='เปลี่ยนค่าตัวเลขที่เราใส่ลงไปเป็นค่า Cos')
            emBed.add_field(name="tan", value='เปลี่ยนค่าตัวเลขที่เราใส่ลงไปเป็นค่า Tan')
            emBed.add_field(name="radians", value='เปลี่ยนจาก Degree เป็น Radians')
            emBed.add_field(name="factorial", value='Return ค่าตัวเลขเป็น Factorial')
            emBed.add_field(name="log", value='Return ค่าเป็นตัวเลขเป็นค่า Log')
            emBed.add_field(name="pow", value='Return ค่าเป็นยกกำลัง')
            emBed.add_field(name="degrees", value='เปลี่ยนค่า Degree เป็น Radians')
            emBed.add_field(name="abs", value='Return ค่าตัวเลขเป็นค่าบวก', inline=False)
            await message.channel.send(embed=emBed)

        
        elif message.content == "!math ceil":
            emBed = discord.Embed(title="math.ceil", description="ปัดค่าขึ้น 1 เมื่อมีทศนิยมมากว่า 0", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = 1.5\nx = math.ceil(txt)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=2)
            emBed.add_field(name="ลองใช้ math.ceil", value='!ceil ตัวเลขที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)

        
        elif message.content == "!math floor":
            emBed = discord.Embed(title="math.floor", description="ปัดค่าลง 1 เมื่อมีทศนิยม", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "1.5"\nx = math.floor(txt)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='1')
            emBed.add_field(name="ลองใช้ floor", value='!floor ตัวเลขที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด copy
        elif message.content == "!math sqrt":
            emBed = discord.Embed(title="math.sqrt", description="Square root ตัวเลขที่เราใส่ลงไป", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "4"\nx = math.sqrt(txt)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=2)
            emBed.add_field(name="ลองใช้ sqrt", value='!sqrt ตัวเลขที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)
        #  List เมธอด count
        elif message.content == "!math sin":
            emBed = discord.Embed(title="math.sin", description="เปลี่ยนค่าตัวเลขเป็นค่า Sin", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "30"\nx = math.sin(txt)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="1/2")
            emBed.add_field(name="ลองใช้ sin", value='!sin ตัวเลขที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด extend
        elif message.content == "!math cos":
            emBed = discord.Embed(title="math.cos", description="เปลี่ยนค่าตัวเลขเป็นค่า Cos", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "60"\nx = math.cos(txt)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="1/2")
            emBed.add_field(name="ลองใช้ cos", value='!cos ตัวเลขที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด index
        elif message.content == "!math tan":
            emBed = discord.Embed(title="math.tan", description="เปลี่ยนค่าตัวเลขเป็นค่า Tan", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "45"\nx = math.sin(txt)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="1")
            emBed.add_field(name="ลองใช้ tan", value='!tan ตัวเลขที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด pop
        elif message.content == "!math radians":
            emBed = discord.Embed(title="math.radians", description="เปลี่ยนค่า Degrees เป็น Radians", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "90"\nx = math.raidans(txt)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=1.5707963267948966)
            emBed.add_field(name="ลองใช้ radians", value='!radians ตัวเลขที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด remove
        elif message.content == "!math factorial":
            emBed = discord.Embed(title="math.factorial", description="Return ค่าตัวเลขเป็น Factiroal number", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "6"\nx = math.factorial(txt)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=720)
            emBed.add_field(name="ลองใช้ factorial", value='!factorial ตัวเลขที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด reverse
        elif message.content == "!math log":
            emBed = discord.Embed(title="math.log", description="Return ค่าตัวเลขให้อยู่ในรูปของ Log", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "2"\nx = math.log(txt)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=0.6931471805599453)
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่า Parameter เพิ่มไปอีกหนึ่งตัวเพื่อเป็นฐานที่เราต้องการเเปลง ', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='x = math.log(8, 2)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=3)
            emBed.add_field(name="ลองใช้ log", value='!log ตัวเลขที่ต้องการ, ฐานที่ต้องการให้เเปลง', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด sort
        elif message.content == "!math pow":
            emBed = discord.Embed(title="math.pow", description="ต้องใส่ Parameter สองตัว โดยตัวเเเรกจะเป็นฐานเเละตัวที่สองเป็นเลขยกกำลัง", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='x = math.pow(2, 2)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=4)
            emBed.add_field(name="ลองใช้ pow", value='!pow ตัวเลขที่ต้องการ, ตัวเลขที่อยากให้ยกกำลัง', inline=False)
            await message.channel.send(embed=emBed)

        elif message.content == "!math degrees":
            emBed = discord.Embed(title="math.radians", description="เปลี่ยนค่า Radians เป็น Degree", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "1"\nx = math.raidans(txt)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=57.29577951308232)
            emBed.add_field(name="ลองใช้ degrees", value='!degrees ตัวเลขที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!math abs":
            emBed = discord.Embed(title="abs", description="เปลี่ยนค่าตัวเลขเป็นบวก โดย Absolute ไม่ต้อง Import Math ก็สามารถใช้ได้", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "-55"\nx = abs(txt)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=55)
            emBed.add_field(name="ลองใช้ abs", value='!abs ตัวเลขที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)


def setup(bot):
    bot.add_cog(math_data(bot))

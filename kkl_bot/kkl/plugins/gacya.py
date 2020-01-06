# -*- coding:utf-8 -*-
from nonebot import on_command, CommandSession, permission as perm
import nonebot
import random as rd
from PIL import Image
import os
root = os.path.join(os.path.dirname(__file__), 'plus', 'image')
os.chdir(root)
bot = nonebot.get_bot()
master = bot.config.MASTER[0]

gacya3 = ['杏奈', '真步', '璃乃',
          '初音', '霞', '伊緒',
          '咲戀', '望', '妮諾', '秋乃',
          '鏡華', '智', '真琴',
          '伊莉亞', '純', '靜流',
          '莫妮卡', '流夏', '吉塔',
          '亞里莎', '安', '古蕾婭',
          '空花（大江戶）', '妮諾（大江戶）']

gacya2 = ['茉莉', '茜里', '宮子',
          '雪', '七七香', '美里',
          '鈴奈', '香織', '美美',
          '綾音', '鈴', '惠理子',
          '忍', '真陽', '栞',
          '千歌', '空花', '珠希',
          '美冬', '深月', '紡希']

gacya1 = ['日和', '怜', '禊', '胡桃', '依里', '鈴莓', '優花梨', '碧', '美咲', '莉瑪', '步未']

fesgacya = ['矛依未', '克莉絲提娜']

up = ['碧（插班生）']
fes = '0'
isdouble = '0'
background = Image.new('RGBA', (330, 135), color='lavenderblush')
# up,3星,2星,1星
ordinary = [0.7, 1.8, 20.5, 77]  # 普通
double = [1.4, 3.6, 18, 77]  # 双倍

# gacya
@on_command('gacya10', aliases=('十连抽',), only_to_me=False)  # changed
async def gacya(session: CommandSession):
    gacya_3 = gacya3
    result = []
    msg = ''
    p = ordinary
    if fes == '1':
        p = double
        gacya_3 += fesgacya
    elif isdouble == '1':
        p = double
    sup, s3, s2 = 100-p[0], 100-p[0]-p[1], p[3]
    print(gacya_3)
    
    if session.ctx['message_type'] == 'group':
        msg = '[CQ:at,qq={}]\n'.format(str(session.ctx['user_id']))
    
    for n in range(9):
        i = rd.random()*100
        if i >= sup:  # up
            result.append(rd.choice(up))
        elif i >= s3 and i < sup:  # 3星
            result.append(rd.choice(gacya_3))
        elif i >= s2 and i < s3:  # 2星
            result.append(rd.choice(gacya2))
        else:  # 1星
            result.append(rd.choice(gacya1))
    result.append(rd.choice(gacya2)) if (rd.random()*100 <
                                         s3) else result.append(rd.choice(gacya_3+up))

    name = session.ctx['user_id']
    a = 0
    for x in range(5):
        for y in range(2):
            pic = Image.open(result[a] + '.png')
            background.paste(pic, (x*65+5, y*65+5))
            a += 1

    background.save(root+f'\\out\\{name}.png')
    await session.send(msg+f'[CQ:image,file=file:///{root}\\out\\{name}.png]')


@on_command('set_gacya', aliases=('卡池设置',), only_to_me=False)
async def set_gacya(session: CommandSession):
    global fes, isdouble
    if master == session.ctx['user_id']:
        msg = session.current_arg.strip()
        if not msg:
            msg = session.get('message', prompt='准备完成，请发送设置')
        fes = msg[0]
        try:
            isdouble = msg[1]
        except:
            isdouble = '0'
        await session.send(message=f'设置完成,现在卡池设置\nfes：{fes}\n双倍：{isdouble}')

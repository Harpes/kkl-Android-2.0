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
          '空花（大江戶）', '妮諾（大江戶）', '碧（插班生）']

gacya2 = ['茉莉', '茜里', '宮子',
          '雪', '七七香', '美里',
          '鈴奈', '香織', '美美',
          '綾音', '鈴', '惠理子',
          '忍', '真陽', '栞',
          '千歌', '空花', '珠希',
          '美冬', '深月', '紡希']

gacya1 = ['日和', '怜', '禊', '胡桃', '依里', '鈴莓', '優花梨', '碧', '美咲', '莉瑪', '步未']

fesgacya = ['矛依未', '克莉絲提娜']

up = ['克蘿依']
fes = '0'
isdouble = '0'
background = Image.new('RGBA', (330, 135), color='lavenderblush')
# up,3星,2星,1星
ordinary = [0.7, 1.8, 20.5, 77]  # 普通
double = [1.4, 3.6, 18, 77]  # 双倍


@on_command('onegacya', aliases=('单抽', ), only_to_me=False)
async def onegacya(session: CommandSession):
    gacya_3, p = gacya3, ordinary
    msg = ''
    if session.ctx['message_type'] == 'group':
        msg = '[CQ:at,qq={}] '.format(str(session.ctx['user_id']))

    if fes == '1':
        p = double
        gacya_3 += fesgacya
    elif isdouble == '1':
        p = double

    sup, s3, s2 = 100-p[0], 100-p[0]-p[1], p[3]
    pic = ''
    i = rd.random() * 100
    if i >= sup:  # up
        pic = rd.choice(up)
    elif i >= s3 and i < sup:  # 3星
        pic = rd.choice(gacya_3)
    elif i >= s2 and i < s3:  # 2星
        pic = rd.choice(gacya2)
    else:  # 1星
        pic = rd.choice(gacya1)

    pic = f'[CQ:image,file=file:///{root}\\{pic}.png]'

    await session.send(msg + pic)


@on_command('gacya10', aliases=('十连抽', ), only_to_me=False)
async def gacya10(session: CommandSession):
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
    n3, n2, n1 = [0, 0, 0]
    stones = [50, 10, 1]

    if session.ctx['message_type'] == 'group':
        msg = '[CQ:at,qq={}] '.format(str(session.ctx['user_id']))

    for x in range(10):
        i = rd.random() * 100
        if i >= sup:  # up
            result.append(rd.choice(up))
            n3 += 1
        elif i >= s3 and i < sup:  # 3星
            result.append(rd.choice(gacya_3))
            n3 += 1
        elif i >= s2 and i < s3:  # 2星
            result.append(rd.choice(gacya2))
            n2 += 1
        else:  # 1星
            if x == 9:
                result.append(rd.choice(gacya2))
                n2 += 1
            else:
                result.append(rd.choice(gacya1))
                n1 += 1

    msg += f'共计{n3 * stones[0] + n2 * stones[1] + n1 * stones[2]}个无名之石'

    name = session.ctx['user_id']
    a = 0
    for x in range(5):
        for y in range(2):
            pic = Image.open(result[a] + '.png')
            background.paste(pic, (x*65+5, y*65+5))
            a += 1
    background.save(root + f'\\out\\{name}.png')

    await session.send(msg + f'[CQ:image,file=file:///{root}\\out\\{name}.png]')


@on_command('set_gacya', aliases=('卡池设置', ), only_to_me=False)
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

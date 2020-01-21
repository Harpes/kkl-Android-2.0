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
          '空花（大江戶）', '妮諾（大江戶）', '碧（插班生）',
          '克蘿依']

gacya2 = ['茉莉', '茜里', '宮子',
          '雪', '七七香', '美里',
          '鈴奈', '香織', '美美',
          '綾音', '鈴', '惠理子',
          '忍', '真陽', '栞',
          '千歌', '空花', '珠希',
          '美冬', '深月', '紡希']

gacya1 = ['日和', '怜', '禊', '胡桃', '依里', '鈴莓', '優花梨', '碧', '美咲', '莉瑪', '步未']

fesgacya = ['矛依未', '克莉絲提娜']

up = ['ネネカ']

background = Image.new('RGBA', (330, 135), color='lavenderblush')
# up,3星,2星,1星
# ordinary = [0.7, 1.8, 20.5, 77]  # 普通
# ordinary = [1.4, 3.6, 18, 77]  # up双倍
ordinary = [0.7, 4.3, 18, 77]  # 三星双倍


@on_command('onegacya', aliases=('单抽', ), only_to_me=False)
async def onegacya(session: CommandSession):
    gacya_3, p = gacya3, ordinary
    gacya_3 += fesgacya

    msg = ''
    if session.ctx['message_type'] == 'group':
        msg = '[CQ:at,qq={}] '.format(str(session.ctx['user_id']))

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
    gacya_3 += fesgacya

    result = []
    msg = ''
    p = ordinary

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


@on_command('gacya300', aliases=('抽一井', ), only_to_me=False)
async def gacya300(session: CommandSession):
    gacya_3 = gacya3
    gacya_3 += fesgacya

    result = []
    msg = ''
    p = ordinary

    sup, s3, s2 = 100-p[0], 100-p[0]-p[1], p[3]
    n3, n2, n1 = [0, 0, 0]
    stones = [50, 10, 1]

    if session.ctx['message_type'] == 'group':
        msg = '[CQ:at,qq={}] '.format(str(session.ctx['user_id']))

    for i in range(30):
        for x in range(10):
            i = rd.random() * 100
            if i >= sup:  # up
                result.append(rd.choice(up))
                n3 += 1
            elif i >= s3 and i < sup:  # 3星
                result.append(rd.choice(gacya_3))
                n3 += 1
            elif i >= s2 and i < s3:  # 2星
                # result.append(rd.choice(gacya2))
                n2 += 1
            else:  # 1星
                if x == 9:
                    # result.append(rd.choice(gacya2))
                    n2 += 1
                else:
                    # result.append(rd.choice(gacya1))
                    n1 += 1

    msg += f'获得{n3 * stones[0] + n2 * stones[1] + n1 * stones[2]}个无名之石'

    name = session.ctx['user_id']
    a = 0
    newPic = Image.new('RGBA', (n3 * 65 + 5, 70), color='lavenderblush')

    for x in range(n3):
        pic = Image.open(result[x] + '.png')
        newPic.paste(pic, (x * 65 + 5, 5))
    newPic.save(root + f'\\out\\{name}.png')
    msg += f'[CQ:image,file=file:///{root}\\out\\{name}.png]'

    msg += f'\n共计{n3}个三星，{n2}个两星，{n1}个一星'

    await session.send(msg)

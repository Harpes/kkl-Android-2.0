# -*- coding:utf-8 -*-
import re
from aiohttp import ClientSession
import json
from PIL import Image
import os
root=os.path.join(os.path.dirname(__file__),'image')
os.chdir(root)

#图片库
name={'100101': ['猫拳.png','日和','猫拳'],
      '100201': ['优衣.png','优衣','种田'],
      '100301': ['剑圣.png','怜','剑圣'],
      '100401': ['炸弹人.png','禊','炸弹人'],
      '100501': ['跳跳虎.png','茉莉','跳跳虎'],
      '100601': ['妹法.png','茜里','妹法'],
      '100701': ['布丁.png','宫子','布丁'],
      '100801': ['镜子.png','雪','镜子','小雪'],
      '100901': ['中二.png','杏奈','中二','煤气罐'],
      '101001': ['狐狸.png','真步','狐狸','真扎','咕噜灵波'],
      '101101': ['妹弓.png','璃乃','妹弓'],
      '101201': ['初音.png','初音','hego'],
      '101301': ['七七香.png','七七香','娜娜卡','眼睛法'],
      '101401': ['霞.png','霞','驴','侦探'],
      '101501': ['圣母.png','美里','圣母'],
      '101601': ['暴击弓.png','玲奈','暴击弓','政委'],
      '101701': ['狗.png','香织','狗子','狗'],
      '101801': ['魅魔.png','伊绪','老师','魅魔','io'],
      '102001': ['兔子.png','美美','兔子','兔兔'],
      '102101': ['铃铛.png','胡桃','铃铛'],
      '102201': ['姐法.png','伊里','姐法','姐姐法'],
      '102301': ['熊锤.png','绫音','熊锤'],
      '102501': ['女仆.png','铃莓','女仆'],
      '102601': ['松鼠.png','铃','松鼠'],
      '102701': ['病娇.png','惠理子','病娇'],
      '102801': ['充电宝.png','咲恋','充电宝'],
      '102901': ['偶像.png','望','偶像'],
      '103001': ['扇子.png','妮诺','扇子'],
      '103101': ['忍.png','忍','鬼父'],
      '103201': ['哈哈剑.png','秋乃','哈哈剑'],
      '103301': ['奶牛.png','真阳','奶牛'],
      '103401': ['黄骑.png','优花梨','黄骑','圣骑','酒鬼','奶骑'],
      '103601': ['xcw.png','镜华','xcw','小仓唯'],
      '103701': ['tomo.png','智','tomo','卜毛','小智'],
      '103801': ['tp弓.png','栞','tp弓','TP弓'],
      '104001': ['香菜.png','碧','香菜弓','香菜'],
      '104201': ['千歌.png','千歌','绿毛奶'],
      '104301': ['狼.png','真琴','狼','狼妹'],
      '104401': ['伊利亚.png','伊莉雅','yly','伊利亚'],
      '104501': ['抖m.png','空花','抖m','抖M'],
      '104601': ['猫剑.png','珠希','猫剑'],
      '104701': ['黑骑.png','纯','黑骑'],
      '104801': ['子龙.png','美冬','子龙'],
      '104901': ['姐姐.png','静流','姐姐'],
      '105001': ['大眼.png','美咲','大眼'],
      '105101': ['眼罩.png','深月','眼罩','抖s'],
      '105201': ['羊驼.png','莉玛','羊驼','草泥马'],
      '105301': ['莫妮卡.png','莫妮卡','毛二力','莫尼卡'],
      '105401': ['裁缝.png','纺希','裁缝'],
      '105501': ['路人.png','步未','路人','路人妹'],
      '105601': ['流夏.png','流夏','大姐','大姐头'],
      '105701': ['吉他.png','吉塔','吉他','团长','骑空士'],
      '105801': ['吃货.png','贪吃佩可','吃货'],
      '105901': ['可可萝.png','可可萝','妈','普白'],
      '106001': ['黑猫.png','凯留','黑猫','臭鼬'],
      '106101': ['511.png','矛依未','511','夏娜'],
      '106301': ['亚里莎.png','亚里莎','瞎子','鸭梨瞎','鸭梨傻','亚里沙'],
      '107001': ['似似花.png','似似花','448'],
      '107101': ['克总.png','克里斯蒂娜','克总','女帝'],
      '107501': ['水吃.png','水吃','水吃货'],
      '107601': ['水白.png','水白'],
      '107701': ['水女仆.png','水女仆'],
      '107801': ['水黑.png','水黑'],
      '107901': ['水猫.png','水猫剑','水猫'],
      '108001': ['水子龙.png','水子龙'],
      '108101': ['万圣忍.png','万圣忍','瓜忍'],
      '108201': ['狼丁.png','万圣布丁','狼布丁','狼丁'],
      '108301': ['万圣大眼.png','万圣美咲','万圣大眼'],
      '108401': ['圣诞千歌.png','圣诞千歌','圣千'],
      '108501': ['圣诞铃铛.png','圣诞胡桃','圣诞铃铛'],
      '108601': ['圣诞熊锤.png','圣诞熊锤'],
      '108701': ['春猫.png','春猫'],
      '108801': ['春田.png','新春优衣','春田'],
      '108901': ['春剑.png','新春剑圣','春剑','春怜'],
      '109001': ['恋病.png','情人节病娇','恋病','情病'],
      '109101': ['情姐.png','情人节静流','情人节姐姐','情姐'],
      '109201': ['安.png','安'],
      '109301': ['露.png','露'],
      '109401': ['龙姬.png','古雷娅','龙姬'],
      '109501': ['江户抖m.png','江户空花','江户抖m','江户m','江户抖M'],
      '109601': ['江户扇子.png','江户扇子','忍扇'],
      '109701': ['蕾姆.png','蕾姆','雷姆'],
      '109801': ['拉姆.png','拉姆'],
      '109901': ['爱蜜莉雅.png','爱蜜莉雅','艾米莉亚','emt'],
      '110001': ['水爆弓.png','瀑击弓','水爆弓','水爆'],
      '110101': ['水魅魔.png','水魅魔','水老师'],
      '110301': ['水电站.png','水电','水电站','泳装充电宝'],
      '110401': ['水狼.jpg','水狼'],
      '110501': ['水狗.jpg','水狗'],
      '110601': ['水狐狸.png','水狐狸','水真步'],
      '110701': ['新香菜.png','新香菜'],
      '110801': ['华哥.png','华哥'],
      '110901': ['切露.png','切噜','切露'],
      '111001': ['优尼.png','优尼'],
      '111101': ['万圣唯.png','万圣xcw','万圣小仓唯','猫仓唯','猫唯'],
      '111201': ['万圣炸弹人.png','万圣炸弹人','万圣禊','万圣炸弹'],
      '111301': ['万圣兔子.png','万圣兔子','万圣美美','万圣兔兔'],
      '111401': ['露娜.png','露娜','璐娜','ルナ']}


# name>>>id
def user_input(msg):
    it=[]
    for i in name.values():
        it+=i
    msglst = msg.split(' ')
    numlst=[]
    if len(msglst) >= 6:
        return '最多五个人哦，或者不要带多余的空格'
    elif len(msglst) <= 4:
        return '一队要五个人哦，或者不要带多余的空格'
    for n in msglst:
        if n not in it:
              return (f'可可萝暂时不知道{n}是谁哦，请换个名称查询')
        for i,j in name.items():
            if n in j :
                numlst.append(int(i))
    for i in numlst :
        if numlst.count(i)>=2:
            return (f'{name[str(i)][1]}重复了，请重新查询')
    return numlst

# search
async def jjcsearch(numlst,key):
    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
              'authorization':key}                                                           #网站作者提供的key，用于绕过验证，作者qq：196435005
    payload = {"_sign":"a","def":numlst,"nonce":"a","page":1,"sort":1,"region":1,"ts":1567847361}
    url = 'https://api.pcrdfans.com/x/v1/search'
    async with ClientSession() as asyncsession:
        async with asyncsession.post(url,headers=header,data=json.dumps(payload)) as response:
            data = await response.read()
    #data = requests.post(url,headers = header,data = json.dumps(payload))
    pattens = '{"equip":.*?,"id":(\\d+),"star":.*?}'#专武 角色 星数
    num = re.findall(pattens ,data.decode())
    return num

# id>>>image
def jjc_output(result,id):
    #out_msg_list = []
    for n in range(len(result)):
        for i,j in name.items():
            if i == result[n]:
                result[n]=j[0]
    #for i in range(0,len(result),10):
#          print(i)
    out_msg_list=[result[i:i+5] for i in range(0,len(result),10)]
    bk=Image.new('RGBA',(330,int(len(out_msg_list))*70+10),color='lavenderblush')
    for i in range(len(out_msg_list)):
        for n in range(5):
            try:
                img=Image.open(out_msg_list[i][n])
            except:
                return f'结果中有未知ID【{i}】,请更新jjc资料库'
            bk.paste(img,(5+n*65,10+i*70))
    bk.save(root+f'\\jjc\\{id}.png')
    return f'已为骑士君[CQ:at,qq={id}]查到以下胜利队伍:\n[CQ:image,file=file:///{root}\\jjc\\{id}.png]'

# name>>>id>>>name
async def total(msg,id,key):
    #remsg=''
    if key=='':
        return '本功能暂未开放，请阅览源码'
    a=user_input(msg)         #返回list
    if type(a) != list:
        return a
    b=await jjcsearch(a,key)        #num
    if b != []:
        remsg=(jjc_output(b,id))
    else:
        remsg='抱歉，可可萝没有找到解法哦'
    return remsg

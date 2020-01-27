import nonebot
from nonebot import CommandSession, on_command

bot = nonebot.get_bot()

reservation = {i:  {} for i in range(1, 6)}
bossNames = {
    1: '一王', 2: '二王', 3: '三王', 4: '四王', 5: '五王'
}


async def reserve_function(session: CommandSession, bossN: int):
    context = session.ctx
    if context['message_type'] != 'group':
        return

    group_id = context['group_id']
    user_id = context['user_id']

    bossName = bossNames[bossN]

    reservation_list = reservation[bossN].get(group_id, [])
    if user_id in reservation_list:
        await session.send(f'[CQ:at,qq={user_id}] 你已预约过{bossName}，请勿重复预约')
    else:
        reservation_list.append(user_id)
        reservation[bossN][group_id] = reservation_list[:]
        await session.send(f'[CQ:at,qq={user_id}] 你已成功预约{bossName}，当前boss预约人数：{len(reservation_list)}')


async def callout_function(session: CommandSession, bossN: int):
    context = session.ctx
    if context['message_type'] != 'group':
        return

    group_id = context['group_id']
    bossName = bossNames[bossN]

    reservation_list = reservation[bossN].get(group_id, [])
    if len(reservation_list) == 0:
        await session.send('当前Boss没有人预约')
    else:
        msg = '公会战已轮到{}，请尽快出刀，如需下轮请重新预约。'.format(bossName)
        for user_id in reservation_list:
            msg += f'\n[CQ:at,qq={user_id}]'
        reservation[bossN][group_id] = []
        await session.send(msg)


@on_command('#reserve_one', aliases=('预约一王', ), only_to_me=False)
async def reserve_one(session: CommandSession):
    await reserve_function(session, 1)


@on_command('#reserve_two', aliases=('预约二王', ), only_to_me=False)
async def reserve_two(session: CommandSession):
    await reserve_function(session, 2)


@on_command('#reserve_three', aliases=('预约三王', ), only_to_me=False)
async def reserve_three(session: CommandSession):
    await reserve_function(session, 3)


@on_command('#reserve_four', aliases=('预约四王', ), only_to_me=False)
async def reserve_four(session: CommandSession):
    await reserve_function(session, 4)


@on_command('#reserve_five', aliases=('预约五王', ), only_to_me=False)
async def reserve_five(session: CommandSession):
    await reserve_function(session, 5)


@on_command('#call_one', aliases=('#一王', ), only_to_me=False)
async def call_one(session: CommandSession):
    await callout_function(session, 1)


@on_command('#call_two', aliases=('#二王', ), only_to_me=False)
async def call_two(session: CommandSession):
    await callout_function(session, 2)


@on_command('#call_three', aliases=('#三王', ), only_to_me=False)
async def call_three(session: CommandSession):
    await callout_function(session, 3)


@on_command('#call_four', aliases=('#四王', ), only_to_me=False)
async def call_four(session: CommandSession):
    await callout_function(session, 4)


@on_command('#call_five', aliases=('#五王', ), only_to_me=False)
async def call_five(session: CommandSession):
    await callout_function(session, 5)

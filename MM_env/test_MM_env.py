import sys

if "../" not in sys.path:
    sys.path.append("../")

#from exchg.lib.envs.simple_rooms import SimpleRoomsEnv
#from exchg.lib.envs.cliff_walking import CliffWalkingEnv
#from exchg.lib.simulation import Experiment

from exchg.exchg import Exchg

def total_sys_nav(e):
    sum = 0
    for trader in e.agents:
        sum += trader.acc.nav
    return sum

def print_info(e):
    e.render()
    for trader in e.agents:
        trader.acc.print_acc()
        print('total_sys_nav:', total_sys_nav(e))
    return 0

def _acc(e, ID):
    return (e.agents[ID].acc.cash,
            e.agents[ID].acc.cash_on_hold,
            e.agents[ID].acc.position_val,
            e.agents[ID].acc.nav,
            e.agents[ID].acc.net_position)

def create_env():
    num_of_traders = 4
    tape_display_length = 100
    init_cash = 10000
    max_step = 100
    e = Exchg(num_of_traders, init_cash, tape_display_length, max_step)
    return e

def test(e, expected_result_0, expected_result_1, expected_result_2, expected_result_3):
    """
    # get results
    result_0 = _acc(e, ID=0)
    result_1 = _acc(e, ID=1)
    result_2 = _acc(e, ID=2)
    result_3 = _acc(e, ID=3)
    print('expected_result_0:', expected_result_0)
    print('result_0:', result_0)
    print('expected_result_1:', expected_result_1)
    print('result_1:', result_1)
    print('expected_result_2:', expected_result_2)
    print('result_2:', result_2)
    print('expected_result_3:', expected_result_3)
    print('result_3:', result_3)
    #test
    assert(expected_result_0 == result_0)
    assert(expected_result_0 == result_1)
    assert(expected_result_1 == result_2)
    assert(expected_result_2 == result_3)
    """
    print_info(e)
    return 0

# place initial orders, 4 traders each with 3 bids, 3 asks all in LOB, no trade
def test_1(e):
    # bid
    action0 = {"type": 'limit', "side": 'bid', "size": 3, "price": 2}
    action1 = {"type": 'limit', "side": 'bid', "size": 4, "price": 5}
    action2 = {"type": 'limit', "side": 'bid', "size": 5, "price": 8}
    action3 = {"type": 'limit', "side": 'bid', "size": 6, "price": 11}
    actions = [action0,action1,action2,action3] # actions
    e.step(actions) # execute actions in 1 step
    action0 = {"type": 'limit', "side": 'bid', "size": 3, "price": 3}
    action1 = {"type": 'limit', "side": 'bid', "size": 4, "price": 6}
    action2 = {"type": 'limit', "side": 'bid', "size": 5, "price": 9}
    action3 = {"type": 'limit', "side": 'bid', "size": 6, "price": 12}
    actions = [action0,action1,action2,action3] # actions
    e.step(actions) # execute actions in 1 step
    action0 = {"type": 'limit', "side": 'bid', "size": 3, "price": 4}
    action1 = {"type": 'limit', "side": 'bid', "size": 4, "price": 7}
    action2 = {"type": 'limit', "side": 'bid', "size": 5, "price": 10}
    action3 = {"type": 'limit', "side": 'bid', "size": 6, "price": 13}
    actions = [action0,action1,action2,action3] # actions
    e.step(actions) # execute actions in 1 step
    # ask
    action0 = {"type": 'limit', "side": 'ask', "size": 3, "price": 14}
    action1 = {"type": 'limit', "side": 'ask', "size": 4, "price": 17}
    action2 = {"type": 'limit', "side": 'ask', "size": 5, "price": 20}
    action3 = {"type": 'limit', "side": 'ask', "size": 6, "price": 23}
    actions = [action0,action1,action2,action3] # actions
    e.step(actions) # execute actions in 1 step
    action0 = {"type": 'limit', "side": 'ask', "size": 3, "price": 15}
    action1 = {"type": 'limit', "side": 'ask', "size": 4, "price": 18}
    action2 = {"type": 'limit', "side": 'ask', "size": 5, "price": 21}
    action3 = {"type": 'limit', "side": 'ask', "size": 6, "price": 24}
    actions = [action0,action1,action2,action3] # actions
    e.step(actions) # execute actions in 1 step
    action0 = {"type": 'limit', "side": 'ask', "size": 3, "price": 16}
    action1 = {"type": 'limit', "side": 'ask', "size": 4, "price": 19}
    action2 = {"type": 'limit', "side": 'ask', "size": 5, "price": 22}
    action3 = {"type": 'limit', "side": 'ask', "size": 6, "price": 25}
    actions = [action0,action1,action2,action3] # actions
    e.step(actions) # execute actions in 1 step

    expected_result_0 = (10000, 0, 0, 10000, 0)
    expected_result_1 = (10000, 0, 0, 10000, 0)
    expected_result_2 = (10000, 0, 0, 10000, 0)
    expected_result_3 = (10000, 0, 0, 10000, 0)
    test(e, expected_result_0, expected_result_1, expected_result_2, expected_result_3)
    return 0
"""
LOB:
 ***Bids***
6@13/3 - 12
6@12/3 - 8
6@11/3 - 4
5@10/2 - 11
5@9/2 - 7
5@8/2 - 3
4@7/1 - 10
4@6/1 - 6
4@5/1 - 2
3@4/0 - 9
3@3/0 - 5
3@2/0 - 1

***Asks***
3@14/0 - 13
3@15/0 - 17
3@16/0 - 21
4@17/1 - 14
4@18/1 - 18
4@19/1 - 22
5@20/2 - 15
5@21/2 - 19
5@22/2 - 23
6@23/3 - 16
6@24/3 - 20
6@25/3 - 24
"""
# init long position for T0, counter party T0, T1, T2, T3(unfilled)
def test_1_1(e):
    # actions
    action0 = {"type": 'limit', "side": 'bid', "size": 50, "price": 27}
    action1 = {"type": 'limit', "side": None, "size": 4, "price": 3}
    action2 = {"type": 'limit', "side": None, "size": 5, "price": 4}
    action3 = {"type": 'limit', "side": None, "size": 6, "price": 5}
    actions = [action0,action1,action2,action3]
    e.step(actions) # execute actions in 1 step
    # hard coded expected results
    expected_result_0 = (10000, 0, 0, 10000, 0)
    expected_result_1 = (10000, 0, 0, 10000, 0)
    expected_result_2 = (10000, 0, 0, 10000, 0)
    expected_result_3 = (10000, 0, 0, 10000, 0)
    test(e, expected_result_0, expected_result_1, expected_result_2, expected_result_3)
    return 0
"""
LOB:
 ***Bids***
6@13/3 - 12
6@12/3 - 8
6@11/3 - 4
5@10/2 - 11
5@9/2 - 7
5@8/2 - 3
4@7/1 - 10
4@6/1 - 6
4@5/1 - 2
3@4/0 - 9
3@3/0 - 5
3@2/0 - 1

***Asks***
4@25/3 - 24

***tape***
Q @ $ (t) c/i side
2 @ 25 (25) 3/0 bid
6 @ 24 (25) 3/0 bid
6 @ 23 (25) 3/0 bid
5 @ 22 (25) 2/0 bid
5 @ 21 (25) 2/0 bid
5 @ 20 (25) 2/0 bid
4 @ 19 (25) 1/0 bid
4 @ 18 (25) 1/0 bid
4 @ 17 (25) 1/0 bid
3 @ 16 (25) 0/0 bid
3 @ 15 (25) 0/0 bid
3 @ 14 (25) 0/0 bid
"""
# init short position for T0, counter party T0, T1, T2, T3(unfilled)
def test_1_2(e):
    # actions
    action0 = {"type": 'limit', "side": 'ask', "size": 52, "price": 2}
    action1 = {"type": 'limit', "side": None, "size": 4, "price": 3}
    action2 = {"type": 'limit', "side": None, "size": 5, "price": 4}
    action3 = {"type": 'limit', "side": None, "size": 6, "price": 5}
    actions = [action0,action1,action2,action3]
    e.step(actions) # execute actions in 1 step
    expected_result_0 = (10000, 0, 0, 10000, 0)
    expected_result_1 = (10000, 0, 0, 10000, 0)
    expected_result_2 = (10000, 0, 0, 10000, 0)
    expected_result_3 = (10000, 0, 0, 10000, 0)
    test(e, expected_result_0, expected_result_1, expected_result_2, expected_result_3)
    return 0
"""
LOB:
 ***Bids***
2@2/0 - 1

***Asks***
3@14/0 - 13
3@15/0 - 17
3@16/0 - 21
4@17/1 - 14
4@18/1 - 18
4@19/1 - 22
5@20/2 - 15
5@21/2 - 19
5@22/2 - 23
6@23/3 - 16
6@24/3 - 20
6@25/3 - 24

***tape***
Q @ $ (t) c/i side        [flawed logic]                [correct value]
1 @ 2 (25) 0/0 ask  0  66
3 @ 3 (25) 0/0 ask  3  60
3 @ 4 (25) 0/0 ask  6  54
4 @ 5 (25) 1/0 ask  12 48                               45@
4 @ 6 (25) 1/0 ask  16 42                               41@
4 @ 7 (25) 1/0 ask  20 36                               37@
5 @ 8 (25) 2/0 ask  30 30                               33@[(5*8)+(28*11.11)/(5+28)]=10.64  87.08
5 @ 9 (25) 2/0 ask  35 24 362+155+45=562 562/28=20.07   28@[(5*9)+(23*11.57)/(5+23)]=11.11  59.11
5 @ 10 (25) 2/0 ask 40 18 246+66+50=362 362/23=15.74    23@[(5*10)+(18*12)]/(5+18)=11.57
6 @ 11 (25) 3/0 ask 54 12 156+24+66=246 246/18=13.67    18@[(6*11)+(12*12.5)]/(6+12)=12
6 @ 12 (25) 3/0 ask 60 6  78+6+72=156 156/12=13         12@12.5                             (12.5*12)-(12*12)=6
6 @ 13 (25) 3/0 ask 66 0  78                            6@13                                0

start pv: 78

total profit: 342

NEED VWAP
"""
# init short position for T0, counter party T0, T1, T2, T3(unfilled)
def test_1_3(e):
    # actions
    action0 = {"type": 'limit', "side": 'ask', "size": 14, "price": 2}
    action1 = {"type": 'limit', "side": None, "size": 4, "price": 3}
    action2 = {"type": 'limit', "side": None, "size": 5, "price": 4}
    action3 = {"type": 'limit', "side": None, "size": 6, "price": 5}
    actions = [action0,action1,action2,action3]
    e.step(actions) # execute actions in 1 step
    expected_result_0 = (10000, 0, 0, 10000, 0)
    expected_result_1 = (10000, 0, 0, 10000, 0)
    expected_result_2 = (10000, 0, 0, 10000, 0)
    expected_result_3 = (10000, 0, 0, 10000, 0)
    test(e, expected_result_0, expected_result_1, expected_result_2, expected_result_3)
    return 0

def test_random():
    num_of_traders = 4
    init_cash = 10000
    tape_display_length = 100
    max_step = 100
    e = Exchg(num_of_traders, init_cash, tape_display_length, max_step)
    for step in range(max_step):
        actions = []
        for i, trader in enumerate(e.agents):
            action = trader.select_random_action(e)
            actions.append(action)
        print('\n\n\nSTEP:', step)
        print(actions)
        e.step(actions)
        print_info(e)


if __name__ == "__main__":
    e = create_env()
    test_1(e) # place initial orders
    test_1_1(e)
    #test_1_2(e)
    test_1_3(e)
    #test_1_4()

    #test_random()

    sys.exit(0)

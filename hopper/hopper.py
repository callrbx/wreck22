#!/usr/local/bin/python

from pwn import *
import os
import random

choices = []

runs = []


def remote_solve(moves):
    sh = remote("challs.wreckctf.com", 31714)
    made = 0
    try:
        for m in moves:
            sh.sendline(m)
            made += 1

        sh.interactive()
    except:
        print(f"Failed at {made}/{len(moves)}")


def do_hop(state):
    hopper = state['hopper']
    line = state['line']

    hops = [
        (hopper - 4, hopper >= 4),
        (hopper - 1, hopper % 4 != 0),
        (hopper + 1, hopper % 4 != 3),
        (hopper + 4, hopper < 12),
    ]

    hoppees = {line[hop]: hop for hop, legal in hops if legal}
    people = ', '.join(hoppees)

    # print('oh no! the order of the line is wrong!')
    # print(f'you can hop with {people}.')

    # print(hoppees)

    hoppee = None
    for p in hoppees:
        if hopper == valid_state.index(p):
            hoppee = p

    # print("Suggested:", hoppee)
    # print("Should be:", valid_state[hopper])
    # hoppee = input('who do you choose? ')
    # if hoppee not in hoppees:
    #     print('can\'t hop there!')
    #     return

    hoppee = random.choice(list(hoppees))
    tries = 0

    while line.index(hoppee) == valid_state.index(hoppee):
        hoppee = random.choice(list(hoppees))
        tries += 1
        if tries > len(hoppees):
            break

    choices.append(hoppee.encode('utf-8'))
    target = hoppees[hoppee]
    line[hopper], line[target] = line[target], line[hopper]
    state['hopper'] = target


def fixed(state):
    position = {hoppee: i for i, hoppee in enumerate(state['line'])}
    if position['olive'] > position['olen']:
        return False
    if position['shauna'] > position['constance']:
        return False
    if position['zane'] > position['tracie']:
        return False
    if position['loretta'] > position['chasity']:
        return False
    if position['gracie'] > position['shauna']:
        return False
    if position['tracie'] > position['louie']:
        return False
    if position['bertram'] > position['antoinette']:
        return False
    if position['antoinette'] > position['dana']:
        return False
    if position['constance'] > position['bertram']:
        return False
    if position['louie'] > position['wes']:
        return False
    if position['olen'] > position['hopper']:
        return False
    if position['wes'] > position['loretta']:
        return False
    if position['chasity'] > position['olive']:
        return False
    if position['rosemarie'] > position['gracie']:
        return False
    if position['dana'] > position['zane']:
        return False
    return True


for i in range(100):
    state = {
        'hopper': 0,
        'line': [
            'hopper',
            'wes',
            'gracie',
            'zane',
            'constance',
            'rosemarie',
            'shauna',
            'chasity',
            'louie',
            'tracie',
            'dana',
            'olen',
            'olive',
            'loretta',
            'bertram',
            'antoinette',
        ],
    }

    valid_state = ['rosemarie',
                   'gracie',
                   'shauna',
                   'constance',
                   'bertram',
                   'antoinette',
                   'dana',
                   'zane',
                   'tracie',
                   'louie',
                   'wes',
                   'loretta',
                   'chasity',
                   'olive',
                   'olen',
                   'hopper',
                   ]

    while not fixed(state):
        do_hop(state)

    # print(os.environ.get('FLAG', 'no flag provided!'))
    print("Completed:", i, len(choices))
    runs.append((len(choices), choices))
    if len(choices) < 3000:
        print("Bypassing now")
        remote_solve(choices)
    choices = []


runs.sort()

print("Attempting remote solve with", runs[0][0])
remote_solve(runs[0][1])


# flag{oops_a_fifteen_puzzle}

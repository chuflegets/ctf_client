import asyncio
import aiohttp
import base64
import json
import time
import urllib.parse

successful_data = [
    ['c', 'o', 'r', 'o', 'n', 'a', '-', 'v', 'i', 'r', 'u', 's', 'u', 's', '.', 'c', 'o', 'm'],
    ['c', 'o', 'r', 'o', 'n', 'a', 'v', 'i', 'r', 'u', 's', '.', 'm', 'e', 'd', 's', '.', 'c', 'o', 'm'],
    ['c', 'o', 'r', 'o', 'n', 'a', 'v', 'i', 'r', 'u', 's', 'c', 'o', 'n', 't', 'a', 'i', 'n', '.', 'c', 'o', 'm'],
    ['c', 'o', 'r', 'o', 'n', 'a', 'v', 'i', 'r', 'u', 's', 'c', 'o', 'n', 't', 'a', 'i', 'n', 'e', 'd', '.', 'c', 'o',
     'm'],
    ['c', 'o', 'r', 'o', 'n', 'a', 'v', 'i', 'r', 'u', 's', 'f', 'e', 'e', 'd', 'b', 'a', 'c', 'k', '.', 'c', 'o', 'm'],
    ['c', 'o', 'r', 'o', 'n', 'a', 'v', 'i', 'r', 'u', 's', 'h', 'a', 'r', 'm', '.', 'c', 'o', 'm'],
    ['c', 'o', 'r', 'o', 'n', 'a', 'v', 'i', 'r', 'u', 's', 'h', 'a', 'z', 'a', 'r', 'd', '.', 'c', 'o', 'm'],
    ['c', 'o', 'r', 'o', 'n', 'a', 'v', 'i', 'r', 'u', 's', 'm', 'e', 's', 's', 'a', 'g', 'e', '.', 'c', 'o', 'm'],
    ['c', 'o', 'r', 'o', 'n', 'a', 'v', 'i', 'r', 'u', 's', 't', 'r', 'o', 'u', 'b', 'l', 'e', '.', 'c', 'o', 'm'],
    ['f', 'i', 'g', 'h', 't', 'c', 'o', 'v', 'i', 'd', '.', 'p', 'r', 'o', 'f', 'i', 't', 'a', 'b', 'i', 't', '.', 'c',
     'l', 'u', 'b'],
    ['m', 'a', 's', 'k', '.', 'c', 'o', 'r', 'o', 'n', 'a', 'p', 'r', 'o', 't', 'e', 'c', 't', 'i', 'v', 'e', '.', 's',
     't', 'o', 'r', 'e'],
    ['c', 'o', 'r', 'o', 'n', 'a', 'v', 'i', 'r', 'u', 's', '-', 'g', 'u', 'i', 'd', 'a', 'n', 'c', 'e',
     '.', 'c', 'o', 'm'],
    ['n', 'y', 'c', 'o', 'v', 'i', 'd', '-', '1', '9', 'c', 'a', 's', 'e', 's', '.', 'c', 'o', 'm'],
    ['c', 'o', 'v', 'i', 'd', 'n', 'e', 'w', 's', 'u', 'p', 'd', 'a', 't', 'e', '.', 'o', 'n', 'l', 'i',
     'n', 'e'],
    ['c', 'o', 'v', 'i', 'd', 'v', 'o', 'i', 'c', 'e', 'p', 'o', 'r', 't', 'a', 'l', '.', 'c', 'o', 'm'],
    ['p', 'o', 'r', 't', 'a', 'l', '-', 'c', 'o', 'v', 'i', 'd', '-', '1', '9', '.', 'm', 'l'],
    ['p', 'o', 'r', 't', 'a', 'l', '-', 'c', 'o', 'v', 'i', 'd', '-', '1', '9', '.', 'g', 'a'],
    ['a', 'y', 'a', 'n', 'g', 'a', 'r', 't', 's', '.', 'o', 'r', '.', 'k', 'r'],
    ['c', 'o', 'v', 'i', 'd', '-', '1', '9', 'd', 'o', 'n', 'o', 'r', '.', 'c', 'o', 'm'],
    ['c', 'o', 'v', 'i', 'd', '1', '9', 'g', 'r', 'a', 'n', 't', 'o', 'r', '.', 'c', 'o', 'm'],
    ['c', 'o', 'v', 'i', 'd', '-', '1', '9', 'd', 'o', 'n', 'a', 't', 'o', 'r', '.', 'c', 'o', 'm'],
    ['c', 'u', 'r', 'e', 'c', 'o', 'r', 'o', 'n', 'a', 'v', 'i', 'r', 'u', 's', '.', 'l', 'i', 'f', 'e'],
    ['c', 'o', 'r', 'o', 'n', 'a', 'v', 'i', 'r', 'u', 's', 'r', 'e', 's', 'o', 'n', 'a', 'n', 'c', 'e',
     'c', 'u', 'r', 'e', '.', 'c', 'o', 'm']
]

fake_data = [['1', '0', '0', '4', '.', 'i', 'n'],
             ['a', 'a', 'b', 'i', 'o', 'k', 'y', 'a', 'g', 'd', 'w', '.', 'c', 'o', 'm'],
             ['4', 'g', 'o', '2', 'c', 'o', 'm', '.', 'n', 'e', 't'],
             ['a', 'd', 'm', 'e', 'd', 'i', 'a', 'd', 'e', 'l', 'i', 'v', 'e', 'r', 'y', '.', 'c', 'o', '.', 'c', 'c'],
             ['6', '0', '0', '0', '0', '0', '0', '.', 'i', 'n'],
             ['a', 'd', 'o', 'b', 'e', 's', 'u', 'p', 'p', 'o', 'r', 't', '.', 'p', 'e', 'r', 'l', '.', 's', 'h'],
             ['7', 'c', 'y', '.', 'n', 'e', 't'],
             ['a', 'h', 'a', 'n', 'i', 'n', 'u', 'i', 'a', 'e', '.', 'p', 'u', 'b', 'l', 'i', 'c', 'v', 'm', '.', 'c',
              'o', 'm'], ['a', 'e', 'r', 'y', 'b', 'o', 'e', 'm', '.', 'i', 'n', 'f', 'o'],
             ['a', 'r', 'e', 'a', 'c', 'o', 'd', 'e', 's', 'z', 'o', 'n', 'e', '.', 'i', 'n'],
             ['a', 'g', 'r', 'e', 'b', 'l', 'e', 'i', 'c', 'e', '.', 'c', 'o', 'm'],
             ['a', 's', 'h', 'a', 'm', 'p', 'o', 'o', '-', '1', '5', '.', 'c', 'o', 'm'],
             ['a', 'l', 'l', '4', 'c', 'o', 'r', 'p', '.', 'c', 'o', 'm'],
             ['a', 's', 'h', 'a', 'm', 'p', 'o', 'o', '-', '1', '8', '.', 'c', 'o', 'm'],
             ['a', 'r', 'y', 'a', 'h', 'o', 'o', '.', 'i', 'n', 'f', 'o'],
             ['a', 's', 'h', 'a', 'm', 'p', 'o', 'o', '-', '1', '9', '.', 'c', 'o', 'm'],
             ['a', 't', 'l', 'a', 'n', 't', 'i', 's', 'c', '.', 'n', 'e', 't'],
             ['a', 'z', 't', 'e', 'c', 'i', 'n', 't', 'e', 'r', 'n', 'a', 't', 'i', 'o', 'n', 'a', 'l', '.', 'c', 'o',
              'm', '.', 'a', 'u'], ['a', 'v', 'y', 'g', 'a', 'm', 'e', 'r', '.', 'c', 'o', '.', 'u', 'k'],
             ['b', 'a', 's', 'i', 'c', 'r', 'e', 'a', 'd', 'e', 'r', '.', 'c', 'o', '.', 'c', 'c'],
             ['b', 'a', 's', 's', 'e', 'a', 'r', 'c', 'h', '.', 'i', 'n', 'f', 'o'],
             ['b', 'e', 'e', 'r', 'h', 'o', 'u', 's', 'e', '.', 'c', 'z', '.', 'c', 'c'],
             ['b', 'f', 't', 'o', 'p', '.', 'r', 'u'],
             ['b', 'l', 'a', 'd', 'e', 'n', 'r', 'a', 'e', 'd', 'e', 's', '.', 'o', 'r', 'g'],
             ['b', 'l', 'i', 'n', 'd', 'r', 'y', '.', 'c', 'o', 'm'],
             ['c', 'a', 'd', 'a', 's', 't', 'r', 'o', '-', 'r', 'e', 'a', 'l', '.', 'c', 'o', 'm'],
             ['b', 'u', 't', 'e', 'h', 'o', 't', 'e', 'l', '.', 'c', 'o', 'm'],
             ['c', 'o', 'n', 's', 'o', 'r', 'z', 'i', 'o', 'n', 'a', 'v', 'i', 'g', 'l', 'i', '.', 'i', 't'],
             ['c', '0', '1', '0', 'x', '1', '.', 'c', 'o', '.', 'c', 'c'],
             ['c', 'r', 'o', 'n', 'e', 'n', 's', 't', 'r', '.', 'c', 'o', '.', 'c', 'c'],
             ['c', 'o', 'c', 'a', '4', 'k', 'a', '.', 'i', 'n', 'f', 'o'],
             ['d', 'e', 's', 'e', 'p', 'r', 'o', 't', 'i', 'k', 'a', 's', 't', '.', 'c', 'o', 'm'],
             ['c', 'o', 'c', 'a', 'l', 'a', '.', 'i', 'n', 'f', 'o'],
             ['d', 'f', 'a', 's', 'd', 'g', 'k', 'g', 't', '.', 'c', 'z', '.', 'c', 'c'],
             ['c', 'o', 'm', 'c', 'a', 's', 't', 'e', '.', 'c', 'o', '.', 'c', 'c'],
             ['d', 'f', 'g', 'y', 't', 'c', 'o', 'd', 'g', 'd', 'w', '.', 'c', 'o', 'm'],
             ['c', 'o', 'o', '0', 'l', 'n', 'e', 't', '.', 'n', 'e', 't'],
             ['d', 'o', 'w', 'n', '.', 'p', 'l', 'a', 'y', 'd', 'n', 's', '.', 'i', 'n', 'f', 'o'],
             ['c', 'o', 'z', 'e', 'm', 'u', '7', '.', 'c', 'o', '.', 'c', 'c'],
             ['d', 'r', 'u', 'm', 'm', 'i', 'n', 'g', 'm', 'a', 'd', '.', 'c', 'o', 'm'],
             ['e', 'a', 'l', 'o', '.', 'n', 'e', 't'],
             ['f', 'g', 's', 'd', 'f', 's', 'd', 'f', 'f', 'g', '3', '.', 'c', 'o', '.', 'c', 'c'],
             ['e', 'l', '-', 'p', 'i', 'c', 's', '.', 'c', 'o', 'm'],
             ['f', 'o', 'r', '-', 'a', 'd', 'v', 'a', 'n', 'c', 'e', 'd', '-', 'c', 'f', 'g', '2', '.', 'c', 'o', 'm'],
             ['e', 'l', 'l', 's', 'e', 'a', 'r', 'c', 'h', '.', 'i', 'n', 'f', 'o'],
             ['f', 'r', 'e', 'e', '-', 'b', 'i', 'g', '-', 'd', 'a', 't', 'a', '.', 'c', 'o', 'm'],
             ['e', 't', 'd', 'w', '.', 'c', 'o', '.', 'c', 'c'],
             ['f', 'r', 'e', 'e', 'i', 'n', 'f', 'o', 'a', 'r', 'e', 'a', 'c', 'o', 'd', 'e', '.', 'c', 'o', 'm'],
             ['f', 'i', 'b', 'e', 'r', 'l', 'i', 'n', 'e', 'z', '.', 'c', 'o', 'm'],
             ['f', 'r', 'i', 'l', 'l', 'e', 'd', '-', 'd', 'r', 'a', 'g', 'o', 'n', '.', 'c', 'o', 'm'],
             ['g', 'a', 't', 'e', '3', '3', '.', 'i', 'n', 'f', 'o'],
             ['f', 'u', 'n', 'k', 'y', 's', 't', 'u', 'f', 'f', 'h', 'e', 'r', 'e', '.', 'k', 'i', 'c', 'k', 'm', 'e',
              '.', 't', 'o'], ['g', 'e', 'n', 'o', 'e', 'c', 'o', '.', 'c', 'o', 'm'],
             ['f', 'v', 'r', 'w', 'q', 't', 'v', 'e', 'd', 'j', 'q', 't', 'h', 'l', 'n', '.', 'c', 'o', 'm'],
             ['g', 'r', 'e', 'a', 't', 'r', 'e', 'l', 'o', 'a', 'd', '.', 'i', 'n'],
             ['f', 'x', '0', '1', '0', '4', '1', '3', '.', 'w', 'h', 'y', 'i', '.', 'o', 'r', 'g'],
             ['h', 'm', 'm', 'i', 'k', 'r', '.', 'c', 'o', 'm'],
             ['g', 'o', 'f', 'o', 'r', 'b', 'r', 'o', 'k', 'e', '.', 'r', 'e', 'a', 'd', 's', '.', 'i', 't'],
             ['j', 'j', 'w', 'e', 'x', 't', 'x', 'f', '.', 'c', 'o', 'm'],
             ['g', 'r', 'e', 'a', 't', 'r', 'e', 'a', 'c', 't', 'o', 'r', '.', 'c', 'o', '.', 'c', 'c'],
             ['j', 'x', '2', 'd', 'b', 't', 'w', 'g', '.', 'c', 'o', 'm'],
             ['h', 'e', 'l', 'p', '.', 'i', 'p', 't', 'a', 'b', 'l', 'e', 's', '.', 'w', 's'],
             ['k', 'a', 'x', 'n', '.', 'r', 'u'],
             ['h', 'e', 'r', 'e', '.', 'g', 'e', 't', '-', '2', '0', '1', '1', '-', 'v', 'e', 'r', 's', 'i', 'o', 'n',
              '-', 'n', 'o', 'w', '.', 'i', 'n', 'f', 'o'], ['k', 'i', 'n', 'o', 'k', 'o', 'l', '.', 'n', 'e', 't'],
             ['h', 'o', 'c', 'k', 'e', 'y', 'm', 'i', 'n', 'n', 'i', 'e', '.', 'c', 'o', '.', 'c', 'c'],
             ['l', 'i', 'd', 'e', 'r', '3', '3', '.', 't', 'k'],
             ['h', 'u', 'e', 'k', 'a', 'c', 'u', 'g', 'e', 'g', 'u', 'j', 'e', 'd', '.', 'l', 'i', 'n', 'k', 'p', 'c',
              '.', 'n', 'e', 't'], ['l', 'i', 'n', 'k', 'b', 'u', 'z', 'z', '7', '6', '.', 'e', 'u'],
             ['j', 'd', 'f', 'h', 'd', 's', 'g', 's', '4', '.', 'c', 'o', '.', 'c', 'c'],
             ['l', 'l', '1', '2', '.', 'r', 'u'],
             ['l', 'd', 'n', '5', '.', 's', 'p', 'i', 'd', 'e', 'r', 'w', 'w', 'w', '.', 'c', 'o', '.', 'c', 'c'],
             ['l', 'o', 'y', 'e', 'j', 'e', '5', '.', 'c', 'o', '.', 'c', 'c'],
             ['m', 'e', 'd', 'i', 'a', 't', 'r', 'a', 'c', 'k', 'i', 'n', 'g', '.', 'c', 'o', '.', 'c', 'c'],
             ['m', 'e', 'g', 'e', 'm', 's', '.', 'n', 'e', 't'],
             ['m', 'e', 'm', 'o', 'r', 'i', 's', 't', 'e', 'a', 'k', '.', 'c', 'o', '.', 'c', 'c'],
             ['m', 'o', 'd', 'a', 'c', 't', 'i', 'o', 'n', '.', 'r', 'u'],
             ['m', 'i', 'c', 'r', 'o', 's', 'o', 'f', 't', 'w', 'i', 'n', 'd', 'o', 'w', 's', 's', 'e', 'c', 'u', 'r',
              'i', 't', 'y', '1', '8', '1', '.', 'c', 'o', 'm'],
             ['n', 'e', 'f', 'e', 'm', 'o', '2', '.', 'c', 'o', '.', 'c', 'c'],
             ['n', 'e', 'x', 't', '-', 'f', 'i', 'l', 'e', '-', 's', 'e', 'r', 'v', 'e', 'r', '.', 'c', 'o', 'm'],
             ['n', 'o', 'f', 'o', 't', 'o', 'r', 'a', 'i', 'd', '.', 'n', 'e', 't'],
             ['o', 'l', 'd', 'd', 'e', 's', 'i', 'n', 'g', 'q', 'u', 't', 'i', 'm', '.', 'c', 'o', 'm'],
             ['n', 'o', 'n', 'o', 'n', 'o', 'n', 'u', 'n', 'u', '.', 'c', 'o', 'm'],
             ['o', 'n', 'l', 'i', 'n', 'e', '-', 'a', 'l', 'e', 'r', 't', '-', 'p', 'o', 'l', 'i', 'c', 'y', '6', '2',
              '.', 'c', 'o', '.', 'c', 'c'], ['o', 'z', 'o', 'n', 'e', '7', '7', '7', '.', 'c', 'o', 'm'],
             ['o', 'n', 'l', 'y', 'o', 'n', 'y', 'x', '1', '0', '.', 'c', 'o', 'm'],
             ['p', 'a', 'r', 't', 'i', '2', '0', '.', 'c', 'o', '.', 'c', 'c'],
             ['o', 'o', 'o', 'a', 'b', 't', 'e', 'r', 'a', 's', 't', '0', '.', 'c', 'o', '.', 'c', 'c'],
             ['p', 'e', 'r', 'c', 'o', 'n', 'e', 'l', '.', 'c', 'o', 'm'],
             ['p', 'e', 'r', 'f', 'o', 'r', 'm', 'a', 'n', 'c', 'e', 'c', 'a', 'r', 'c', 'o', 'm', 'p', 'a', 'n', 'y',
              '.', 'c', 'o', 'm'], ['p', 'i', 'n', 'k', 'i', 'z', '.', 'c', 'o', 'm'],
             ['p', 'o', 'p', 'g', 'o', 'e', 's', 't', 'h', 'e', 'w', 'e', 'e', 'k', '.', 'c', 'o', 'm'],
             ['p', 'o', 'o', 'n', 's', 't', 'a', 'r', 't', '.', 'r', 'u'],
             ['p', 'o', 'r', 'n', '-', 'h', 'u', 'n', 't', '.', 'c', 'z', '.', 'c', 'c'],
             ['q', 'w', 'w', 'w', 'w', '.', 'c', 'o', '.', 'c', 'c'],
             ['p', 'o', 'r', 'n', '-', 'h', 'u', 'n', 't', 'e', 'r', '.', 'c', 'z', '.', 'c', 'c'],
             ['r', 'e', 'd', 'f', 'j', 'h', 's', 'f', 'k', '.', 'c', 'o', 'm'],
             ['p', 'o', 'r', 'n', 't', 'u', 'b', 'e', 'x', 'x', 'l', '.', 'c', 'o', 'm'],
             ['r', 'e', 'k', 'e', 't', 'f', 'o', 't', 'o', '.', 'r', 'u'],
             ['p', 'o', 's', 't', 'c', 'a', 'r', 'd', 's', 's', 'e', 'r', 'v', 'i', 'c', 'e', 's', '.', 'n', 'e', 't'],
             ['r', 'f', 'u', 's', 'h', 'o', 'p', '.', 'c', 'o', 'm'],
             ['p', 'r', 'i', 'v', 'a', 't', 'e', 'c', 'o', 'n', 'f', 'i', 'g', 'u', 'r', 'a', 't', 'i', 'o', 'n', 'f',
              'o', 'r', 'm', 'e', '.', 'c', 'o', 'm'], ['s', 'e', 'r', 'c', 'a', 'a', 'g', '.', 'c', 'o', 'm'],
             ['s', 'e', 'a', 'r', 'c', 'h', 'a', 'l', 't', 'h', 'o', 'u', 'g', 'h', '.', 'o', 'r', 'g'],
             ['s', 'g', 't', 'e', 'w', 'k', 'h', 'k', '.', 'b', 'i', 'z'],
             ['s', 'e', 'r', 'p', 'e', 'n', 't', 'a', 'r', 'i', 'u', 'm', '.', 'c', 'v', '.', 'u', 'a'],
             ['s', 'p', 'b', 'i', 'n', 'g', '.', 'c', 'o', 'm'],
             ['s', 'n', 'o', 'b', 'c', 'h', 'y', 'c', 't', '.', 'i', 'n', 'f', 'o'],
             ['t', 'i', 'n', 'k', 'i', '.', 'j', 'i', 'n', 'o', '.', 'r', 'u'],
             ['s', 't', 'e', 'a', 'm', 'c', 'a', 's', 't', 'l', 'e', 'r', 'u', 'n', '.', 'c', 'o', '.', 'c', 'c'],
             ['t', 'r', 'e', 'v', 'o', 'r', 's', 'e', 'e', '.', 'n', 'e', 't'],
             ['s', 'u', 'p', 'e', 'r', 'c', 'y', 'b', 'e', 'r', 's', 'e', 'c', 'u', 'r', 'i', 't', 'y', '.', 'c', 'o',
              'm'], ['u', 's', 'o', 'f', 'r', 'a', 'n', 'c', 'e', '.', 'f', 'r'],
             ['s', 'y', 's', 't', 'e', 'm', 'd', 'l', 'l', 's', 'u', 'p', 'd', '.', 'r', 'u'],
             ['u', 's', 'o', 's', 'o', 'p', '.', 'c', 'o', 'm'],
             ['t', 'i', 'm', 'e', '-', 's', 'y', 'n', 'c', '-', '2', '4', '.', 'n', 'e', 't'],
             ['v', 'e', 'i', 'c', 'l', '.', 'n', 'e', 't'],
             ['t', 'i', 'm', 'e', '-', 's', 'y', 'n', 'c', '-', '2', '4', 'y', '.', 'n', 'e', 't'],
             ['v', 'k', 'o', 't', 'a', 'l', 'k', 'e', '.', 'i', 'n', 'f', 'o'],
             ['u', 'n', 'n', 'u', 'r', 'h', 'm', 'i', 'n', 't', '.', 'c', 'o', 'm'],
             ['w', '1', 'z', 'z', 'z', '.', 'c', 'o', 'm'],
             ['u', 'n', 'u', 'b', 'i', 'g', 'l', 'e', 'n', 'r', '.', 'c', 'o', 'm'],
             ['w', 'e', 'b', 'y', 'e', 'e', 'w', 'o', 'r', 'x', '.', 'c', 'o', 'm'],
             ['v', 'a', 'n', 'd', 'e', 'l', 'i', 'v', 'e', 'n', 's', '.', 'o', 'r', 'g'],
             ['w', 'e', 'd', 'n', 'e', 's', 's', '.', 'c', 'v', '.', 'u', 'a'],
             ['w', 'i', 'n', 'h', 'o', 's', 't', 'm', 'a', 'n', 'a', 'g', 'e', 'r', '.', 'n', 'e', 't'],
             ['x', '1', 'x', '4', 'x', '0', '.', 'n', 'e', 't'],
             ['w', 'i', 'n', 'u', 'p', 'd', 'a', 't', 'e', 'c', 'o', 'n', 't', 'r', 'o', 'l', '.', 'n', 'e', 't'],
             ['z', 'e', 'd', 'o', 'z', 'e', '9', '.', 'c', 'o', '.', 'c', 'c'],
             ['z', 'u', 'n', 'd', 'e', 'r', '.', 'f', 'a', 'c', 'e', 'l', 'o', 'o', 'k', 'b', 's', '.', 'n', 'e', 't']
             ]

headers = {
    'Connection': 'close',
    'Upgrade-Insecure-Requests': str(1),
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/95.0'
}


def generate_domains():
    data = successful_data + fake_data
    return [''.join(pieces) for pieces in data]


def base64encode(domains):
    return [base64.b64encode(element.encode()).decode() for element in domains]


def urlencode(domains):
    return [urllib.parse.quote(element) for element in domains]


async def get_instructions(session, semaphore, c2server):
    url = f'http://{c2server}/ctf'
    async with semaphore, session.get(url, headers=headers) as response:
        return await response.text()


async def try_code(session, semaphore, c2server, code):
    url = f'http://{c2server}/ctf/pieces/{code}'
    async with semaphore, session.get(url, headers=headers) as response:
        return await response.text()


async def try_measure(session, semaphore, c2server, measure):
    url = f'http://{c2server}/ctf/prevent'
    data = json.dumps({
        'measure': measure
    })
    async with semaphore, session.post(url, data=data, headers=headers) as response:
        return await response.text()


async def main():
    c2server = 'localhost:1337'
    domains = generate_domains()
    codes = urlencode(base64encode(domains))
    concurrency_limit = len(codes) // 10
    semaphore = asyncio.Semaphore(concurrency_limit)
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_instructions(session, semaphore, c2server))] + [
            asyncio.create_task(try_code(session, semaphore, c2server, code)) for code in codes] + [
                    asyncio.create_task(try_measure(session, semaphore, c2server, measure)) for measure in
                    ['d0_n0thing', 'c0ugh_th3_3ld3rly_1n_d4_f4c3']]
        results = await asyncio.gather(*tasks)
        for result in results:
            try:
                body = json.loads(result)
                if 'piece' in body:
                    output = 'Looking for measures against COVID-19...'
                elif 'message' in body:
                    output = body['message']
                print(output)
            except json.decoder.JSONDecodeError:
                continue
    elapsed = time.perf_counter() - start
    print(f"Time taken: {elapsed:0.2f} seconds")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

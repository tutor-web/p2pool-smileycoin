from p2pool.bitcoin import networks

PARENT = networks.nets['smileycoinSha256']
SHARE_PERIOD = 180 # seconds target spacing, 1/5 of the block period
CHAIN_LENGTH = 24*60*60//10
REAL_CHAIN_LENGTH = 24*60*60//10
TARGET_LOOKBEHIND = 200 
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c69231cd'.decode('hex')
PREFIX = '7208c1a53ef621cd'.decode('hex')
P2P_PORT = 11720
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 11730
BOOTSTRAP_ADDRS = 'smileyco.in 130.208.71.203'.split(' ')
ANNOUNCE_CHANNEL = ''
VERSION_CHECK=lambda v: True
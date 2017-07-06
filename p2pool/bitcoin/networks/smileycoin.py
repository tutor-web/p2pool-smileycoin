import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 11337
ADDRESS_VERSION = 25
RPC_PORT = 14242
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
'smileycoinaddress' in (yield bitcoind.rpc_help())
))
SUBSIDY_FUNC=lambda height: 10000*100000000 >> (height + 1)//1226400
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 180
SYMBOL = 'SMLY'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'smileycoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/smileycoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.smileycoin'), 'smileycoin.conf')
BLOCK_EXPLORER_URL_PREFIX='http://blockexplorer.smileycoin.eu/block/'
ADDRESS_EXPLORER_URL_PREFIX='https://bitinfocharts.com/smileycoin/address/'
TX_EXPLORER_URL_PREFIX='http://blockexplorer.smileycoin.eu/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8

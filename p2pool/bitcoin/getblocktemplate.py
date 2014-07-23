import random
import sys

from twisted.internet import protocol, reactor
from twisted.python import log

from p2pool.bitcoin import data as bitcoin_data, getwork
from p2pool.util import expiring_dict, jsonrpc, pack


class StratumRPCMiningProvider(object):
    def __init__(self, wb, other, transport):
        self.wb = wb
        self.other = other
        self.transport = transport
        
        self.username = None
        self.handler_map = expiring_dict.ExpiringDict(300)
        
        self.watch_id = self.wb.new_work_event.watch(self._send_work)
    
    def rpc_subscribe(self, miner_version=None, session_id=None):
        reactor.callLater(0, self._send_work)
        
        return [
            ["mining.notify", "ae6812eb4cd7735a302a8a9dd95cf71f"], # subscription details
            "", # extranonce1
            self.wb.COINBASE_NONCE_LENGTH, # extranonce2_size
        ]
    
    def rpc_authorize(self, username, password):
        self.username = username
        
        reactor.callLater(0, self._send_work)
    
    def _send_work(self):

    
    def rpc_submit(self, worker_name, job_id, extranonce2, ntime, nonce):

        return got_response(header, worker_name, coinb_nonce)
    
    def close(self):
        self.wb.new_work_event.unwatch(self.watch_id)

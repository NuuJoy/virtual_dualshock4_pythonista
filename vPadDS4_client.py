

import time
import json
from nuuJoyLib.Pythonista.touchpad import touchGamePad
from nuuJoyLib.Socket.tcpipv4 import client_socket


__version__ = (2021,2,9,'beta')


class socketjsonput():
    class fake_client():
        def send_msgs(self,*args,**kwargs):
            pass
    def __init__(self,client=None):
        self.client = self.fake_client() if client is None else client
    def send_event(self,action,state):
        msgstext = json.dumps({**{'action':action},**state})
        self.client.send_msgs(msgstext.encode())
        

if __name__ == '__main__':

    scktjson = socketjsonput()

    ds4pad = touchGamePad('ds4')

    ds4pad.override_extfunc('dpad_y_up','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('dpad_y_up','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('dpad_y_down','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('dpad_y_down','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('dpad_x_left','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('dpad_x_left','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('dpad_x_right','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('dpad_x_right','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_cross','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_cross','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_circle','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_circle','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_square','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_square','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_triangle','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_triangle','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_l1','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_l1','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_l2','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_l2','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_r1','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_r1','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_r2','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_r2','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_option','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_option','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_ps','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_ps','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_share','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('button_share','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('left_analog','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('left_analog','touchmoved_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('left_analog','touchended_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('right_analog','touchbegan_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('right_analog','touchmoved_extfunc',scktjson.send_event)
    ds4pad.override_extfunc('right_analog','touchended_extfunc',scktjson.send_event)

    ds4pad.run()

    for retry in range(5):
        if not(ds4pad.stop_event.is_set()):
            print('connecting to server ... (retry: {})'.format(retry))
            try:
                with client_socket('172.20.10.9',13666) as client:
                    scktjson.client = client
                    while client.conn_status() and not(ds4pad.stop_event.is_set()):
                        time.sleep(1.0)
                    scktjson.client = socketjsonput.fake_client()
            except:
                pass
            time.sleep(1.0)
            
    print('terminate.')


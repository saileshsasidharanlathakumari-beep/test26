from neurapy.apps import App
from neura_gui_data_parser.converters import parse_dict_data

from typing import Dict
import test26Dependencies
from test26Payload import test26Payload


#Here you can add your imports, Please make sure you add them in requirements.txt and provide a compatible version with your robot

class test26(App):
    def __init__(self, robot):
        self.robot = robot
        raise NotImplementedError(f"Constructor of test26 not implemented")
        
    def init(self, payload: Dict) -> None:
        self.payload = payload
        self.local_payload: test26Payload = parse_dict_data(self.payload, test26Payload)

    def run(self) -> None:
        # Please implement the logic for executing the node here
        raise NotImplementedError(f"run of test26 not implemented")

    def finish(self):
        raise NotImplementedError(f"Finish of test26 not implemented")

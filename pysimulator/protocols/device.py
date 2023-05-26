from typing import List
from pysimulator.protocols.runtime import RunTime
from pysimulator.exec import Executor

from pysimulator.protocols.list_types import CMD, ListTypes


class Device:
    def __init__(self,
                 name,
                 state,
                 udid,
                 device_type_indentifier,
                 device_type,
                 is_available,
                 log_path,
                 data_path) -> None:
        self.name = name
        self.state = state
        self.udid = udid
        self.device_type_indentifier = device_type_indentifier
        self.device_type = device_type
        self.is_available = is_available
        self.log_path = log_path
        self.data_path = data_path


class DeviceList(List[Device]):

    def filter(self, name=None, udid=None) -> 'DeviceList':
        filter_devices = DeviceList()
        for device in self[:]:
            if name and name in device.name:
                filter_devices.append(device)
            if udid and udid in device.udid:
                filter_devices.append(device)
        return filter_devices

    def first(self) -> 'Device':
        return self[:][0]

    @staticmethod
    def list_devices() -> 'DeviceList':
        device_list = DeviceList()
        for device_type, device_item_list in Executor.shell(CMD.format(ListTypes.DEVICES) + ' --json').safe_json_stdout_data().get(ListTypes.DEVICES).items():
            for device_item in device_item_list:
                device_list.append(Device(name=device_item.get('name'),
                                          state=device_item.get('state'),
                                          udid=device_item.get('udid'),
                                          device_type_indentifier=device_item.get('device_type_indentifier'),
                                          device_type=device_item.get('device_type'),
                                          is_available=device_item.get('is_available'),
                                          log_path=device_item.get('log_path'),
                                          data_path=device_item.get('data_path')
                                          ))
        return device_list

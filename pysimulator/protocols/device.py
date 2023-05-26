from typing import List


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

    def filter(self, name) -> 'DeviceList':
        filter_devices = DeviceList()
        for device in self[:]:
            if device.name == name:
                filter_devices.append(device)
        return filter_devices
    
    def first(self) -> 'Device':
        return self[:][0]

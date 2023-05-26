from typing import List
from pysimulator.exec import Executor
from pysimulator.protocols.list_types import CMD, ListTypes


class DeviceType:
    def __init__(self,
                 mini_runtime_version,
                 max_runtime_version,
                 bundle_path,
                 name,
                 identifier,
                 product_family
                 ) -> None:
        self.name = name
        self.mini_runtime_version = mini_runtime_version
        self.max_runtime_version = max_runtime_version
        self.bundle_path = bundle_path
        self.identifier = identifier
        self.product_family = product_family


class DeviceTypeList(List[DeviceType]):

    def filter(self, name) -> 'DeviceTypeList':
        filter_devicetypes = DeviceTypeList()
        for devicetype in self[:]:
            if name in devicetype.name:
                filter_devicetypes.append(devicetype)
        return filter_devicetypes

    def first(self) -> 'DeviceType':
        return self[:][0]

    @staticmethod
    def list_device_types() -> 'DeviceTypeList':
        device_types_list = DeviceTypeList()
        for device_type in Executor.shell(CMD.format(ListTypes.DEVICE_TYPES) + ' --json').safe_json_stdout_data().get(ListTypes.DEVICE_TYPES):
            device_types_list.append(DeviceType(max_runtime_version=device_type.get('max_runtime_version'),
                                                mini_runtime_version=device_type.get('mini_runtime_version'),
                                                name=device_type.get('name'),
                                                bundle_path=device_type.get('bundle_path'),
                                                identifier=device_type.get('identifier'),
                                                product_family=device_type.get('product_family'),
                                                ))
        return device_types_list

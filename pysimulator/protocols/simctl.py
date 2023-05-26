'''List Command.'''
from enum import Enum
from pysimulator.exec import Executor
from pysimulator.protocols.runtime import RunTimeList, RunTime
from pysimulator.protocols.device import DeviceList, Device
from pysimulator.protocols.device_type import DeviceTypeList, DeviceType
from pysimulator.protocols.list_types import CMD, ListTypes



class Simctl:
    def __init__(self) -> None:
        ...

    def __str__(self) -> str:
        return Executor.shell(CMD.format('--help'))

    @staticmethod
    def list(list_type: ListTypes) -> str:
        return Executor.shell(CMD.format(ListTypes))

    @staticmethod
    def list_runtimes() -> RunTimeList:
        return RunTimeList.list_runtimes()

    @staticmethod
    def list_devices() -> DeviceList:
        return DeviceList.list_devices()

    @staticmethod
    def list_devicetypes() -> DeviceTypeList:
        return DeviceTypeList.list_device_types()

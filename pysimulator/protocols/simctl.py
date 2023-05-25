'''List Command.'''
from enum import Enum
from pysimulator.exec import Executor
from pysimulator.protocols.runtime import RunTimeList, RunTime


class ListTypes:
    '''Usage: simctl list [-j | --json] [-v] [devices|devicetypes|runtimes|pairs] [<search term>|available]'''
    DEVICE = 'device'
    DEVICE_TYPES = 'devicetypes'
    RUNTIMES = 'runtimes'
    PAIRS = 'pairs'


CMD = 'xcrun simctl list {0}'


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
        return [
            RunTime(bundle_path=runtime_item.get('bundlePath'),
                    bundle_version=runtime_item.get('bundleversion'),
                    runtime_root=runtime_item.get('runtimeRoot'),
                    identifier=runtime_item.get('identifier'),
                    version=runtime_item.get('version'),
                    is_available=runtime_item.get('isAvailable'),
                    name=runtime_item.get('name')
                    )
            for runtime_item in Executor.shell(CMD.format(ListTypes.RUNTIMES) + ' --json').safe_json_stdout_data().get('runtimes')
        ]
    
    @staticmethod
    def list_devices() -> RunTimeList:
        return [
            RunTime(bundle_path=runtime_item.get('bundlePath'),
                    bundle_version=runtime_item.get('bundleversion'),
                    runtime_root=runtime_item.get('runtimeRoot'),
                    identifier=runtime_item.get('identifier'),
                    version=runtime_item.get('version'),
                    is_available=runtime_item.get('isAvailable'),
                    name=runtime_item.get('name')
                    )
            for runtime_item in Executor.shell(CMD.format(ListTypes.RUNTIMES) + ' --json').safe_json_stdout_data().get('runtimes')
        ]

'''Runtime Modle.'''
from typing import List
from pysimulator.exec import Executor
from pysimulator.protocols.list_types import CMD, ListTypes


class RunTime:
    def __init__(self,
                 bundle_path,
                 bundle_version,
                 runtime_root,
                 identifier,
                 version,
                 is_available,
                 name) -> None:
        self.bundle_path = bundle_path
        self.bundle_version = bundle_version
        self.runtime_root = runtime_root
        self.identifier = identifier
        self.version = version
        self.is_available = is_available
        self.name = name


class RunTimeList(List[RunTime]):

    def filter(self, name) -> 'RunTimeList':
        filter_runtimes = RunTimeList()
        for runtime in self[:]:
            if name in runtime.name:
                filter_runtimes.append(runtime)
        return filter_runtimes

    def first(self) -> 'RunTime':
        return self[:][0]

    @staticmethod
    def list_runtimes() -> 'RunTimeList':
        runtime_list = RunTimeList()
        for runtime_item in Executor.shell(CMD.format(ListTypes.RUNTIMES) + ' --json').safe_json_stdout_data().get(ListTypes.RUNTIMES):
            runtime_list.append(RunTime(bundle_path=runtime_item.get('bundlePath'),
                                        bundle_version=runtime_item.get('bundleversion'),
                                        runtime_root=runtime_item.get('runtimeRoot'),
                                        identifier=runtime_item.get('identifier'),
                                        version=runtime_item.get('version'),
                                        is_available=runtime_item.get('isAvailable'),
                                        name=runtime_item.get('name')
                                        ))
        return runtime_list

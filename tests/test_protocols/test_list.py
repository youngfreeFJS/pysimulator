from pysimulator.protocols.commands.list import List
from pysimulator.protocols.runtime import RunTime, RunTimeList


def test_list_cmd():
    runtime_list = List.runtimes_list()
    for runtime in runtime_list:
        assert isinstance(runtime, RunTime)
        assert runtime.name != None

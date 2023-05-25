from pysimulator.protocols.simctl import Simctl, ListTypes
from pysimulator.protocols.runtime import RunTime, RunTimeList


def test_list_cmd():
    runtime_list = Simctl.list_runtimes()
    for runtime in runtime_list:
        assert isinstance(runtime, RunTime)
        assert runtime.name != None

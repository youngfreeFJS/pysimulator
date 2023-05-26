from pysimulator.protocols.simctl import Simctl, ListTypes
from pysimulator.protocols.runtime import RunTime, RunTimeList
from pysimulator.protocols.device import Device, DeviceList


def test_runtime_list():
    runtime_list = Simctl.list_runtimes()
    for runtime in runtime_list:
        assert isinstance(runtime, RunTime)
        assert runtime.name != None


def test_device_list():
    device_list = Simctl.list_devices()
    for device in device_list:
        assert isinstance(device, Device)
        assert device.name != None
        assert len(device.udid) == 36

def test_device_list_filter():
    device_list = Simctl.list_devices()
    devices_filter = device_list.filter('myios135a')
    assert len(devices_filter) == 1


def test_device_list_first():
    device_list = Simctl.list_devices()
    device = device_list.filter('myios135a').first()
    assert device.name == 'myios135a'
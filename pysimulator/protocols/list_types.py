
class ListTypes:
    '''Usage: simctl list [-j | --json] [-v] [devices|devicetypes|runtimes|pairs] [<search term>|available]'''
    DEVICES = 'devices'
    DEVICE_TYPES = 'devicetypes'
    RUNTIMES = 'runtimes'
    PAIRS = 'pairs'


CMD = 'xcrun simctl list {0}'

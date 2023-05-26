import json
from subprocess import Popen, PIPE, SubprocessError

class SimulatorErr(Exception):
    ...

class PopenReturns:
    def __init__(self, p_open: Popen) -> None:
        self.p_open = p_open
    
    def safe_json_stdout_data(self):
        try:
            return json.loads(self.p_open.stdout_data)
        except json.decoder.JSONDecodeError:
            return self.p_open.stdout_data

class Executor:

    @staticmethod
    def shell(command: str, cwd: str = None, env: dict = None, timeout_sec: int = 60, print_stdout: bool = False):
        '''func is extend subporcess.Popen func.
        Is a tool method for create and manage subprocess.
        The custom parameters are added to the Popen object returns, such as whether 
        successful or not, subprocess environment variables, etc.
        '''

        # pylint: disable=consider-using-with
        sub_proc = Popen(command, shell=True, stdout=PIPE, stderr=PIPE, env=env, cwd=cwd, encoding='utf-8')

        # Print Stdout In Realtime instead of End of Process Run.
        if print_stdout:
            while sub_proc.poll() is None:
                print(sub_proc.stdout.readline().strip())

        # Fetch stdout and stderr from Popen.communicate funcs instead of Popen.stdout and Popen.stderr.
        # If not will deadlock when using stdout=PIPE or stderr=PIPE and the child process generates enough
        # output to a pipe such that it blocks waiting for the OS pipe buffer to accept more data.
        try:
            sub_proc.stdout_data, sub_proc.stderr_data = sub_proc.communicate(timeout=timeout_sec)
        except SubprocessError:
            sub_proc.kill()
            sub_proc.stdout_data, sub_proc.stderr_data = sub_proc.communicate()

        # Add variable `success` to func returns object.
        sub_proc.success = sub_proc.returncode == 0

        if not sub_proc.success:
            raise SimulatorErr(f'Original Error: {sub_proc.stderr_data}')

        return PopenReturns(sub_proc)

import threading
import time

from tilt_dev.python_client.api_client import ApiClient

class TiltChecker(threading.Thread):
    def __init__(self, starting_seconds=0, is_running=True, active=True):
        self.starting_seconds = starting_seconds
        self.is_running = is_running
        self.active = active

        self.start_time = None
        self.time_passed = None

        super().__init__(daemon=True)

    def run(self):
        self.start_time = time.time()
        self.time_passed = self.starting_seconds

        while self.active:
            if self.is_running:
                self.time_passed = (self.starting_seconds
                                    + int(time.time() - self.start_time))

            time.sleep(0.5)

    def is_div5(self):
        _, seconds = divmod(self.time_passed, 60)
        return seconds % 5 == 0


if __name__ == "__main__":
    print('hello worldddd')
    cli = ApiClient()
    cli.rest_client

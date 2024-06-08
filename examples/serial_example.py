import sys

from colour import Color
from loguru import logger

from wled_adapter.adapter import Adapter
from wled_adapter.connection import SerialConnection
from wled_adapter.state import Seg, State


class Tester:
    def __init__(self, port: str):
        self._adapter = Adapter(SerialConnection(port, 115200))

    def run(self):

        # for segment in range(3):

        config = State(
            seg=[
                Seg(
                    id=0,
                    start=0,
                    stop=6,
                    grp=1,
                    on=True,
                    bri=32,
                    fx=0,
                    col=[[255, 0, 0], [0, 0, 0], [0, 0, 0]],
                ),
            ]
        )
        self._adapter.send_state(config)

        self._adapter.initialise_segments()
        segment = 0
        iterations = 254

        for pixel in range(4):
            for col in range(iterations):
                colour = col / iterations
                self._adapter.segments[segment]._set_pixel(
                    pixel, Color("blue", luminance=1 - colour)
                )
                self._adapter.segments[segment]._set_pixel(
                    pixel + 1, Color("purple", luminance=colour)
                )
                self._adapter.segments[segment]._set_pixel(
                    pixel + 2, Color("green", luminance=1 - colour)
                )
                self._adapter.update_segment(segment)


def main(argv: list):
    regexp = ".*USB.*"
    # regexp = ".*"
    ports = list(SerialConnection.available_ports(regexp))
    ports = [port.device for port in ports]
    logger.info(f"Available ports: \n{ports}")
    if len(argv) < 2:
        port = ports[0]
    else:
        port = argv[1]

    tester = Tester(port)
    tester.run()


if __name__ == "__main__":
    main(sys.argv)

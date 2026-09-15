import pyControl.hardware as _h


class Hex_port():
    # Single capacitive lick sensor (SparkFun AT42QT1011) + one Lee solenoid valve
    # (LHQA2431220H, run at +12V) on a single pyControl behaviour port.
    #
    # Wiring (via pyControl Port Adapter):
    #   cap sensor VDD  -> port adapter +5V
    #   cap sensor GND  -> port adapter GND
    #   cap sensor OUT  -> port adapter DIO_A
    #   cap sensor PAD  -> lick tube (tube is the sense electrode)
    #   solenoid        -> POW_A / +12V driver header
    def __init__(self, port, rising_event=None, falling_event=None):
        self.cap_sensor = _h.Digital_input(port.DIO_A, rising_event, falling_event)
        self.SOL = _h.Digital_output(port.POW_A)

    def value(self):
        return self.cap_sensor.value()

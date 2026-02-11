import Adafruit_BBIO.GPIO as GPIO
import time

class RelayControl:
    """
    Handles hardware relay control for the EVSE power path.
    """
    def __init__(self, pin="P8_17"):
        self.pin = pin
        self.is_initialized = False
        self._setup()

    def _setup(self):
        try:
            GPIO.setup(self.pin, GPIO.OUT)
            # Default to LOW for safety
            GPIO.output(self.pin, GPIO.LOW)
            self.is_initialized = True
            print(f"Relay initialized on {self.pin}")
        except Exception as e:
            print(f"GPIO Setup Error: {e}")

    def turn_on(self):
        """Sets pin to HIGH (3.3V)"""
        if self.is_initialized:
            print(f"SET HIGH (3.3V) - Relay Closed")
            GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        """Sets pin to LOW (0V)"""
        if self.is_initialized:
            print(f"SET LOW (0V) - Relay Open")
            GPIO.output(self.pin, GPIO.LOW)

    def cleanup(self):
        """Releases the GPIO pin"""
        self.turn_off()
        GPIO.cleanup()
        print("GPIO Cleaned up")

if __name__ == "__main__":
    relay = RelayController("P8_17")
    
    try:
        relay.turn_off()
        time.sleep(2)

        relay.turn_on()
        time.sleep(2)

        relay.turn_off()
        
    finally:
        relay.cleanup()
        print("DONE")

from OmegaExpansion import pwmExp

class OmegaPwm:
    """Base class for PWM signal"""

    def __init__(self, channel, frequency=50):
        self.channel     = channel
        self.frequency     = frequency

        # check that pwm-exp has been initialized
        bInit     = pwmExp.checkInit()

        if (bInit == 0):
            # initialize the Expansion
            ret     = pwmExp.driverInit()
            if (ret != 0):
                print 'ERROR: pwm-exp init not successful!'

            # set to default frequency
            self._setFrequency(self.frequency)

    def _setFrequency(self, freq):
        """Set frequency of pwm-exp oscillator"""
        self.frequency     = freq
        ret     = pwmExp.setFrequency(freq);
		if (ret != 0):
            print 'ERROR: pwm-exp setFrequency not successful!'

        return ret

    def getFrequency(self):
        """Get frequency of pwm-exp oscillator"""
        return self.frequency

    def setDutyCycle(self, duty):
        """Set duty cycle for pwm channel"""
        ret     = pwmExp.setupDriver(self.channel, duty, 0)
        if (ret != 0):
			print 'ERROR: pwm-exp setupDriver not successful!'

        return ret

################################################################################
# define the minimum and maximum pulse widths that will suit most servos (in us)
SERVO_MIN_PULSE = 1000
SERVO_MAX_PULSE = 2000

# Servo motor
class Servo:
    """Class that uses PWM signals to drive a servo"""
	
    def __init__(self, channel, minPulse=SERVO_MIN_PULSE, maxPulse=SERVO_MAX_PULSE):
        # initialize a pwm channel
        self.channel = channel
        self.frequency = 50
        self.pwmDriver = OmegaPwm(self.channel, self.frequency)

        # note the min and max pulses (in microseconds)
        self.minPulse = minPulse
        self.maxPulse = maxPulse

        # calculate the total range
        self.range = self.maxPulse - self.minPulse		
		
		
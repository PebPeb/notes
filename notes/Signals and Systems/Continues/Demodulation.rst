============
Demodulation
============

Carrier Wave 
- Is a waveform modulated with an information bearing signal
- The Carrier signal has a much higher frequency because it is impractical to transmit lower frequency signals

There are different ways to demodulated depending on the base-band signal paramaters such as amplitude, frequency or phase. 

----------------
Decibels and dbm
----------------

Decibels are dimensionless numbers used to represent the ratio of two quantities of power 

	| :math:`db = 10log(P_1 / P_0)`

For dbm the refrence power is a static :math:`P_0 = 1mW`

	| :math:`dbm = 10log(P / 1mw)`

--------------------
Frequency Modulation
--------------------

**Frequency Modulation** (FM)
- Is the encoding of information in a carrier wave by varying the instantaneous frequency of the wave

	| :math:`x_m (t)` = *Baseband Signal*
	| :math:`x_c (t)` = *Sinusoidal Carrier*
	| :math:`f_c` = *Carrier's Base Frequency*
 	| :math:`A_c` = *Carrier Amplitude*
 	

.. math::
   
   x_c(t)=A_c cos(2\pi f_c t)

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Fast Fourier Transform (FFT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For frequency demodulation we can use a FFT. A FFT converts a signal into individual spectral compents that thereby provide frequency information about the signal. This is basically breaking the signal down into a Fourier series. The FFT is much faster than the Discrete Fourier Transform and this is why we use this with digital signal processing.

--------------------
Amplitude Modulation
--------------------

^^^^^^^^^^^^^^^^^^
Envelope detection
^^^^^^^^^^^^^^^^^^

For amplitude demodulation we can use what is known as a envelope detector. Sometimes known as a peak detector is typically implemented with a lowpass filter to create the envelope shape.



----------------
Phase Modulation
----------------



^^^^^^^^^^^^^^^^^^^^^^^
Phase-Locked Loop (PLL)
^^^^^^^^^^^^^^^^^^^^^^^





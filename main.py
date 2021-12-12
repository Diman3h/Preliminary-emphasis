import numpy as np
import wave
import matplotlib.pyplot as plt
f = wave.open(r"adx.wav", "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = f.readframes(nframes)
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data = wave_data*1.0/(max(abs(wave_data)))
plt.specgram(wave_data,Fs = framerate, scale_by_freq = True, sides = 'default')
plt.show()

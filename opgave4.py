from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

title_index = html.find("<title>")

start_index = title_index + len("<title>")

end_index = html.find("</title>")

title = html[start_index:end_index]



# Now for the 2nd website

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title >") + len("<title >") #fixed for the extra space in the html tag
end_index = html.find("</title>")
title = html[start_index:end_index]



import re

match_results = re.search("ab*c", "ABC", re.IGNORECASE)

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)



import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags




from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

image1, image2 = soup.find_all("img")

import mechanicalsoup
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)



links = profiles_page.soup.select("a")

'''
for link in links:
    address = link["href"]
    text = link.text
    print(f"{text}: {address}")
'''

'''
base_url = "http://olympus.realpython.org"
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")
'''


browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
result = tag.text

import time

browser = mechanicalsoup.Browser()

'''
for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    time.sleep(10)


for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")

    # Wait 10 seconds if this isn't the last request
    if i < 3:
        time.sleep(10)
'''




import sounddevice as sd
from scipy.io import wavfile

def play_wave_file(filename):
    try:
        # Load the file
        samplerate, data = wavfile.read(filename)
        
        # Play the audio
        sd.play(data, samplerate)
        
        # Wait until the audio has finished playing
        sd.wait()
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = r"C:\Users\Victor Steinrud\Downloads\stoopd.wav"
# play_wave_file(filename)



import numpy as np

def generate_and_play_sound(frequency=440, fs=44100, seconds=3):
    t = np.linspace(0, seconds, fs * seconds, False)

    note = np.sin(frequency * t * 2 * np.pi)

    audio = note * (2**15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)

    sd.play(audio, fs)
    sd.wait()

# generate_and_play_sound()


import winsound

filename = r"C:\Users\Victor Steinrud\Downloads\stoopd.wav"
# winsound.PlaySound(filename, winsound.SND_FILENAME)


import pyaudio
import wave

filename = r"C:\Users\Victor Steinrud\Downloads\stoopd.wav"
'''
# Set chunk size of 1024 samples per data frame
chunk = 1024  

# Open the sound file 
wf = wave.open(filename, 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# Read data in chunks
data = wf.readframes(chunk)

# Play the sound by writing the audio data to the stream
while data != '':
    stream.write(data)
    data = wf.readframes(chunk)

# Close and terminate the stream
stream.close()
p.terminate()
'''

'''
import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file 
'''
'''

import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()



import soundfile as sf

# Extract audio data and sampling rate from file 
data, fs = sf.read(r"C:\Users\Victor Steinrud\Downloads\stoopd.wav") 
# Save as FLAC file at correct sampling rate
sf.write('myfile.flac', data, fs)  
'''


from pydub import AudioSegment
sound = AudioSegment.from_wav("C:\\Users\\Victor Steinrud\\Downloads\\stoopd.wav")

sound.export('myfile.mp3', format='mp3')
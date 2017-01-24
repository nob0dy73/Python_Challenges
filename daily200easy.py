import wave, struct, math

notes = [261.626, 293.665, 329.628, 349.228, 391.995, 440.000, 493.883,
     523.251,
     498.883, 440.000, 391.995, 349,228, 329.628, 293.665, 261.626]

def create(notes, sample_rate, duration, file):

    noise_file = wave.open(file, 'w')
    noise_file.setnchannels(1)
    noise_file.setsampwidth(2)
    noise_file.setframerate(sample_rate)

    for index, note in enumerate(notes):
        samples_per_note = duration * sample_rate // len(notes)
        first_sample = samples_per_note * index
        last_sample = first_sample + samples_per_note

        for i in range(first_sample, last_sample):
            value = int(32767.0 * math.cos(note * math.pi * float(i) / float(sample_rate)))
            data = struct.pack('<h', value)
            noise_file.writeframesraw(data)
    noise_file.close()

create(notes, 44100, 10, 'audio.wav')

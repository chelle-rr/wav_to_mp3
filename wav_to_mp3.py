import os
import csv
import re
import ffmpeg

paths_to_search = []
with open('test_no_wav.csv', 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        paths_to_search.append(line[0].strip())
	
#wav_pattern = \.[w|W][a|A][v|V]

wav_list = []
for each_path in paths_to_search:
    # wav_find = wav_pattern.findall(each_path)
    for dirpath, dirnames, filenames in os.walk(each_path):
        for filename in [f for f in filenames if f.lower().endswith(".wav")]:
            wavpath = os.path.join(dirpath, filename)
            wav_list.append(wavpath)

f = open("wav_to_mp3_results.txt", "x")

success_count = 0
fail_count = 0

for each_wav in wav_list:
    no_ext = each_wav[:-3]
    output = no_ext + "mp3"
    if os.path.exists(output):
        print("mp3 already exists at ", output)
    if not os.path.exists(output):
        (
            ffmpeg
            .input(each_wav)
            .output(output)
            .run()
        )
    if os.path.exists(output):
        f.write("Successfully created mp3 at " + output)
        success_count = success_count + 1

    else:
        f.write("Failed to create mp3 at " + each_wav)

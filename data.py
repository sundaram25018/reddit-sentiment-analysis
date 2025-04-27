# create_nrc_file.py
sample_lexicon = [
    ("happy", "joy"),
    ("sad", "sadness"),
    ("angry", "anger"),
    ("fearful", "fear"),
    ("surprised", "surprise"),
    ("trusting", "trust"),
    ("disgusted", "disgust"),
    ("anticipating", "anticipation"),
    ("love", "joy"),
    ("hate", "anger"),
    ("worry", "fear"),
    ("cry", "sadness"),
    ("smile", "joy"),
    ("laugh", "joy"),
    ("scream", "fear"),
    ("betray", "disgust"),
    ("hope", "anticipation"),
    ("death", "sadness"),
    ("success", "joy"),
    ("failure", "sadness"),
]

with open("nrc_emotion_lexicon.txt", "w") as f:
    for word, emotion in sample_lexicon:
        f.write(f"{word}\t{emotion}\t1\n")

print("✅ nrc_emotion_lexicon.txt created successfully!")

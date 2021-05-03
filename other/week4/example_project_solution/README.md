
# Lyrics Predictor

Sample solution

## Installation

Install required packages with:

    pip install -r requirements.txt

## Usage

### Step 1: Download artists

Download all songs for multiple artists with:

   python download_songs.py

And enter the artist names (with spaces, case insensitive).

The lyrics will be stored in a folder `songs/`

### Step 2: Train the model

Train a Naive Bayes classifier

    python train_model.py

It writes the model to a pickle file in the same folder.

**TODO: the model is not optimized, the focus of the example is on writing a clean pipeline**

### Step 3: Predict

Classify songs:

    python predict_artist.py

And enter your own lyrics.

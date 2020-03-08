# Python Instagram Story Stitcher (PISS)

This script will extract all your instagram video stories and stitch files that belongs together in a story into one file.

## Requirements

* Python 3
* ffmpeg

## Usage

1. Go to your Instagram account and request download of your Instagram data (https://www.instagram.com/download/request/)
2. Download the zipfile(s) when your download email arrives and unzip it.
3. Put the downloaded `media.json` file into the `json/` folder. If you downloaded more than one zipfile and have several `media.json` files just rename them e.g. `media1.json` and `media2.json` before putting them in the `json/` folder.
4. Put the content of the downloaded `stories/` directory/directories into the `stories/` folder. Your folder structure should look something like this:
```
├── json
│   ├── media1.json
│   └── media2.json
├── out
├── piss.py
├── README.md
└── stories
    ├── 201809
    │   ├── 03cec5e3cc60a43e026e8ed97e12baff.jpg
    │   ├── 17b460a57f5361deacee63eac8c7d103.jpg
    │   ├── 2476d112ba5136d9fd93d756ed471108.jpg
    │   ├── 284aa9c4101993ea6b9e879e5f220425.mp4
    │   ├── 38c266e2b28886dc7fdc5863cb3ae774.jpg
    │   ├── 6925cc194ec7dabf5d54046f9ab14592.jpg
    │   ├── 71d3dde1d2593333dab93d4fd37193f8.mp4
    │   ├── 88b090f69f301f0637985c2760cde962.jpg
    │   ├── a0bc2577fd370adf9dd441d91bf75ac8.mp4
    │   └── f57ab66c7a43a59ee4e07c98ad7e4561.jpg
    ├── 201811
    ├── 201904
    ├── 201905
    ├── 201906
    ├── 201907
    ├── 201908
    ├── 201909
    ├── 201910
    ├── 201911
    ├── 201912
    ├── 202001
    └── 202002

```
5. Run `python3 piss.py` to generate video stories.
6. Stories are generated inside the `out/` folder.

## But why?

The maximum length of a video on your story is 15 seconds. You can have as many videos as you want in a row to generate a longer story, but there is no way to download the complete story from Instagram. You would need to download all 15 second videos and manually stitch them together. This script will automate that job for you and it will also rename the videofile to something more readable (the complete date and time of when your story was created).
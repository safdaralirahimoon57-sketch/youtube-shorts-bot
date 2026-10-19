#!/usr/bin/env python3
"""Bawaal Beasts — funny Hindi/Urdu animal Short starter."""

import json
import os
import random
from pathlib import Path

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

STORIES = [
    {
        "title": "Sher Bana Food Vlogger 😂",
        "scenes": [
            {
                "visual": "A funny 3D cartoon lion holding a tiny camera in a jungle",
                "dialogue": "Assalam-o-alaikum dosto! Aaj sher bhai ka food review hai!"
            },
            {
                "visual": "A funny 3D cartoon monkey steals the lion's lunch",
                "dialogue": "Aray bandar! Mera khana kahan gaya? Yeh kya badtameezi hai!"
            },
            {
                "visual": "The monkey eats the food while the lion looks shocked",
                "dialogue": "Review zabardast tha, lekin khana bandar kha gaya! 😂"
            }
        ]
    },
    {
        "title": "Bandar Ka Fake Interview 😂",
        "scenes": [
            {
                "visual": "A funny 3D cartoon monkey holding a microphone in a jungle",
                "dialogue": "Aaj hum jungle ke sab se ameer janwar ka interview lenge!"
            },
            {
                "visual": "A funny 3D cartoon elephant proudly shows an empty wallet",
                "dialogue": "Mere paas bohat bara wallet hai, bas paisay chhutti par hain!"
            },
            {
                "visual": "The monkey and elephant laugh together",
                "dialogue": "Jungle mein bhi salary ka intezar khatam nahi hota! 😂"
            }
        ]
    }
]


def main():
    story = random.choice(STORIES)
    output_file = OUTPUT_DIR / "story.json"

    result = {
        "channel": "Bawaal Beasts",
        "language": "Hindi + Urdu mix",
        "format": "YouTube Short",
        "title": story["title"],
        "description": (
            "Bawaal Beasts par dekhein funny animal stories! "
            "#Shorts #BawaalBeasts #FunnyAnimals #Cartoon"
        ),
        "scenes": story["scenes"]
    }

    output_file.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print("Bawaal Beasts story created successfully!")
    print(f"Title: {result['title']}")
    print(f"Story file: {output_file}")
    print("Scenes:", len(result["scenes"]))


if __name__ == "__main__":
    main()

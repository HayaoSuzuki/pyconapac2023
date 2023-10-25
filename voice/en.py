import asyncio

import edge_tts

with open("script_en.txt") as f:
    TEXT = f.read()


VOICE = "en-US-AriaNeural"
RATE = "-15%"
OUTPUT_FILE = "talk_en.mp3"
WEBVTT_FILE = "talk_en.vtt"


async def amain() -> None:
    """Main function"""
    communicate = edge_tts.Communicate(TEXT, VOICE, rate=RATE)
    submaker = edge_tts.SubMaker()
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])

    with open(WEBVTT_FILE, "w", encoding="utf-8") as file:
        file.write(submaker.generate_subs())


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(amain())
    finally:
        loop.close()

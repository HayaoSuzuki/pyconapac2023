import asyncio

import edge_tts

with open("script_en.txt") as f:
    text = f.read()


async def main() -> None:
    communicate = edge_tts.Communicate(text, "en-US-AriaNeural", rate="-15%")
    with open("talk_en.mp3", "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

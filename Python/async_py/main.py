import asyncio


def main() -> None:
    """Our normal, synchronous starting point for our programs."""

    async def say_hello() -> None:
        await asyncio.sleep(1)
        print("Hello")

    asyncio.run(say_hello())


if __name__ == "__main__":
    main()

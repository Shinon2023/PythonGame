# main.py
import asyncio
from prisma import Prisma

# Define the main asynchronous function
async def run():
    # Create a Prisma client instance
    prisma = Prisma()

    # Connect to the database
    await prisma.connect()

    # Create a new record (for example, a user)
    user = await prisma.user.create(
        data={
            "name": "John Doe",
        }
    )

    # Fetch all records from the "user" table
    users = await prisma.user.find_many()
    for u in users:
        print(f"User: {u.name}, Email: {u.email}")

    # Disconnect from the database
    await prisma.disconnect()

# Run the asynchronous function using asyncio
if __name__ == '__main__':
    asyncio.run(run())

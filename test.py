from database.database import *
from database.models import *
import asyncio

print(asyncio.run(BeerService.read_all()))
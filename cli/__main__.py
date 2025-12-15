import argparse
from app.main import app
from app.utils.redis_client import r
import uvicorn

parser = argparse.ArgumentParser()

parser.add_argument("--port", help="Selects the port ",type=int)
parser.add_argument( "--origin", help="Selects the url api", type=str)
parser.add_argument("--clear-cache", action="store_true",help="Clear the cache")

args = parser.parse_args()

if args.clear_cache:
    r.flushdb()
    print("Current database has been flushed.")

else:
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port= args.port,
        reload=True
    )

import redis
import subprocess, time

def start_redis(port):

    print('Start Redis Server...')

    try:
        redis_command = ['redis-server', '--port', port]

        process = subprocess.Popen(redis_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text = True)
        print(f"Redis server started with PID {process.pid}")

        time.sleep(2)
        print("Attemping to connect to redis server with Python client...")

        r = redis.Redis(host= 'localhost', port=port, decode_responses = True)

        print(f"Connection successful.")

        print("\nRedir server is running. Press Enter to stop the server.")
        input()

    except FileNotFoundError:
        print("Error: 'redis-server' command not found.")
        print("Please ensure Redis is installed and available in your system's PATH.")
        process = None

    except redis.exceptions.ConnectionError:
            print("Error: Could not connect to the Redis server.")
            print("Check if the server started correctly and the port is available.")
            process = None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        process = None

    finally:
         if process:
                print("\nStopping Redis Server...")
                process.terminate()
                try:
                    process.wait(timeout = 5)
                    print("Redis server stoped.")
                except subprocess.TimeoutExpired:
                    print("Redis server did not terminate gracefully, killing process.")
                    process.kill()
                    print("Redis server killed.")

start_redis("6379")
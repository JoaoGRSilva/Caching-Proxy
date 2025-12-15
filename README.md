# 🚀 Caching Proxy Server (Python)

https://roadmap.sh/projects/caching-server

This project is a simple **caching proxy server** built with **Python**, **FastAPI**, and **Redis**.

The proxy forwards HTTP requests to an origin server, caches the responses, and serves cached data on subsequent requests, improving performance and reducing unnecessary external calls.

---

## 📌 Features

* HTTP proxy server
* Response caching using Redis
* Cache expiration (TTL)
* Cache status via response headers:

  * `X-Cache: HIT`
  * `X-Cache: MISS`
* CLI to start the proxy server
* CLI command to clear the cache

---

## 🛠 Tech Stack

* Python 3
* FastAPI
* Uvicorn
* Redis
* argparse

---

## 📁 Project Structure

```
Caching Proxy/
├── app/
│   ├── controllers/
│   │   └── proxy.py
│   ├── utils/
│   │   └── redis_client.py
│   └── main.py
│
├── cli/
│   └── __main__.py
│
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1️⃣ Start Redis

Make sure Redis is running locally:

```bash
redis-server
```

---

### 2️⃣ Start the Proxy Server

Run the CLI command:

```bash
python3 -m cli --port 3000 --origin http://dummyjson.com
```

The proxy server will start at:

```
http://localhost:3000
```

---

### 3️⃣ Make Requests

Example request:

```bash
curl -i http://localhost:3000/products
```

On the first request, the response will include:

```
X-Cache: MISS
```

On subsequent requests:

```
X-Cache: HIT
```

---

## 🧹 Clear Cache

To clear the Redis cache, run:

```bash
python3 -m cli --clear-cache
```

---

## 📖 How It Works

1. The CLI starts the FastAPI server using Uvicorn.
2. Incoming requests are forwarded to the origin server.
3. Responses are cached in Redis.
4. Cached responses are returned when available.
5. Each response includes a header indicating cache status.

---

## 🎯 Learning Goals

This project was built to practice and understand:

* How HTTP caching works
* How proxy servers forward requests
* Redis as a caching layer
* Building CLIs with argparse
* FastAPI + Uvicorn fundamentals

---

## 📌 Notes

* This project focuses on learning and simplicity.
* The origin URL is currently fixed for development purposes.
* Designed for educational and portfolio use.

---

## 📄 License

This project is open-source and free to use for learning purposes.

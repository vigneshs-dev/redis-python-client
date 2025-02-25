# Redis Python Client

This repository contains simple Python examples for interacting with Redis, a popular in-memory data structure store.

## Overview

The project demonstrates basic Redis operations using Python:
- Checking connection to Redis server (ping)
- Setting key-value pairs
- Retrieving values by key

## Files

- `redis_ping.py`: Tests connection to Redis server
- `redis_set.py`: Demonstrates setting values in Redis
- `redis_get.py`: Shows how to retrieve values from Redis

## Prerequisites

- Python 3.6+
- Redis server installed and running
- Virtual environment (recommended)

## Installation

### Installing Redis Server on Ubuntu

1. Update your package lists:
   ```
   sudo apt update
   ```

2. Install Redis server:
   ```
   sudo apt install redis-server
   ```

3. Verify the installation:
   ```
   redis-cli --version
   ```

### Managing Redis Service

Start Redis server:
```
sudo systemctl start redis-server
```

Check Redis server status:
```
sudo systemctl status redis-server
```

Stop Redis server:
```
sudo systemctl stop redis-server
```

Restart Redis server:
```
sudo systemctl restart redis-server
```

Enable Redis to start on boot:
```
sudo systemctl enable redis-server
```

### Setting up Python Project

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-name>
   ```

2. Set up a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate 
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Ensure your Redis server is running before executing these scripts.

### Testing Connection

```
python code/redis_ping.py
```

Expected output if successful:
```
True
```

### Setting Values

```
python code/redis_set.py
```

### Getting Values

```
python code/redis_get.py
```

Example:
```
Vicky
```

## Configuration

By default, the scripts connect to Redis running on localhost (127.0.0.1) at port 6379. To modify these settings, edit the connection parameters in each script.

## Dependencies

- redis: Python client for Redis
- hiredis: C library providing faster Redis protocol parsing

## License

MIT License

## Contributing

Feel free to submit issues or pull requests.
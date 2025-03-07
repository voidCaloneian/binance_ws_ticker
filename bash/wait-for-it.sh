#!/usr/bin/env bash

if [ "$#" -lt 3 ]; then
  echo "Usage: $0 <host> <port> <timeout> [--strict]" >&2
  exit 1
fi

host="$1"
port="$2"
timeout="$3"
strict="$4"

echo "Waiting for **${host}:${port}** to be available..."
start_time=$(date +%s)

while true; do
  if timeout 1 bash -c "cat < /dev/null > /dev/tcp/${host}/${port}" 2>/dev/null; then
    echo "**${host}:${port}** is available."
    break
  fi

  current_time=$(date +%s)
  elapsed=$(( current_time - start_time ))
  if [ "$elapsed" -ge "$timeout" ]; then
    echo "Timeout after ${timeout} seconds, **${host}:${port}** still unavailable." >&2
    if [ "$strict" = "--strict" ]; then
      exit 1
    fi
    break
  fi
  sleep 1
done

shift 4
exec "$@"
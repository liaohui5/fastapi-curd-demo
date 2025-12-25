alias d := dev
alias s := start

dev:
  uv run uvicorn main:app --reload

start:
  uv run uvicorn main:app --host 0.0.0.0 --port 8000

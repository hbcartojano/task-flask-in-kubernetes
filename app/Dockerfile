FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM gcr.io/distroless/python3
WORKDIR /app

COPY --from=builder /root/.local /usr

COPY . .

ENV PATH=/usr/lib:$PATH
ENV PYTHONPATH=/usr/lib/python3.11/site-packages
ENV FLASK_APP=main.py

USER nonroot
EXPOSE 5000
CMD ["-m", "flask", "run", "--host=0.0.0.0"]
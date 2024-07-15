FROM python:3.8-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# FROM gcr.io/distroless/python3
# WORKDIR /app
# COPY --from=builder /root/.local /root/.local
# COPY . .
# ENV PATH=/root/.local/bin:$PATH
# ENV PYTHONPATH=/app
# USER nonroot
# EXPOSE 8080
# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["tail", "-f", "/dev/null"]

# Calculator

Add, subtract and multiply two positive integers. Python 3.x, Docker, GitHub Actions CI.

## Run locally
    python -m unittest discover -s tests -v
    python -m calculator add 2 3

## Docker
    docker build -t calculator .
    docker run --rm calculator multiply 6 7
    docker run --rm --entrypoint python calculator -m unittest discover -s tests -v

## CI
`.github/workflows/ci.yml` builds the image and runs the tests inside it on every push.

"""Hello World HTTP service."""

from fastapi import FastAPI

from howto_release_please_python import __version__

app = FastAPI(title="howto-release-please-python", version=__version__)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World", "version": __version__}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

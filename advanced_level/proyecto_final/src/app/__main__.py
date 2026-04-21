import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",  # o "main:app" si no usas package app/
        host="0.0.0.0",
        port=8000,
        workers=4,
        reload=True,  # opcional en dev
    )

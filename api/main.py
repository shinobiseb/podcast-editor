from fastapi import FastAPI, File, UploadFile, HTTPException
from pathlib import Path
import tempfile

app = FastAPI(title="Podcast Editor API")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/uploadfile/")
async def create_file(file: UploadFile):
    content_type = file.content_type or ""

    if not content_type.startswith("audio/"):
        raise HTTPException(
            status_code=415,
            detail="Only audio files are allowed.",
        )

    contents = await file.read()
    original_file_name = file.filename or ""
    original_suffix = Path(original_file_name).suffix.lower()
    
    # REMEMBER TO DELETE AFTER PROCESSING
    with tempfile.NamedTemporaryFile(mode="wb", suffix=original_suffix, delete=False) as tf:
        written_bytes = tf.write(contents)
        return {
            "filename": file.filename,
            "content_type": content_type,
            "temporary path": tf.name,
            "size in bytes": written_bytes
        }
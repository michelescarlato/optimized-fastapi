# routes.py
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from .database import get_db
from .models import MyModel
from .storage import upload_file_to_blob
from .cache import get_cached_data, set_cached_data

router = APIRouter()

# Example: Get all items
@router.get("/items")
def get_items(db: Session = Depends(get_db)):
    # Attempt to get data from Redis cache
    cached_items = get_cached_data("items")
    if cached_items:
        return {"items": cached_items.decode("utf-8")}

    # If not cached, fetch from the database
    items = db.query(YourModel).all()
    if not items:
        raise HTTPException(status_code=404, detail="No items found")

    # Cache the result in Redis for faster access next time
    set_cached_data("items", str(items))
    return {"items": items}

# Example: Create a new item
@router.post("/items")
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    new_item = YourModel(name=name, description=description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"item": new_item}

# Example: Upload a file to Azure Blob Storage
@router.post("/upload")
def upload_file(file: UploadFile):
    try:
        # Save the file temporarily
        file_path = f"/tmp/{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        # Upload to Azure Blob Storage
        container_name = "your-container-name"  # Replace with your container name
        blob_name = file.filename
        upload_message = upload_file_to_blob(container_name, file_path, blob_name)
        return {"message": upload_message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Example: Get a single item by ID
@router.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(YourModel).filter(YourModel.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": item}

# Example: Delete an item by ID
@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(YourModel).filter(YourModel.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}

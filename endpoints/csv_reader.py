from fastapi import APIRouter, File, UploadFile
import csv
import io


router = APIRouter()


@router.post("/csv_to_json")
async def csv_to_json(file: UploadFile = File(...)):
    content = await file.read()
    decoded = content.decode("utf-8")
    csv_file = io.StringIO(decoded)
    reader = csv.DictReader(csv_file)

    result = []
    for row in reader:
        result.append(row)

    return {
        "data": result,
        "rows": len(result)
    }

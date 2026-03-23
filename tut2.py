from fastapi import FastAPI, Path, Query, HTTPException
import json

app = FastAPI()


# helper function to load json file

def load_data():
    with open("data/patients.json") as f:
        data = json.load(f)
        return data


@app.get("/")
def home() -> dict:
    return {"message": "Patient Management System API"}


@app.get("/about")
def about() -> dict:
    return {"message": "A fully functional API to manage your patients records."}


@app.get("/services")
def services() -> dict:
    return {"message": "We provide our state of the art APIs for free"}


@app.get("/contact")
def contact() -> dict:
    return {"message": "If any query please contact to +918605060204"}


@app.get("/view")
def view_data() -> dict:
    data = load_data()
    return data


# view patient by ID
@app.get("/patient/{pat_id}")
def view_patient(pat_id: str = Path(
    ...,
    description="Enter Patient ID",
    example="P001"
)) -> dict:
    data = load_data()

    if pat_id in data:
        return data[pat_id]

    raise HTTPException(status_code=404, detail="Patient Not Found!")


# sort patient by weight, height and BMI or in ascending or descending order
@app.get("/sort")
def sort_data(
    sort_by: str = Query(...,
                         description="Sort on the basis of height, weight and BMI"),
    order: str = Query(description="sort in ascending or descending order")
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=404, detail=f"Invalid Filed! select from {valid_fields}")

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=404, detail="Invalid Order! select between asc or desc")

    data = load_data()

    if order == "asc":
        sort_order = False
    else:
        sort_order = True

    sorted_data = sorted(
        data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data


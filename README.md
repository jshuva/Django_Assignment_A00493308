# MCDA5550: Web Mobile and Cloud Application
## REST API Project - Hotel Reservation System

**Student Details:**  
Name: Jayanta Sarker Shuva  
Email: Jayanta.sarker.shuva@smu.ca  
Student ID: A00493308  

**Live API Deployment:**  
The API is fully deployed and interactive via Swagger UI:  
👉 [https://jshuva09.pythonanywhere.com/api/docs/](https://jshuva09.pythonanywhere.com/api/docs/)

---

This is a REST API made with Django Rest Framework for a Hotel Reservation System, satisfying the course assignment requirements.

## Features
- `getListOfHotels` - Returns a list of hotels from the simulation.
- `reservationConfirmation` - Books a room and returns a confirmation number.

## Requirements
- `uv` for python dependencies
- Python 3.10+

## Setup & Run Instructions
1. Navigate to the `hotel_api` directory:
   ```bash
   cd hotel_api
   ```
2. Set up the environment and install dependencies automatically using `uv`:
   ```bash
   uv sync
   ```
3. Run database migrations prefixing with `uv run` to use the virtual environment:
   ```bash
   uv run python manage.py makemigrations api
   uv run python manage.py migrate
   ```
4. Populate dummy hotel data (Optional):
   ```bash
   uv run python populate.py
   ```
5. Run the local development server:
   ```bash
   uv run python manage.py runserver
   ```
7. Use Postman or another REST client to test the endpoints at `http://127.0.0.1:8000/`.

## API Definition
No authentication (API Keys/credentials) is currently required for these endpoints.

### 1. Get List of Hotels
- **Endpoint**: `/api/getListOfHotels`
- **Method**: `GET`
- **Query Params**: `checkin` (optional), `checkout` (optional)
- **Response**: List of hotel objects.

Example request:
```
GET http://127.0.0.1:8000/api/getListOfHotels?checkin=2026-04-01&checkout=2026-04-05
```
Example response:
```json
[
  {
    "hotel_name": "The Grand Budapest Hotel"
  },
  {
    "hotel_name": "Overlook Hotel"
  }
]
```

### 2. Reservation Confirmation
- **Endpoint**: `/api/reservationConfirmation`
- **Method**: `POST`
- **Description**: Submits a hotel reservation and returns a confirmation number.
- **Request Body**:
```json
{
  "hotel_name": "The Grand Budapest Hotel",
  "checkin": "2026-04-01",
  "checkout": "2026-04-05",
  "guests_list": [
    {
      "guest_name": "John Doe",
      "gender": "Male"
    },
    {
      "guest_name": "Jane Doe",
      "gender": "Female"
    }
  ]
}
```
- **Response**:
```json
{
  "confirmation_number": "A1B2C3D4"
}
```

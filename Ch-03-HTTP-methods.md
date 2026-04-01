# 🌐 HTTP Methods

## 🌐 HTTP Request–Response Flow (Client → Server)

```mermaid
sequenceDiagram
    participant Client (Browser / App)
    participant Server (FastAPI / Backend)
    participant Database

    Client->>Server: HTTP Request (GET / POST / PUT / DELETE)
    Note right of Client: Sends data + headers

    Server->>Server: Process Request
    Note right of Server: Business logic runs

    Server->>Database: Query / Save / Update / Delete
    Database-->>Server: Data Response

    Server-->>Client: HTTP Response (JSON / Status Code)
    Note left of Server: 200, 404, 500 etc.
```

---

## 🔥 What’s REALLY happening (no fluff)

* Client = browser / mobile app / frontend
* Server = your FastAPI app
* HTTP Request = “hey server, do this”
* HTTP Response = “done, here’s result”

---

# 📦 Structure of HTTP Request

```text
GET /students HTTP/1.1
Host: example.com
Authorization: Bearer token

Body (optional)
```

---

# 📤 Structure of HTTP Response

```text
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "success",
    "data": [...]
}
```

---

# 🧠 HTTP Methods mapped to CRUD

Stop memorizing blindly. Understand intent.

| HTTP Method | CRUD Operation   | Meaning (Real World)  |
| ----------- | ---------------- | --------------------- |
| GET         | Read             | Fetch data            |
| POST        | Create           | Add new data          |
| PUT         | Update (full)    | Replace entire data   |
| PATCH       | Update (partial) | Update specific field |
| DELETE      | Delete           | Remove data           |

---

## 🔁 CRUD Mapping Diagram

```mermaid
flowchart LR
    A[Client Action] --> B[HTTP Method]
    B --> C[Server Operation]
    C --> D[Database]

    A1[View Students] -->|GET| C1[Read Data]
    A2[Add Student] -->|POST| C2[Create Data]
    A3[Update Student] -->|PUT / PATCH| C3[Update Data]
    A4[Delete Student] -->|DELETE| C4[Delete Data]
```

---

# 💻 FastAPI Example (Reality Check)

```python
from fastapi import FastAPI

app = FastAPI()

# READ
@app.get("/students")
def get_students():
    return {"students": []}

# CREATE
@app.post("/students")
def create_student(student: dict):
    return {"msg": "student created"}

# UPDATE
@app.put("/students/{id}")
def update_student(id: int):
    return {"msg": "student updated"}

# DELETE
@app.delete("/students/{id}")
def delete_student(id: int):
    return {"msg": "student deleted"}
```

---

# ⚠️ Where most beginners mess up (including you if not careful)

* Thinking **HTTP methods = just syntax** → WRONG
  → They define **intent + API design**

* Using `GET` to send data → BAD practice

* Using `POST` for everything → lazy design

* Not understanding status codes → weak backend skills

---

# 🧠 Final Mental Model

Think like this:

> Client = “What I want”
> HTTP Method = “What action”
> Server = “How to do it”
> Database = “Where data lives”

---
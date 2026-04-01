# 🔹 What are Query Parameters?

Query parameters are **optional inputs sent in the URL after `?`**.

Example:

```
/students?age=20&course=CS
```

They are used to **modify or filter data**, not identify a specific resource.

---

## 🔹 Why Query Parameters Exist (Real Reason)

If you think they’re just “extra inputs”, you’re missing the point.

They exist for:

* Filtering → `?age=20`
* Sorting → `?sort=price`
* Pagination → `?page=2`
* Searching → `?name=akshit`

👉 In short:
**Query params = control how data is returned**

Not *which* data, but *how*.

---

## 🔹 Clean Example (Not Your Code)

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/students")
def get_students(
    course: str | None = Query(None, description="Filter by course"),
    min_age: int | None = Query(None, ge=0),
    page: int = Query(1, ge=1)
):
    return {
        "course": course,
        "min_age": min_age,
        "page": page
    }
```

---

## 🔹 Key Things You Should Actually Notice

* `None` → makes parameter optional
* `Query(...)` → used for validation + docs
* `ge=1` → validation (greater than or equal)
* Automatically appears in Swagger UI

👉 This is why FastAPI is powerful:
You get **validation + docs + parsing** for free.

---

# 🔥 Path vs Query Parameters (This is where most people mess up)

If you don’t understand this, your API design will be garbage.

---

## 🔹 Path Parameters

Example:

```
/students/101
```

Used for:

* Identifying a **specific resource**

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}
```

👉 Meaning:
“Give me THIS exact student”

---

## 🔹 Query Parameters

Example:

```
/students?course=CS
```

Used for:

* Filtering
* Sorting
* Searching
* Pagination

👉 Meaning:
“Give me students, but apply conditions”

---

# ⚔️ Direct Comparison (No Fluff)

| Concept  | Path Parameter    | Query Parameter       |
| -------- | ----------------- | --------------------- |
| Purpose  | Identify resource | Modify result         |
| Required | Usually required  | Usually optional      |
| Position | Inside URL path   | After `?`             |
| Example  | `/students/101`   | `/students?course=CS` |
| Meaning  | Exact item        | Filtered list         |

---

# 🧠 Real-World Thinking (This is what matters)

Let’s say you're building a real API.

### ❌ Wrong Thinking

```
/getStudentsByCourse/CS
```

This is bad design. You’re misusing path params.

---

### ✅ Correct Thinking

```
/students?course=CS
```

---

### ❌ Another Mistake

```
/students?student_id=101
```

👉 Wrong. This should be:

```
/students/101
```

---

# 💥 Simple Rule (Memorize This)

* If it’s **required to find the resource → Path**
* If it’s **optional to shape/filter data → Query**

---

# ⚠️ Brutal Truth

If you mix these up:

* Your API becomes inconsistent
* Hard to scale
* Looks amateur in interviews

Good backend engineers are judged heavily on this.

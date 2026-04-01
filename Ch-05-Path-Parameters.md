
# 🔥 Path Parameters in FastAPI (Deep Understanding)

## 1. What a Path Parameter actually is

A **path parameter** is a dynamic value inside the URL path.

Example:

```
/students/S001
```

Here:

* `/students/` → fixed route
* `S001` → **path parameter value**

In FastAPI:

```python
@app.get("/students/{student_id}")
def get_student(student_id: str):
    return {"id": student_id}
```

👉 `{student_id}` is a placeholder
👉 FastAPI extracts it from URL and passes it to the function

---

## 2. How FastAPI Processes It Internally

This is where most people stay shallow. You shouldn’t.

### Flow:

1. Client sends request:

   ```
   GET /students/S001
   ```

2. FastAPI (via Starlette router):

   * Matches `/students/{student_id}`
   * Extracts `student_id = "S001"`

3. Validation (via Pydantic):

   * Ensures type = `str`
   * If mismatch → error

4. Injects into function:

   ```python
   get_student(student_id="S001")
   ```

---

## 3. Your Code — Let’s Break It Brutally

```python
def search_student(
    student_id: str = Path(
        ...,
        description='ID of the student in DB',
        example='S001'
    )
):
```

### 🔹 `student_id: str`

* Type annotation
* Used for:

  * validation
  * auto docs
  * editor support

---

### 🔹 `Path(...)` — THIS IS IMPORTANT

This is NOT default value.

It is **metadata + validation config**

---

## 4. What does `...` (Ellipsis) mean?

```python
Path(...)
```

👉 Means: **REQUIRED parameter**

If you don’t provide:

```
/students/
```

👉 FastAPI will return:

```
422 Unprocessable Entity
```

---

## 5. Path vs Query Parameter (Don’t mix this up)

### Path:

```
/students/S001
```

### Query:

```
/students?student_id=S001
```

### Difference:

| Feature      | Path Param        | Query Param         |
| ------------ | ----------------- | ------------------- |
| Required     | Always            | Optional by default |
| Used for     | Resource identity | Filtering/search    |
| URL position | Inside path       | After `?`           |

👉 If you're using path param incorrectly for filtering → you're designing APIs wrong.

---

## 6. Validation with Path

You can enforce strict constraints:

```python
from fastapi import Path

@app.get("/students/{student_id}")
def get_student(
    student_id: str = Path(
        ...,
        min_length=3,
        max_length=10,
        regex="^S[0-9]+$"
    )
):
    return {"id": student_id}
```

### What this enforces:

* Must start with `S`
* Must be numeric after that
* Length between 3–10

👉 `/students/abc` → ❌ rejected
👉 `/students/S123` → ✅ accepted

---

## 7. Type Conversion (Silent but powerful)

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

### Behavior:

* `/items/10` → works
* `/items/abc` → ❌ 422 error

👉 FastAPI auto converts + validates

---

## 8. Multiple Path Parameters

```python
@app.get("/students/{student_id}/courses/{course_id}")
def get_course(student_id: str, course_id: str):
    return {
        "student": student_id,
        "course": course_id
    }
```

URL:

```
/students/S001/courses/C101
```

---

## 9. Order Matters (Critical Mistake People Make)

```python
@app.get("/users/me")
def get_current_user():
    return "me"

@app.get("/users/{user_id}")
def get_user(user_id: str):
    return user_id
```

👉 `/users/me` must come **before**

Otherwise:

* `"me"` gets treated as `user_id`
* Your route breaks logically

---

## 10. Path Parameters in OpenAPI Docs

Your `Path()` metadata appears in Swagger UI:

* description
* example
* validation rules

👉 This is why FastAPI feels “magical”

---

## 11. Common Mistakes (You need to avoid these)

### ❌ Mistake 1: Using Path for optional data

```python
/students/{filter}
```

Wrong.

👉 Use query params instead

---

### ❌ Mistake 2: No validation

```python
student_id: str
```

👉 Too loose. Always restrict if possible.

---

### ❌ Mistake 3: Treating IDs as free text

If your ID format is fixed → enforce it.

---

## 12. Real-World Example (Closer to production)

```python
@app.get("/students/{student_id}")
def search_student(
    student_id: str = Path(
        ...,
        title="Student ID",
        description="Unique student identifier",
        regex="^S[0-9]{3}$",
        example="S001"
    )
):
    return {"student_id": student_id}
```

---

## 13. Mental Model (You must lock this in)

Think:

> Path parameter = identity of resource

* `/students/S001` → specific student
* `/products/10` → specific product

👉 If removing it changes the meaning of endpoint → it's a path param
👉 If it's optional → it's NOT a path param

---
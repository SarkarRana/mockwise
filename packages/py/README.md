# mockwise (Python)

Realistic, edge-case-aware test fixtures generated from your Pydantic v2 models.

See the [monorepo root](../../README.md) for the full pitch.

## Install

```bash
pip install mockwise
```

## Usage

```python
from pydantic import BaseModel, EmailStr, Field
from mockwise import generate

class User(BaseModel):
    email: EmailStr
    age: int = Field(ge=13)

users = await generate(User, count=50, edge_cases=True)
```

## Status

**Pre-release.** API is implemented incrementally — see the [project plan](../../README.md#status).

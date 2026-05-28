# mockwise

> Realistic, edge-case-aware test fixtures generated from your Zod or Pydantic schemas. Drop into your tests directly, or call from Claude Code / Cursor via MCP.

`mockwise` generates test data that's both realistic *and* deliberately exercises the edges of your schema — boundary values, unicode, empty optionals, max-length strings. It targets the two places developers actually define schemas in code (Zod for TypeScript, Pydantic for Python) and ships as a library plus an MCP server.

## Status

Pre-release. The MVP targets Zod and Pydantic v2 only — see [the plan](https://github.com/sarkarrana/mockwise#roadmap) for phased expansion to Drizzle, Prisma, SQLAlchemy and beyond.

## Packages

This is a pnpm monorepo with three packages:

| Package | Path | Distributed as |
|---|---|---|
| TypeScript library | [packages/ts](packages/ts) | `mockwise` on npm |
| Python library | [packages/py](packages/py) | `mockwise` on PyPI |
| MCP server | [packages/mcp](packages/mcp) | `@mockwise/mcp` on npm + MCP marketplaces |

## Quickstart

> **Not published yet.** Snippets below show the intended API.

### TypeScript

```ts
import { z } from "zod";
import { generate } from "mockwise";

const User = z.object({
  email: z.string().email(),
  age: z.number().int().min(13),
});

const users = await generate(User, { count: 50, edgeCases: true });
```

### Python

```python
from pydantic import BaseModel, EmailStr, Field
from mockwise import generate

class User(BaseModel):
    email: EmailStr
    age: int = Field(ge=13)

users = await generate(User, count=50, edge_cases=True)
```

### MCP (Claude Code / Cursor)

```
> Generate 50 users matching my User Zod schema, with edge cases around the age boundary.
```

## Why not just use Faker / polyfactory / zod-fixture?

Those tools are schema-aware but **edge-case-blind** — they generate random values from the middle of the schema's range. Real bugs hide at boundaries: a user with age 13 exactly, an email at the max length limit, a unicode name with combining characters, an empty optional field. `mockwise` deliberately targets those edges, then fills the rest with realistic-looking data (names paired with cultures, addresses that geocode, plausible timestamps).

## Development

```bash
# Install everything
pnpm install
cd packages/py && pip install -e ".[dev]"

# Run tests
pnpm -r test
cd packages/py && pytest
```

## License

MIT — see [LICENSE](LICENSE).

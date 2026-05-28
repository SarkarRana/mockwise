# mockwise (TypeScript)

Realistic, edge-case-aware test fixtures generated from your Zod schemas.

See the [monorepo root](../../README.md) for the full pitch.

## Install

```bash
npm install mockwise zod
# or
pnpm add mockwise zod
```

## Usage

```ts
import { z } from "zod";
import { generate } from "mockwise";

const User = z.object({
  email: z.string().email(),
  age: z.number().int().min(13),
});

const users = await generate(User, { count: 50, edgeCases: true });
```

## Status

**Pre-release.** API is implemented incrementally — see the [project plan](../../README.md#status).

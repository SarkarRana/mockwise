# @mockwise/mcp

MCP server that lets Claude Code, Cursor, or any MCP-aware client generate test fixtures from a Zod or Pydantic schema.

See the [monorepo root](../../README.md) for the full pitch.

## Install (Claude Code)

```bash
claude mcp add mockwise -- npx -y @mockwise/mcp
```

## Install (Cursor)

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "mockwise": {
      "command": "npx",
      "args": ["-y", "@mockwise/mcp"]
    }
  }
}
```

## Usage

```
> Generate 50 users matching this Zod schema, with edge cases around the age boundary.
```

## Status

**Pre-release.** See the [project plan](../../README.md#status).

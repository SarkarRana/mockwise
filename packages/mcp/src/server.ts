#!/usr/bin/env node

async function main(): Promise<void> {
  throw new Error("mockwise-mcp: server not implemented yet — see plan weeks 6–7");
}

main().catch((err: unknown) => {
  console.error(err);
  process.exit(1);
});

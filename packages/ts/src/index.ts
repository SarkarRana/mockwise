import type { ZodTypeAny, z } from "zod";

export interface GenerateOptions {
  count?: number;
  edgeCases?: boolean;
  seed?: number;
  provider?: "openai" | "anthropic" | "ollama";
  model?: string;
}

export async function generate<T extends ZodTypeAny>(
  _schema: T,
  _options: GenerateOptions = {},
): Promise<z.infer<T>[]> {
  throw new Error("mockwise: generate() not implemented yet — see plan weeks 2–3");
}

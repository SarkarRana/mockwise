from typing import TYPE_CHECKING, Any, Literal, TypeVar

if TYPE_CHECKING:
    from pydantic import BaseModel

__version__ = "0.0.0"

M = TypeVar("M", bound="BaseModel")

Provider = Literal["openai", "anthropic", "ollama"]


async def generate(
    model: type[M],
    count: int = 1,
    *,
    edge_cases: bool = False,
    seed: int | None = None,
    provider: Provider = "openai",
    model_name: str | None = None,
) -> list[M]:
    """Generate realistic, edge-case-aware fixtures matching a Pydantic model.

    Not implemented yet — see project plan weeks 4–5.
    """
    raise NotImplementedError(
        "mockwise: generate() not implemented yet — see plan weeks 4–5"
    )


__all__ = ["generate", "Provider", "__version__"]

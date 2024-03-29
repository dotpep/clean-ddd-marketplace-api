from dataclasses import dataclass


@dataclass(frozen=True)
class ProductFiltersEntity:
    """Domain Entity of ProductFilters."""
    search: str | None = None

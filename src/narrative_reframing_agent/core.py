"""Core rule-based narrative reframing logic."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


LIMITING_MARKERS = ("i always", "i never", "i can't", "i am stuck", "i failed")
STRENGTH_MARKERS = ("learned", "built", "adapted", "persisted", "led", "shipped")


@dataclass
class ReframeResult:
    """Structured narrative reframing output."""

    reframed_identity: str
    strength_based_narrative: str
    decision_framing: str
    detected_limitations: list[str]

    def to_dict(self) -> dict[str, Any]:
        """Return JSON-serializable output."""
        return asdict(self)


def reframe_narrative(text: str) -> ReframeResult:
    """Produce a neutral, strengths-oriented reframing from raw narrative text."""
    lowered = text.lower()
    detected_limitations = [marker for marker in LIMITING_MARKERS if marker in lowered]
    strengths = [marker for marker in STRENGTH_MARKERS if marker in lowered]

    if not strengths:
        strengths = ["adapted"]

    reframed_identity = (
        "You are a founder navigating constraints through iterative learning, "
        "rather than a fixed identity defined by a single difficult period."
    )
    strength_based_narrative = (
        "Observed agency signals suggest resilience and execution capacity: "
        + ", ".join(strengths)
        + "."
    )
    decision_framing = (
        "Frame near-term decisions as experiments with bounded downside, "
        "explicit assumptions, and clear learning goals."
    )

    return ReframeResult(
        reframed_identity=reframed_identity,
        strength_based_narrative=strength_based_narrative,
        decision_framing=decision_framing,
        detected_limitations=detected_limitations or ["no explicit limiting marker detected"],
    )

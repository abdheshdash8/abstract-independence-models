"""
ci.py
=====

Core representation of Conditional Independence (CI) statements.

This module defines the fundamental CIStatement class used throughout
the AIM (Abstract Independence Models) library.

A conditional independence statement has the form

    A ⟂ B | C

where

A : non-empty set of variables
B : non-empty set of variables
C : conditioning set

References
----------
Lauritzen, S. L. (1996)
    Graphical Models.

Sadeghi, K.
    Faithfulness of Probability Distributions and Graphs.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet, Iterable, Hashable


Variable = Hashable


@dataclass(frozen=True, slots=True)
class CIStatement:
    """
    Represents one conditional independence statement.

    A ⟂ B | C

    Parameters
    ----------
    A
        Left variable set.

    B
        Right variable set.

    C
        Conditioning set.

    Notes
    -----
    Internally all variable collections are stored as frozensets
    so that the object is immutable and hashable.

    Examples
    --------
    >>> CIStatement({"A"}, {"B"}, {"C"})
    {A} ⟂ {B} | {C}

    >>> CIStatement({"X","Y"}, {"Z"}, set())
    {X,Y} ⟂ {Z} | ∅
    """

    A: FrozenSet[Variable]
    B: FrozenSet[Variable]
    C: FrozenSet[Variable]

    # -----------------------------------------------------
    # Constructor
    # -----------------------------------------------------

    def __init__(
        self,
        A: Iterable[Variable],
        B: Iterable[Variable],
        C: Iterable[Variable] = (),
    ):

        object.__setattr__(self, "A", frozenset(A))
        object.__setattr__(self, "B", frozenset(B))
        object.__setattr__(self, "C", frozenset(C))

        self._validate()

    # -----------------------------------------------------
    # Validation
    # -----------------------------------------------------

    def _validate(self) -> None:
        """
        Validate the CI statement.

        Raises
        ------
        ValueError
            If the CI statement is invalid.
        """

        if len(self.A) == 0:
            raise ValueError("A must be non-empty.")

        if len(self.B) == 0:
            raise ValueError("B must be non-empty.")

        if self.A & self.B:
            raise ValueError(
                "A and B must be disjoint."
            )

    # -----------------------------------------------------
    # Canonical representation
    # -----------------------------------------------------

    def canonical(self) -> "CIStatement":
        """
        Return canonical ordering.

        Since

            A ⟂ B | C

        is identical to

            B ⟂ A | C

        we always keep the lexicographically smaller side first.

        Returns
        -------
        CIStatement
        """

        left = tuple(sorted(map(str, self.A)))
        right = tuple(sorted(map(str, self.B)))

        if left <= right:
            return self

        return CIStatement(self.B, self.A, self.C)

    # -----------------------------------------------------
    # Properties
    # -----------------------------------------------------

    @property
    def is_elementary(self) -> bool:
        """
        True if

            |A| = |B| = 1
        """
        return len(self.A) == 1 and len(self.B) == 1

    @property
    def variables(self) -> FrozenSet[Variable]:
        """
        All variables appearing in the statement.
        """
        return self.A | self.B | self.C

    @property
    def order(self) -> tuple[int, int, int]:
        """
        Returns

        (|A|,|B|,|C|)
        """
        return (
            len(self.A),
            len(self.B),
            len(self.C),
        )

    # -----------------------------------------------------
    # Pretty printing
    # -----------------------------------------------------

    @staticmethod
    def _format_set(S: FrozenSet[Variable]) -> str:

        if len(S) == 0:
            return "∅"

        return (
            "{"
            + ",".join(
                sorted(map(str, S))
            )
            + "}"
        )

    def __str__(self):

        return (
            f"{self._format_set(self.A)} "
            f"⟂ "
            f"{self._format_set(self.B)} "
            f"| "
            f"{self._format_set(self.C)}"
        )

    def __repr__(self):

        return (
            "CIStatement("
            f"A={self._format_set(self.A)}, "
            f"B={self._format_set(self.B)}, "
            f"C={self._format_set(self.C)})"
        )

    # -----------------------------------------------------
    # Comparisons
    # -----------------------------------------------------

    def __lt__(self, other):

        if not isinstance(other, CIStatement):
            return NotImplemented

        return (
            tuple(sorted(map(str, self.A))),
            tuple(sorted(map(str, self.B))),
            tuple(sorted(map(str, self.C))),
        ) < (
            tuple(sorted(map(str, other.A))),
            tuple(sorted(map(str, other.B))),
            tuple(sorted(map(str, other.C))),
        )

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self):

        return {
            "A": sorted(map(str, self.A)),
            "B": sorted(map(str, self.B)),
            "C": sorted(map(str, self.C)),
        }

    @classmethod
    def from_dict(cls, d):

        return cls(
            d["A"],
            d["B"],
            d.get("C", []),
        )

    # -----------------------------------------------------
    # Symmetry
    # -----------------------------------------------------

    def symmetric(self):

        """
        Return

            B ⟂ A | C
        """

        return CIStatement(
            self.B,
            self.A,
            self.C,
        )

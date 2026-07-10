#!/usr/bin/env python3
"""Pre-registered WCAG contrast reference (PAIR-OPUS rubric, 2026-07-09).

Judge recomputation is authoritative over any in-repo checker.
Usage: python3 wcag-contrast-check.py '#1a1a2e' '#f5f5f5'  -> prints ratio.
"""
import sys


def srgb_to_lin(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexcolor: str) -> float:
    h = hexcolor.lstrip("#")
    h = "".join(ch * 2 for ch in h) if len(h) == 3 else h
    r, g, b = (int(h[i : i + 2], 16) / 255.0 for i in (0, 2, 4))
    return 0.2126 * srgb_to_lin(r) + 0.7152 * srgb_to_lin(g) + 0.0722 * srgb_to_lin(b)


def contrast(a: str, b: str) -> float:
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


if __name__ == "__main__":
    print(f"{contrast(sys.argv[1], sys.argv[2]):.4f}")

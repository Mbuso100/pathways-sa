# ADR-0001: Separate eligibility decisions from generative AI

Status: Accepted for prototype (2026-11-18)

## Context
Opportunity guidance may be costly or harmful if AI invents eligibility rules. Source data can be incomplete or unverified.

## Decision
Evaluate explicit verified requirements with deterministic domain rules. Return stable reason codes. When source verification is missing, return `needs_verification`. AI may later explain the result but cannot override it.

## Trade-offs
This prototype only supports NQF-level and province constraints. Real qualifications, subjects, citizenship, age, deadlines, accommodations, equivalence rules and programme-specific exceptions are not yet modeled. NQF level alone does not establish eligibility for any actual programme. No real opportunity should be presented as eligible based solely on this prototype.

## Next steps
Introduce source provenance, rule versioning, programme-specific conditions, human verification and multilingual terminology review.

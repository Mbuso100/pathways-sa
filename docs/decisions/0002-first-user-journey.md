# ADR 0002 — Build a complete exploration journey before AI integration

**Status:** Accepted for prototype, subject to user research.

## Context

The product must offer value even when there are no verified vacancies. AI-generated aptitude claims would be misleading, and a large unverified listings database would undermine trust.

## Decision

Implement a bilingual, no-account journey: welcome → fictional scenario → non-diagnostic reflection → exploratory career information → official source portals. Keep the reflection deterministic and transparent. Do not persist user choices. Keep source portals separate from live opportunity records.

## Consequences

The initial experience is usable without an AI provider or database, but is **not** personalized career counseling, an aptitude assessment, or a production-ready opportunity platform. The initial isiZulu copy requires human review. Career content is illustrative. Real opportunities require provenance, dated verification and moderation.

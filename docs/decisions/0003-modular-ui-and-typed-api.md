# ADR 0003 — Modular frontend and explicit API response contracts

**Status:** Accepted for Milestone A.

## Context

The initial frontend combined image-heavy landing content, state transitions, HTTP calls, types and copy in one large entrypoint. The API returned untyped dictionaries, so response drift could escape review.

## Decision

Keep one React application and one FastAPI service. Extract the landing presentation, API client, shared frontend types and translations from the React entrypoint. Define Pydantic response models for the public API. Keep deterministic discovery and eligibility rules in framework-independent Python modules.

## Trade-offs

This is intentionally not microservices or a complex state-management framework. UI journey orchestration remains in `main.tsx` for now and merits further component-level decomposition when the interaction surface grows. API response validation does not replace end-to-end browser tests or editorial review of career content.

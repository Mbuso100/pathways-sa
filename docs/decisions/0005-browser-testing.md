# ADR 0005 — Browser-level journey verification

## Context

Unit tests verify translation keys and HTTP helpers, but not the interaction between React, FastAPI, and browser navigation.

## Decision

Use Playwright with Chromium to run the actual English and isiZulu discovery journeys against local FastAPI and Vite servers. Keep the existing unit and API tests. Browser tests check observable behavior, not implementation details, although the current selectors use CSS classes pending accessible-role improvements.

## Trade-offs

Browser tests require a browser download and are slower than unit tests. The full test should run in CI as a separate quality gate. The homepage appearance is not redesigned for this change.

## Follow-up

Improve accessible names for interactive controls; expand browser coverage for failed requests and small-screen navigation. Review dependencies regularly.

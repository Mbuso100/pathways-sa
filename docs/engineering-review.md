# Engineering review: unit-test / browser-test discovery conflict

## Context

When Playwright browser tests were introduced in v0.8, the frontend's `npm run check` failed: Vitest discovered `e2e/water-challenge.spec.ts` and attempted to run Playwright's `test()` under Vitest.

## Diagnosis

The two tools use different test runners. The failure was test discovery and runner configuration, not evidence that the water-challenge UI logic was incorrect.

## Decision and correction

A dedicated `apps/web/vitest.config.ts` restricts Vitest discovery to `src/**/*.test.ts` and `src/**/*.test.tsx`, excluding `e2e/**`. Playwright independently uses `testDir: './e2e'`. This preserves unit and browser tests as distinct quality gates rather than suppressing a failing test.

A separate startup issue occurred when Playwright launched system Python without Uvicorn. The v0.9 config prefers the repository's isolated API virtual environment and falls back to `python` for CI. Browser workers are limited to one after a local machine freeze during initial execution; the freeze's root cause was not established.

## Verification evidence and boundaries

After the Vitest discovery fix, the user reported `npm run check` passing (6 Vitest tests plus build/lint/typecheck), 24 backend pytest tests passing, and both English and isiZulu Chromium journeys passing twice. This evidence applies to the locally tested v0.8 state. The updated v0.9 config must be rerun locally and in GitHub Actions before calling the release CI-verified.

## What this demonstrates

Debugging requires identifying the failing boundary, choosing a targeted configuration fix, and validating with separate automated checks. This is a real AI-assisted engineering workflow; no unobserved AI-generated defects or fabricated benchmark results are claimed.

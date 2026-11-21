import { existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { defineConfig, devices } from '@playwright/test';

// Prefer the project's isolated Python environment on developer machines.
// GitHub Actions uses the Python interpreter provisioned by setup-python.
const venvPython = resolve(
  dirname(fileURLToPath(import.meta.url)),
  process.platform === 'win32' ? '../api/.venv/Scripts/python.exe' : '../api/.venv/bin/python',
);
const python = existsSync(venvPython) ? `"${venvPython}"` : 'python';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: false,
  workers: process.env.CI ? 1 : 1,
  retries: process.env.CI ? 1 : 0,
  reporter: process.env.CI ? 'github' : 'list',
  use: { baseURL: 'http://127.0.0.1:5173', trace: 'retain-on-failure' },
  projects: [{ name: 'chromium', use: { ...devices['Desktop Chrome'] } }],
  webServer: [
    {
      command: `${python} -m uvicorn pathways.api.main:app --app-dir ../api --host 127.0.0.1 --port 8000`,
      url: 'http://127.0.0.1:8000/health',
      reuseExistingServer: !process.env.CI,
      timeout: 45_000,
    },
    {
      command: 'npm run dev',
      url: 'http://127.0.0.1:5173',
      reuseExistingServer: !process.env.CI,
      timeout: 45_000,
    },
  ],
});

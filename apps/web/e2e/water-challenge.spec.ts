import { test, expect } from '@playwright/test';

for (const lang of ['en', 'zu'] as const) {
  test(`water challenge discovery flow in ${lang}`, async ({ page }) => {
    await page.goto('/');
    await page.locator('header select').selectOption(lang);
    const start = page.locator('.hero .actions button').first();
    await expect(start).toBeVisible();
    await start.click();
    await expect(page.locator('.panel .choices button').first()).toBeVisible();
    const reflect = page.locator('.panel .actions button').last();
    await expect(reflect).toBeDisabled();
    await page.locator('.panel .choices button').first().click();
    await expect(reflect).toBeEnabled();
    await reflect.click();
    await expect(page.locator('.panel .notice')).toBeVisible();
    // Continue to the three-stage exploration and verify feedback and progression.
    await page.locator('.panel .actions button').first().click();
    for (let stage = 0; stage < 3; stage++) {
      await expect(page.locator('.panel .choices button').first()).toBeVisible();
      await page.locator('.panel .choices button').first().click();
      await page.locator('.panel .actions button').last().click();
      await expect(page.locator('.panel [role="status"]')).toBeVisible();
      await page.locator('.panel .actions button').last().click();
    }
    await expect(page.locator('.panel .card-grid')).toBeVisible();
    await page.locator('.panel .actions button').first().click();
    await expect(page.locator('.panel .card-grid a').first()).toBeVisible();
  });
}

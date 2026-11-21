import { describe, expect, it } from 'vitest';
import { copy } from './copy';

describe('bilingual interface copy', () => {
  it('provides corresponding English and isiZulu keys', () => {
    expect(Object.keys(copy.en).sort()).toEqual(Object.keys(copy.zu).sort());
  });
  it('has nonempty translations for every key', () => {
    for (const language of ['en', 'zu'] as const) {
      for (const [key, value] of Object.entries(copy[language])) {
        expect(value.trim(), `${language}.${key}`).not.toBe('');
      }
    }
  });
});

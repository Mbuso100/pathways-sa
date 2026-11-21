import { afterEach, describe, expect, it, vi } from 'vitest';
import { get, post } from './api';

afterEach(() => vi.unstubAllGlobals());

describe('API client', () => {
  it('reads a successful JSON response', async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true, json: async () => ({ items: [] }) });
    vi.stubGlobal('fetch', fetchMock);
    await expect(get('/v1/careers')).resolves.toEqual({ items: [] });
    expect(fetchMock).toHaveBeenCalledWith(expect.stringMatching(/\/v1\/careers$/));
  });

  it('sends a JSON POST request', async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true, json: async () => ({ choice_id: 'a' }) });
    vi.stubGlobal('fetch', fetchMock);
    await post('/v1/discovery/reflections', { choice_id: 'a' });
    expect(fetchMock).toHaveBeenCalledWith(expect.stringMatching(/\/v1\/discovery\/reflections$/), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ choice_id: 'a' }),
    });
  });

  it('rejects unsuccessful responses instead of returning malformed data', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: false, status: 422 }));
    await expect(post('/v1/discovery/reflections', { choice_id: 'invalid' })).rejects.toThrow('API');
  });

  it('propagates connection failures', async () => {
    vi.stubGlobal('fetch', vi.fn().mockRejectedValue(new TypeError('Failed to fetch')));
    await expect(get('/v1/resources')).rejects.toThrow('Failed to fetch');
  });
});

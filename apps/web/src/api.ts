const API = import.meta.env.VITE_API_URL || 'http://localhost:8000';
export async function get<T>(path:string):Promise<T>{const r=await fetch(`${API}${path}`);if(!r.ok)throw Error('API');return r.json()}
export async function post<T>(path:string, body:unknown):Promise<T>{const r=await fetch(`${API}${path}`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});if(!r.ok)throw Error('API');return r.json()}

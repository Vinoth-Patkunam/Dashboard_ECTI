// src/app/services/api.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class ApiService {
  constructor(private http: HttpClient) {}

  getAll<T>(resource: string) {
    return this.http.get<T[]>(`/api/${resource}/`);
  }
}


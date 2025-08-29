// src/app/services/multidb.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MultiDbService {
  constructor(private http: HttpClient) {}

  /**
   * GET /api/ → { [tableName: string]: url }
   */
  getApiRoot(): Observable<Record<string, string>> {
    return this.http.get<Record<string, string>>(
      '/api/?format=json',
      { headers: { 'Accept': 'application/json' } }
    );
  }

  /**
   * GET /api/models/{dbAlias}/{modelName}/fields/?format=json → string[]
   */
  getFields(dbAlias: string, modelName: string): Observable<string[]> {
    return this.http.get<string[]>(
      `/api/models/${dbAlias}/${modelName}/fields/?format=json`,
      { headers: { 'Accept': 'application/json' } }
    );
  }

  /**
   * GET /api/{tableName}/?format=json → any[]
   */
  getData<T = any>(tableName: string): Observable<T[]> {
    return this.http.get<T[]>(
      `/api/${tableName}/?format=json`,
      { headers: { 'Accept': 'application/json' } }
    );
  }
}

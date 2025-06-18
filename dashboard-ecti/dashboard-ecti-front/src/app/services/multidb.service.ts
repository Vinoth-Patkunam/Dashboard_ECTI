// src/app/services/multidb.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

/**
 * Ce service fournit trois méthodes pour récupérer :
 *  - la liste des modèles (tables) d’une base donnée,
 *  - la liste des champs d’un modèle précis,
 *  - les données brutes de ce modèle.
 */
@Injectable({
  providedIn: 'root'
})
export class MultiDbService {
  constructor(private http: HttpClient) {}

  /** GET /api/models/{dbAlias}/ → string[] */
  getApiRoot(): Observable<Record<string, string>> {
    // On ajoute "?format=json" pour forcer JSON, sinon DRF peut renvoyer du HTML
    return this.http.get<Record<string, string>>('/api/');
  }

  /** GET /api/models/{dbAlias}/{modelName}/fields/ → string[] */
  getFields(dbAlias: string, modelName: string): Observable<string[]> {
    return this.http.get<string[]>(`/api/models/${dbAlias}/${modelName}/fields/`);
  }

  /** GET /api/data/{dbAlias}/{modelName}/ → any[] */
  getData<T = any>(tableName: string): Observable<T[]> {
  return this.http.get<T[]>(`/api/${tableName}/?format=json`, {
    headers: { 'Accept': 'application/json' }
  });
}
}

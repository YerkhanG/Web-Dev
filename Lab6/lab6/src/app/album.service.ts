import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Album} from "./models";
import {Photos} from "./photos";

@Injectable({
  providedIn: 'root'
})
export class AlbumService {

  constructor(private client: HttpClient) { }

  getAlbums(): Observable<Album[]>{
    return this.client.get<Album[]>('https://jsonplaceholder.typicode.com/albums');
  }

  getAlbum(id: number): Observable<Album>{
    return this.client.get<Album>(`https://jsonplaceholder.typicode.com/albums/${id}`)
  }
  updateAlbumTitle(id: number, newTitle: string): Observable<any> {
    return this.client.put(`https://jsonplaceholder.typicode.com/albums/${id}`, { title: newTitle })
  }

  getPhotos(id: number): Observable<Photos[]> {
    return this.client.get<Photos[]>(`https://jsonplaceholder.typicode.com/albums/${id}/photos`);
  }
}

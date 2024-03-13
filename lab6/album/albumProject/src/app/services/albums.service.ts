import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Album } from '../module';
import { Observable } from 'rxjs';
import { Photo } from '../module';

@Injectable({
  providedIn: 'root'
})
export class AlbumsService {

  constructor(private client: HttpClient) { }
  MAIN_URL= 'https://jsonplaceholder.typicode.com/'
  getAlbums(): Observable<Album[]>{
    return this.client.get<Album[]>(this.MAIN_URL + 'albums');
  }

  getAlbum(id:number): Observable<Album>{
    return this.client.get<Album>(this.MAIN_URL + 'albums/' + id);
  }

  deleteAlbum(id: number){
    return this.client.delete(this.MAIN_URL + 'albums/' + id)

  }

 createAlbum(newAlbum:Album): Observable<Album>{
  return this.client.post<Album>(this.MAIN_URL + 'albums/', newAlbum);
 }
 
 getPhotos(id:number): Observable<Photo[]>{
  return this.client.get<Photo[]>(this.MAIN_URL + 'albums/' + id + '/photos');
  
 }

 editAlbum(id:number, album: Album):Observable<Album>{
  return this.client.put<Album>(this.MAIN_URL + 'albums/'+ id, album)
 }

}

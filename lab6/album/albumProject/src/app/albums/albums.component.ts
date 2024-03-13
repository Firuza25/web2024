import { Component, OnInit } from '@angular/core';
import { ALBUMS } from '../my_db';
import { Album } from '../module';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { AlbumsService } from '../services/albums.service';
import { FormsModule, NgModel } from '@angular/forms';

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './albums.component.html',
  styleUrl: './albums.component.css'
})
export class AlbumsComponent  implements OnInit{
  albums!: Album[];
  newAlbum: string;
  loaded?: boolean;

  constructor(private albumService: AlbumsService){
    this.newAlbum = '';

  }

  ngOnInit() {
    this.getAlbums();
  }
  getAlbums(){
    this.loaded = false; 
    this.albumService.getAlbums().subscribe((albums)=>{
      this.albums = albums
      this.loaded = true;
    });

  }



  addAlbum(){
    const newAlbum: Album = {
      id: this.albums?.length!+1,
      title: this.newAlbum
    };
    this.loaded = false
    this.albumService.createAlbum(newAlbum).subscribe((album)=>{
      this.albums.push(newAlbum);
      alert('album created');
      this.newAlbum= " "
      this.loaded = true;
    });
  }



 

  deleteAlbum(id:number){
    this.albumService.deleteAlbum(id).subscribe(()=>{
      console.log('deleted');
    });
    this.albums = this.albums.filter(a => a.id !== id);
  }

  



}

import { Component, NgModule, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap, RouterModule } from '@angular/router';
import { Album } from '../module';
import { AlbumsService } from '../services/albums.service';
import { CommonModule } from '@angular/common';
import {Location} from "@angular/common";
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [RouterModule,CommonModule,FormsModule],
  templateUrl: './album-detail.component.html',
  styleUrl: './album-detail.component.css'
})
export class AlbumDetailComponent implements OnInit {
  album?: Album;
  loaded?: boolean;
  saving?:boolean;
  newTitle: string;

  constructor(private route: ActivatedRoute,
     private albumService: AlbumsService,  
     private location: Location){
      this.newTitle = "";

  }


  ngOnInit() {
    this.getAlbum()
  }

  getAlbum(){
    this.route.paramMap.subscribe((params)=>{
      const albumId = Number(params.get('id'));
      this.loaded = false;
      this.albumService.getAlbum(albumId).subscribe((album) => {
        this.album = album;
        this.loaded = true;
      });
      // this.album = ALBUMS.find((album: Album):boolean => album.id === albumId) as Album;

    })
  }

  updateAlbumTitle(album: Album) {
    this.albumService.editAlbum(this.album!.id,album ).subscribe((updated) => {
    console.log(updated)
      alert('title updated');
    });
  }
  

 
  

  // updateAlbumTitle(newAlbum:Album){
  //   if (this.album) {
  //     this.saving = true;
  //     this.albumService.editAlbum(newAlbum).subscribe((updated)=>{
  //      this.album = updated; 
  //       console.log(updated);
  //       this.saving = false;
  //     });
  // }
  // }


 

  returnBack(){
    this.location.back();
  }



}


import { Component, OnInit } from '@angular/core';
import { Photo } from '../module';
import { CommonModule, Location } from "@angular/common";
import { AlbumsService } from '../services/albums.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-album-photos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './album-photos.component.html',
  styleUrl: './album-photos.component.css'
})
export class AlbumPhotosComponent implements OnInit {
  photos!: Photo[];
  loaded!: boolean;

  constructor(private route: ActivatedRoute, 
    private albumService: AlbumsService, 
    private location: Location){

  }


  ngOnInit() {
    this.getPhotos();
  
    }
    getPhotos(){
      this.route.paramMap.subscribe((params)=>{
        const albumId = Number(params.get('id'));
        this.loaded=false;
        this.albumService.getPhotos(albumId).subscribe((photos)=>{
          this.photos = photos;
          this.loaded = true;
        });
      });

    }
    returnBack(){
      this.location.back();
    }
  }
import { Component, OnInit, NgModule } from '@angular/core';
import { SneakersService } from '../services/sneakers/sneakers.service';
import { CommonModule } from '@angular/common';
import { Sneakers } from '../shared/models/Sneakers';
import { ActivatedRoute } from '@angular/router';
import { TagsComponent } from "../tags/tags.component";


@Component({
    selector: 'app-home-page',
    standalone: true,
    templateUrl: './home-page.component.html',
    styleUrl: './home-page.component.css',
    imports: [CommonModule, TagsComponent]
})

export class HomePageComponent implements OnInit {
  
  sneakers:Sneakers[]=[];
  constructor(private sneakersService:SneakersService, private route: 
    ActivatedRoute){}

    ngOnInit(): void {
      this.route.params.subscribe(params =>{
        const tag = params['tag'];
        if(tag && tag.toLowerCase() !== 'all'){
          this.sneakers = this.sneakersService.getAll().filter(sneakerss => sneakerss.name.toLowerCase().
          includes(params['tag'].toLowerCase())); 
        } else {
          this.sneakers = this.sneakersService.getAll();
        }
      })
      
  }
  toggleLike(sneakers: Sneakers): void {
    sneakers.likeCounter++;
  }

  deleteProduct(index:number): void {
    this.sneakers.splice(index, 1);
    this.sneakersService.deleteProduct(index);
  }


  
}

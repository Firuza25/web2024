import { Component, OnInit } from '@angular/core';
import { Tag } from '../shared/models/Tags';
import { SneakersService } from '../services/sneakers/sneakers.service';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-tags',
  standalone: true,
  imports: [CommonModule,RouterModule],
  templateUrl: './tags.component.html',
  styleUrl: './tags.component.css'
})
export class TagsComponent implements OnInit {

  tags?:Tag[] = []
  constructor(private sneakersService: SneakersService){}

  ngOnInit(): void {
    this.tags = this.sneakersService.getAllTags()
      
  }

}

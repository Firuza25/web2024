import { Injectable } from '@angular/core';
import { Sneakers, sn_products } from '../../shared/models/Sneakers';
import { Tag } from '../../shared/models/Tags';
@Injectable({
  providedIn: 'root'
})
export class SneakersService {

  constructor() { }

  getAllTags(): Tag[]{
    return [
      {name: "All"},
      {name: "Adidas"},
      {name: "Nike"},
      {name: "Skechers"},
      {name: "Asics"}
    ];
  }

  getAllFoodsByTag(tag: string): Sneakers[] {
    return tag == "All" ?
      this.getAll() :
      this.getAll().filter(sneakers => sneakers['tags']?.includes(tag));
  }



  getAll(): Sneakers[] {
      return sn_products;
  }
}

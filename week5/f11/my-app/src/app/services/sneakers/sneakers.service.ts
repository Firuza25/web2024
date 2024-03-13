import { Injectable } from '@angular/core';
import { Sneakers, sn_products } from '../../shared/models/Sneakers';
import { Tag } from '../../shared/models/Tags';
@Injectable({
  providedIn: 'root'
})
export class SneakersService {

   private snikers = [...sn_products];

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

  getAll(): Sneakers[] {
      return this.snikers;
  }

  deleteProduct(index:number): void {
    this.snikers.splice(index, 1)
  }
}
